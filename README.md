# Project Proposal: Optimal Portfolio Generator

## 0.5. Installation Instructions:
- Python version, packages, etc.
- Jupyter Notebook

## 1. Introduction:
The project aims to develop an application that generates an optimal investment portfolio based on a user's risk tolerance and desired return profile. The portfolio optimizer will utilize historical price data of various assets such as bonds, stocks, and cryptocurrencies to construct an efficient frontier and recommend a portfolio allocation that maximizes returns for a given level of risk.

## 2. Project Structure:
The project will be structured as follows:

### 2.1 Data Gathering:
Historical price data will be collected from various sources using APIs. Yahoo Finance will be utilized for stock and bond data, considering a timeframe of at least three years due to API limitations. Additional data sources, such as the Federal Reserve sites, will be explored for supplementary economic indicators.

**Assets to be included:**
- **Bonds:**
  - Vanguard Aggregated Bond ETF (AGG)
  - Vanguard International Bond ETF (BNDX)
- **Stocks:**
  - S&P 500 (SPX)
  - S&P 500 Growth
  - S&P 500 Value
- **Cryptocurrencies:**
  - Bitcoin (BTC)
  - Ethereum (ETH)

### 2.2 Optimization Algorithm:
- User's risk tolerance and desired return profile will be collected as input.
- Historical risk-return profiles of each asset will be analyzed.
- An optimization algorithm, similar to Excel's Solver but implemented in Python using `scipy.optimize`, will be employed to generate optimal portfolio weights.
- Pre-calculated scenarios based on user risk preferences will be considered to facilitate quick portfolio allocation.

### 2.3 Portfolio Construction:
- A DataFrame will be created to capture volatility, returns, and weights of each asset combination.
- The optimization algorithm will generate multiple portfolios ranging from conservative to aggressive based on risk-return preferences.
- Volatility constraints will be enforced to ensure the generated portfolios align with the user's risk tolerance.

### 2.4 User Interface:
- A user-friendly interface will be developed to input risk preferences and display recommended portfolios.
- Selected portfolio compositions will be presented to the user along with their corresponding risk-return profiles.

### 2.5 Monte Carlo Simulation:
- After selecting a portfolio, a Monte Carlo simulation will be conducted to forecast the investment's performance over a specified time horizon.
- The simulation will provide a range of expected returns with a 95% confidence interval, offering insights into potential investment outcomes.

## 3. Deliverables:
- Interactive application for portfolio optimization and selection.
- Documentation outlining project methodology, including data sources and optimization techniques.
- Monte Carlo simulation results for selected portfolios.
- User guide explaining how to use the application and interpret results.

## 4. Timeline:
- Data Gathering and Preprocessing: 2 weeks
- Optimization Algorithm Development: 3 weeks
- Portfolio Construction and User Interface: 4 weeks
- Monte Carlo Simulation Integration: 2 weeks
- Testing and Debugging: 2 weeks
- Documentation and Finalization: 2 weeks

## 5. Conclusion:
The proposed project aims to empower users to make informed investment decisions by providing personalized portfolio recommendations based on their risk preferences. By leveraging historical data and advanced optimization techniques, the application will enable users to construct optimal portfolios tailored to their individual financial goals and risk tolerance levels.
