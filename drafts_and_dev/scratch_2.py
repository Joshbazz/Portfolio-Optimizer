import hvplot.pandas  # Step 1: Import hvplot.pandas

class MCSimulation:
    def __init__(self, ...):
        ...

    def plot_distribution(self):
        """
        Visualizes the distribution of cumulative returns simulated using calc_cumulative_return method.
        """
        # Check to make sure that simulation has run previously.
        if not isinstance(self.simulated_return, pd.DataFrame):
            self.calc_cumulative_return()

        # Use hvplot to create a probability distribution histogram of simulated ending prices
        # with markings for a 95% confidence interval
        plot_title = f"Distribution of Final Cumulative Returns Across All {self.nSim} Simulations"
        plot = self.simulated_return.iloc[-1, :].hvplot.hist(bins=10, title=plot_title, density=True)
        plot *= hvplot.hline(self.confidence_interval.iloc[0], color='r')
        plot *= hvplot.hline(self.confidence_interval.iloc[1], color='r')
        return plot


# Convert DataFrame column to a Pandas Series
        simulated_returns_series = self.simulated_return.iloc[-1, :]

        # Use hvplot to create a probability distribution histogram of simulated ending prices
        # with markings for a 95% confidence interval
        plot_title = f"Distribution of Final Cumulative Returns Across All {self.nSim} Simulations"
        plot = simulated_returns_series.hvplot.hist(bins=10, title=plot_title, density=True)
        plot *= hvplot.hline(self.confidence_interval.iloc[0], color='r')
        plot *= hvplot.hline(self.confidence_interval.iloc[1], color='r')
        return plot