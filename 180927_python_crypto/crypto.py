import pandas as pd
import os.path
import matplotlib.pyplot as plt

# configure pyplot
plt.style.use('ggplot')

# directory with data files
DIR = 'data'

class Crypto(object):
    '''class for accessing hitorical market data'''

    def __init__(self, symbol):
        '''object constructor'''
        self.symbol = symbol
        print('object created with argument', symbol)

def load_crypto(symbol):
    '''return a df with historical data for the given symbol'''
    if not isinstance(symbol, str):
        raise TypeError('symbol must be a string')
    symbol = symbol.upper()

    # load from disk
    filename = os.path.join(DIR, symbol+'.csv')
    df = pd.read_csv(filename)

    # use canonical column names
    df.rename(index=str, inplace=True, columns={
        '1a. open (EUR)': 'open',
        '4a. close (EUR)': 'close',
    })

    # set index to dates
    df.index = pd.to_datetime(df['date'])

    return df

def plot_crypto(dfs, symbols):
    '''plot historical data in dfs'''
    plt.figure()
    for df, symbol in zip(dfs, symbols):
        plt.semilogy(df['close'], label=symbol)

    plt.legend()
    plt.title('Crypto Closing Price')
    plt.ylabel('EUR')
    plt.show()
    return

# def plot_crypto_old(symbols):
#     '''plot all symbols in iterable symbols.

#     args:

#     symbols: list of symbols, e.g., ['DOGE', 'BTC']

#     '''
#     plt.figure()
#     for symbol in symbols:
#         df = load_crypto(symbol)
#         print(symbol)
#         plt.semilogy(df['close'], label=symbol)

#     plt.legend()
#     plt.title('Crypto Closing Price')
#     plt.ylabel('EUR')
#     plt.show()
#     return

def main():
    print('does not execute on module import')
    symbols = ['doge', 'btc']
    dfs = [load_crypto(symbol) for symbol in symbols]
    plot_crypto(dfs, symbols)

print('executes on module import')
if __name__ == '__main__':
    main()
