from scipy.optimize import minimize
import yfinance as yf
import datetime
import pandas as pd
import numpy as np

# Define the list of stock ticker symbols
tickers = ['AGG', 'BNDX', 'SPY', 'IVW', 'IVE', 'BTC-USD', 'ETH-USD']

# Calculate the start date (three years ago from today)
start_date = datetime.datetime.now() - datetime.timedelta(days=1095)


def ticker_data_pull():

    new_df = pd.DataFrame()
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

    print(new_df)

    return new_df, ticker_closes


new_df, ticker_closes = ticker_data_pull()

# Print the list of ticker close column names
print("Ticker Close Column Names:", ticker_closes)


# get the exponentially weighted annualized return and standard deviation for each asset
def agg_returns_std_dev(new_df=new_df):
    span = len(new_df)  # Adjust the span for three years of historical data

    # Calculate the annualized exponentially weighted mean return for each asset
    annualized_mean_return = new_df.ewm(span=span).mean().iloc[-1] * 252

    # Calculate the annualized exponentially weighted standard deviation (risk) for each asset
    annualized_std_dev = new_df.ewm(span=span).std().iloc[-1] * np.sqrt(252)

    # Display annualized risk and return for each asset
    for ticker in tickers:
        print(f'{ticker}:')
        print(f'Annualized Mean Return: {annualized_mean_return[f"{ticker}_Daily_Return"]:.2%}')
        print(f'Annualized Risk (Standard Deviation): {annualized_std_dev[f"{ticker}_Daily_Return"]:.2%}')
        print()

    return new_df, annualized_mean_return, annualized_std_dev


annualized_mean_return = agg_returns_std_dev()[1]
annualized_std_dev = agg_returns_std_dev()[2]


# Create a dictionary with calculated values
def individual_assets():    
    assets_data = {
        'Ticker': tickers,
        'Annualized_Mean_Return': [annualized_mean_return[f"{ticker}_Daily_Return"] for ticker in tickers],
        'Annualized_Std_Dev': [annualized_std_dev[f"{ticker}_Daily_Return"] for ticker in tickers]
    }

    # Convert the dictionary into a DataFrame
    individual_assets = pd.DataFrame(assets_data)

    # Print the DataFrame
    print(individual_assets)

    return individual_assets

# optimize the portfolio weights to arrive at a target return
# ***NOTE*** when calling, adjust the target_return parameter to get different weights
def optimize_portfolio(agg_mean_return, target_return=0.05):
    # Define the objective function to minimize
    def objective_function(weights, mean_returns, target_return):
        # Calculate the portfolio return
        portfolio_return = np.dot(mean_returns, weights)
        # Calculate the squared difference between the portfolio return and the target return
        return (portfolio_return - target_return) ** 2

    # Define initial guess for weights
    initial_guess = np.ones(len(agg_mean_return)) / len(agg_mean_return)  # Equal weights initially

    # Define constraint function to ensure weights sum to 1
    def constraint(weights):
        return np.sum(weights) - 1

    # Perform optimization
    result = minimize(objective_function, initial_guess, args=(agg_mean_return, target_return), method='SLSQP', bounds=[(0, 1)] * len(agg_mean_return), constraints={'type': 'eq', 'fun': constraint})

    # Print optimization result
    print("Optimization Result:")
    print(result)
    print("Optimal solution:", result.x)

    # Round the optimal solution to a certain number of decimal places
    rounded_solution = np.round(result.x, decimals=4)

    # Ensure that the rounded weights sum up to 1
    rounded_solution /= np.sum(rounded_solution)

    # Print the rounded and normalized solution
    print("Optimal solution (rounded and normalized):", rounded_solution)
    
    return result.x

# Example usage:
agg_mean_return = individual_assets()['Annualized_Mean_Return']
optimal_weights = optimize_portfolio(agg_mean_return)
