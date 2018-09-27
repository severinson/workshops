from crypto import plot_crypto, load_crypto

symbols = ['doge', 'btc']
dfs = [load_crypto(symbol) for symbol in symbols]
plot_crypto(dfs, symbols)
