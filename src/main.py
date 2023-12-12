# The code is importing the necessary libraries, `yfinance` and `datetime`, to retrieve historical
# stock data.
import yfinance as yf
import datetime as dt

# Define the ticker symbol and time frame
tickerSymbol = 'NVDA'
start = dt.datetime(2022, 1, 1)
end = dt.datetime(2023, 12, 12)

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get historical prices for this ticker
tickerDf = tickerData.history(start=start, end=end, interval='5d')

# See your data
print(tickerDf)
save_to_csv = False  # Set this to True to save the data to CSV

if save_to_csv:
    tickerDf.to_csv('NVDA_stock_data.csv', index=False)

