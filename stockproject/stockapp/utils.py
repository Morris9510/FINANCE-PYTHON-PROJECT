import yfinance as yf
# Import other necessary libraries for analysis and plotting

def fetch_stock_data(ticker_symbol, start_date, end_date):
    # Fetch data using yfinance
    data = yf.download(ticker_symbol, start=start_date, end=end_date)
