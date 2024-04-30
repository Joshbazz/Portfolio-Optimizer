notes for project structure
1. Portfolio optimizer based on a basket of indices/stocks/etc
    - user gets a risk tolerance, optimizer generates weights on each index, outputs an optimal portfolio

2. things to do:
- gather data from apis
        -> historical price data
        -> go back 5 years (depending on data allowance[3 could easier])
            - yahoo finance at least does 3
        -> fed reserve sites (may or may not be API -- should check) have lots of free data
    - What are we grabbing?
    [WE NEED TO PICK OUR ASSETS IN ORDER TO GET STARTED]
        -> BONDS
            1. Vanguard Aggregated Bond ETF (AGG)
            2. Vanguard International Bond ETF (BNDX)
        -> STOCKS
            1. SPX (overall SP500 index)
            2. SP500 Growth
            3. SP500 Value
        -> CRYPTO
            1. BTC
            2. ETH

- how are we going to get the weights?
    - how aggressive is the investor going to be based off risk/return?
        -> if we're targeting a risk/return profile, how do we back into that from our data?
        -> we'll need to analyze the historical risk return profiles for each asset we're using, then run some sort of optimizing algo that will do a curve fit to get close to the User's preferred profile
        -> maybe we can do one of three options that are pre-calced and based on the User's risk preference, we bucket them into one of the preprogrammed scenarios
    - is there a way to optimize weights based on bucketing? 
        -> WE CAN GENERATE HVPLOTS AND PYVIZ DURING PRECOMPUTING PORTION
        -> this is the solver in Excel but in Python: 
                from scipy.optimize import minimize

                # Define the objective function to minimize
                def objective_function(x):
                    return (x[0] - 1)**2 + (x[1] - 2)**2  # Example objective function (you would replace this with your own)

                # Define initial guess
                initial_guess = [0, 0]

                # Perform optimization
                result = minimize(objective_function, initial_guess, method='BFGS')

                # Print optimization result
                print("Optimization Result:")
                print(result)
                print("Optimal solution:", result.x)
        -> use Solver or something to get 10 (or N) portfolios (0 being 100% the AGG, 10 being 100% ETH), bucket out in between, generate 10 inbtermediate portfolios, return those to the user based on their risk/return profile
    
    - we would need another dataframe that is capturing the vol and returns and weights
        - 100% AGG and 100% ETH -> to set lower 
        - "we want the volatility to be 5-20, then => vol 10,7, etc."
        - calculate using the solver code, the Max vol, and min Vol, to spit out weights of return would be and weights of each of the assets -> send to dataframe / do same with maximum => then WE can create what the slices would be => "vol should be LESS than X, or MORE than Y"
    
    - return to the user -> fairly simple, can elaborate later

    - after returning the selected portfolio to the User, run a monte Carlo simulation on the portfolio to get: "Based on your risk and return, and the selected portfolio, here is a simulated return on your investment over an X year period. at a 95% Confidence interval, at the end of X years, your investment can be expected to be worth between (investmest - C.I. max loss) and (investment + C.I. max gain)

