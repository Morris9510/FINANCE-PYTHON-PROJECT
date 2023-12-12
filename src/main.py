import yfinance as yf
import plotly.graph_objs as go
import datetime as dt

# Define the ticker symbol and time frame
tickerSymbol = 'NVDA'
start = dt.datetime(2022, 1, 1)
end = dt.datetime(2023, 12, 12)

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get historical prices for this ticker
tickerDf = tickerData.history(start=start, end=end, interval='1d')

# Create a candlestick chart
fig = go.Figure(data=[go.Candlestick(x=tickerDf.index,
                open=tickerDf['Open'],
                high=tickerDf['High'],
                low=tickerDf['Low'],
                close=tickerDf['Close'])])

# Customize the appearance of the chart
fig.update_layout(
    title=f"{tickerSymbol} Candlestick Chart",
    xaxis_title='Date',
    yaxis_title='Price (USD)',
    xaxis_rangeslider_visible=True,  # Add a range slider for zooming
)

# Show the chart
fig.show()

# See your data
print(tickerDf)
