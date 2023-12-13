import yfinance as yf
import datetime as dt
import matplotlib.pyplot as plt
import plotly.graph_objs as go

def fetch_stock_data(ticker_symbol, start_date, end_date):
    """
    Fetch historical stock data from Yahoo Finance.

    :param ticker_symbol: Stock ticker symbol (e.g., 'NVDA').
    :param start_date: Start date for data retrieval (datetime object).
    :param end_date: End date for data retrieval (datetime object).
    :return: DataFrame with historical stock data.
    """
    ticker_data = yf.Ticker(ticker_symbol)
    return ticker_data.history(start=start_date, end=end_date, interval='1d')

def compute_RSI(data, window=14):
    """
    Compute the Relative Strength Index (RSI).

    :param data: Pandas Series of stock prices.
    :param window: The period for calculating RSI, typically 14.
    :return: Pandas Series representing the RSI.
    """
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).ewm(span=window, adjust=False).mean()
    loss = (-delta.where(delta < 0, 0)).ewm(span=window, adjust=False).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def add_technical_indicators(df):
    """
    Add technical indicators to the DataFrame.

    :param df: DataFrame with stock data.
    """
    df['50MDA'] = df['Close'].rolling(window=50).mean()
    df['100MDA'] = df['Close'].rolling(window=100).mean()
    df['VWAP'] = (df['Close'] * df['Volume']).cumsum() / df['Volume'].cumsum()
    df['RSI'] = compute_RSI(df['Close'])

def plot_data(df, ticker_symbol):
    """
    Create plots for stock data and technical indicators.

    :param df: DataFrame with stock data and indicators.
    :param ticker_symbol: Stock ticker symbol (e.g., 'NVDA').
    """
    # Plotting stock prices and moving averages
    plt.figure(figsize=(12, 6))
    plt.plot(df['Close'], label='Close Price')
    plt.plot(df['50MDA'], label='50-Day MDA')
    plt.plot(df['100MDA'], label='100-Day MDA')
    plt.title(f'{ticker_symbol} Stock Price with 50 and 100 Day Moving Averages')
    plt.legend()
    plt.show()

    # Plotting candlestick chart
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                         open=df['Open'],
                                         high=df['High'],
                                         low=df['Low'],
                                         close=df['Close'])])
    fig.update_layout(title=f'{ticker_symbol} Candlestick Chart',
                      xaxis_title='Date',
                      yaxis_title='Price (USD)',
                      xaxis_rangeslider_visible=True)
    fig.show()

# Main execution
start_date = dt.datetime(2022, 1, 1)
end_date = dt.datetime(2023, 12, 12)
ticker_symbol = 'NVDA'

ticker_df = fetch_stock_data(ticker_symbol, start_date, end_date)
add_technical_indicators(ticker_df)
plot_data(ticker_df, ticker_symbol)

# Print the DataFrame
print(ticker_df)
