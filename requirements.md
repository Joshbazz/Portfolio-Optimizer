Your assignment will be graded according to the expectations outlined in the following rubric.
Proficiency (≥ 90% of the points)
Approaching Proficiency (≥ 80% of the points)
Progressing (≥ 70% of the points)
Emerging (< 70% of the points)
Technical Requirements (75 points)

Software Version Control (10 points)

Repository is created on GitHub. (2 points) [DONE]
Files are frequently committed to the repository. (3 points) [DONE]
Commit messages include an appropriate level of detail. (2 points) [DONE]
Repository is organized and includes relevant information and project files. (3 points) [DONE]
Data Collection and Preparation (10 points) [DONE]

Data is collected from CSV files, APIs, or databases by using Python or a Python library. (5 points) [DONE]
Data is cleaned and prepared for the application or analysis by using Python or a Python library. (5 points) [DONE]
Financial Programming (40 points)

Code runs without errors and produces the assigned results. (25 points) [SORT OF DONE --> Josh]
Code uses good systems design with appropriate use of functions and modules for code organization. (5 points) [DONE]
Code uses DRY (don’t repeat yourself) principles and is as concise as possible. Variable names are short but specific. (5 points) [DONE]
Code incorporates a new Python library not previously covered in the course. (5 points) [DONE]
Documentation (15 points) [Ill go thru this --> Josh]

Code is well commented with concise, relevant notes. (5 points) [DONE-ish]
GitHub README file includes a concise project overview. (2 points) [DONE]
GitHub README file includes detailed usage and installation instructions. (3 points) [NOT DONE]
GitHub README includes either examples of the application, or the results and a summary of the analysis. (5 points) [add prints from end of file here]
Presentation Requirements (25 points)

Your presentation should cover the following:
An executive summary/overview of the project and project goals. (5 points)
    -> the goal is to get information from a User or Customer, and then return them a portfolio that is nearest to their needs
    -> the returned portfolio will have prescribed Asset Weights, Mean Return, Portfolio Standard Deviation, Simulated Future Returns Chart, and Distribution of Simulated Returns
An overview of the data collection, cleanup, and exploration processes. (5 points)
    -> Summary of the following:
        1. Get Assets from Yahoo Finance => dataframe => get Annual Returns and Standard Deviation 
        2. Solve for multiple Return Profiles => get Asset weights into dataframe
        3. Calculate correlations of assets and their respective weights to get Portfolio Standard Deviations
        4. Monte Carlo simulation for each portfolio, printing out a Sim Chart and a Return Distribution
        5. Return Summary Statistics and relevent information to the User
The approach that your group took in achieving the project goals. (5 points)
    1. collaboration and creativity
The results and conclusions of the financial application or analysis. (5 points)
    1. 25% ROI portfolio is the best Risk-Adjusted (Sharpe) on a historical basis, and after simulating all 5 portfolios over 1000 times, even though Portfolio 4 does not have the highest Simulated Return, it still consistently generates the Highest Simulated Sharpe Ratio, further strengthening the Analysis that the combination of Asset weights in Portfolio 4 show a strong tendency to give outsized Returns on a Risk-Adjusted Basis.
Any additional questions that surfaced, what your group might research next if more time was available, or share a plan for future development. (5 points)
Submission -> Further building out logic for more complex User Interaction, and/or giving more control to the user in terms of what Assets they would like to pick in order to construct their own portfolios and do the historical and simulation analysis themselves on a more ad-hoc basis

To submit your project, click Submit, and then provide the URL of your GitHub repository for grading. In addition to submitting your project individually, please fill out this form Links to an external site.. (You only need to submit one form per group.)