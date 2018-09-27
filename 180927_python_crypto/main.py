import os.path
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# pyplot setup
plt.style.use('ggplot')
plt.rc('pgf',  texsystem='pdflatex')
plt.rc('text', usetex=True)
plt.rcParams['text.latex.preamble'] = [r'\usepackage{lmodern}']
plt.rcParams['figure.figsize'] = (5, 5)
plt.rcParams['figure.dpi'] = 300

# data directory
DIR = 'data'

class Crypto(object):
    '''class for accessing historical crypto data. instances of this class
    act like a dict mapping symbol names to historical data.

    '''
    def __init__(self):
        '''

        '''
        self.cache = dict()
        self.date = None

    def setdate(self, date):
        '''set the current date (for backtesting)'''
        assert date is None or isinstance(date, datetime.datetime)
        self.date = date

    def __getitem__(self, symbol):
        '''return historical data for the given symbol'''

        # load data not in cache from disk
        if symbol not in self.cache:
            self.cache[symbol] = load_symbol(symbol)

        # make a copy of the cached data (in case the user modifies
        # the returned df)
        df = self.cache[symbol].copy()

        # truncate by date
        if self.date is not None:
            df = df.iloc[df.index < self.date]

        return df

    def __setitem__(self, symbol, df):
        '''set an item in the cache'''
        self.cache[symbol] = df
        return

def load_symbol(symbol, date=None):
    '''return historical data for the give symbol. the data is read from
    disk.

    args:

    symbol: string representing the symbol, e.g., 'BTC'.

    date: load data up until this date, e.g., for backtesting.

    '''
    if not isinstance(symbol, str):
        raise TypeError('symbol must be a string')
    if date is not None and not isinstance(date, datetime.datetime):
        raise TypeError('date must be None or of type datetime')

    # input normalization
    symbol = symbol.upper()

    # load data from disk
    filename = os.path.join(DIR, symbol + '.csv')
    df = pd.read_csv(filename)

    # use canonical column names
    df.rename(index=str, inplace=True, columns={
        '1a. open (EUR)': 'open',
        '4a. close (EUR)': 'close',
    })

    # convert index to datetime
    df.index = pd.to_datetime(df['date'])

    # truncate by date
    if date is not None:
        df = df.iloc[df.index < date]

    return df

def load_symbols(symbols, date=None):
    '''return a list of historical data for all symbols in iterable
    symbols.

    '''
    return [load_symbol(symbol, date=date) for symbol in symbols]

def plot_dfs(dfs, symbols, column='close'):
    '''plot all symbols in iterable symbols.'''
    assert len(dfs) == len(symbols), 'len(dfs) must equal len(symbols)'
    plt.figure()
    for df, symbol in zip(dfs, symbols):
        plt.semilogy(df[column], '-', label=symbol)
    plt.title(f'Crypto Value ({column})')
    plt.ylabel('EUR')
    plt.legend()
    plt.tight_layout()
    plt.show()
    return

def plot_crypto(crypto, symbols, column='close', plot_function=None):
    assert isinstance(crypto, Crypto)
    if not plot_function:
        plot_function = plt.plot
    plt.figure()
    for symbol in symbols:
        df = crypto[symbol]
        plot_function(df[column], '-', label=symbol)
    plt.title(f'Crypto Value ({column})')
    plt.ylabel('EUR')
    plt.legend()
    plt.tight_layout()
    plt.show()

def crypto_divide(crypto, symbol1, symbol2):
    '''divide the opening and closing value of symbol1 with those of
    symbol2.

    - avoiding bloated class

    '''
    df1 = crypto[symbol1]
    df2 = crypto[symbol2]
    df = pd.DataFrame()
    df['open']= df1['open'] / df2['open']
    df['close']= df1['close'] / df2['close']
    return df

def crypto_f(crypto, f, symbol1, symbol2):
    '''return a new df with columns open=f(open1, open2) and
    close=f(close1, close2).

    - first class functions and lambas

    '''
    df1 = crypto[symbol1]
    df2 = crypto[symbol2]
    df = pd.DataFrame()
    df['open']= f(df1['open'], df2['open'])
    df['close']= f(df1['close'], df2['close'])
    return df

def main():
    crypto = Crypto()
    date = datetime.datetime(2017, 6, 1)
    crypto.setdate(date)
    crypto['doge/btc'] = crypto_f(
        crypto,
        lambda x,y: x / y,
        'doge',
        'btc',
    )
    df = crypto['doge/btc']
    print(df)
    symbols = ['doge/btc']
    # symbols = ['doge', 'btc', 'ltc', 'bch', 'eth']
    plot_crypto(crypto, symbols)

if __name__ == '__main__':
    main()
