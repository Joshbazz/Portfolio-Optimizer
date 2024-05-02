import yfinance as yf
import datetime
import pandas as pd

# Define the list of stock ticker symbols
tickers = ['AGG', 'BNDX', 'SPY', 'IVW', 'IVE', 'BTC-USD', 'ETH-USD']

# Calculate the start date (three years ago from today)
start_date = datetime.datetime.now() - datetime.timedelta(days=1095)

# Initialize an empty dataframe to store the Close columns for each ticker
new_df = pd.DataFrame()

# Initialize an empty list to store the column names of Close prices for each ticker
ticker_closes = []

# Iterate over each ticker symbol
for ticker in tickers:
    # Fetch historical stock price data for the current ticker
    stock_data = yf.download(ticker, start=start_date, end=datetime.datetime.now())
    
    # Extract the 'Close' column and rename it for the current ticker
    close_column = stock_data[['Close']].rename(columns={'Close': f'{ticker}_Close'})
    
    # Compute the daily returns and insert them to the left of the corresponding ticker's Close column
    daily_returns = close_column.pct_change().rename(columns={f'{ticker}_Close': f'{ticker}_Daily_Return'})
    new_df = pd.concat([daily_returns, new_df], axis=1)
    
    # Append the Close column name for the current ticker to the ticker_closes list
    ticker_closes.append(f'{ticker}_Close')

# Drop rows containing NaNs from the new_df dataframe
new_df.dropna(inplace=True)

# Print the list of ticker close column names
print("Ticker Close Column Names:", ticker_closes)

# Print the new dataframe to verify
print(new_df)

asset_summary = new_df.describe()
print(asset_summary)
