# Here is some made up data
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np

"""
ESTIMATING THE COEFFICIENTS
- Single Linear Regression
- Plotting Results
- Multiple Linear Regression

Data: Bikesharing
http://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset
Citation: Fanaee-T, Hadi, and Gama, Joao, 'Event labeling combining 
ensemble detectors and background knowledge', Progress in 
Artificial Intelligence (2013): pp. 1-15, Springer Berlin Heidelberg,
"""
# Dataset: How many people rent capitol bikeshare bikes
bike_dat = pd.read_csv("day.csv")
bike_dat.head()

# Plot the data in a scatter plot
plt.scatter(bike_dat.atemp, bike_dat.cnt, alpha=0.3)  # Plot the raw data

# Estimate the model parameters
est_s = smf.ols(formula='cnt ~ temp', data=bike_dat).fit()

# View the model estimates
est_s.summary()

# Create the line based on parameters
# Create line with 100 points bsed on the x-range
x_prime = pd.DataFrame({'temp': np.linspace(bike_dat.temp.min(), 
                                             bike_dat.temp.max(), 100)})

# Generate the predictions using the built in method
y_hat = est_s.predict(x_prime)

# Plot the data with scatter plot
plt.scatter(bike_dat.temp, bike_dat.cnt, alpha=0.3)
plt.xlabel("Temperature")
plt.ylabel("Number of Bike Rentals")

# Add a line to the same plot
plt.plot(x_prime, y_hat, 'r', linewidth=2, alpha=0.9)

# Plot the residuals (more on this later)
plt.figure()
plt.scatter(est_s.predict(bike_dat), est_s.resid, alpha=0.3)
plt.xlabel("Predicted Rentals")
plt.ylabel("Residuals")


"""
COMMON PROBLEMS - Multicollinearity
"""

# temp is significant by itself
# temp is no longer significant
est_m = smf.ols(formula='cnt ~ atemp + temp + workingday + windspeed', 
                data=bike_dat).fit()
est_m.summary()

# Scatter plot
cols = ['cnt','atemp','windspeed','weathersit','temp','workingday','hum']
pd.scatter_matrix(bike_dat[cols])

# Correlation coefficient matrix
corr_matrix = np.corrcoef(bike_dat[cols].T)
sm.graphics.plot_corr(corr_matrix, xnames=cols)

# Let's say we wanted to include an interaction term
# We would do this by including the : between interacting variables
est_m = smf.ols(formula='cnt ~ temp + windspeed + temp:windspeed + workingday', 
                data=bike_dat).fit()

# Note: this is equivalent to:
est_m = smf.ols(formula='cnt ~ temp*windspeed + workingday',
                data=bike_dat).fit()

# What are the pros/cons associated with these methods?

"""
QUIZ: 
1) Read in the advertising data located at this link: http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv
2) Create a scatter matrix plot using pandas
3) Create a ols model using the statsmodels formula interface (Sales vs. TV)
4) Determine whether TV advertising impacts sales

"""

# 1) Read in advertising data
adv = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)

# 2) Create a scatter matrix plot using pandas
pd.scatter_matrix(adv)

# 3) Create a ols model using the statsmodels formula interface 
est = smf.ols(formula='Sales ~ TV', data=adv).fit()

# 4) Determine whether TV advertising impacts sales
est.summary()

"""
COMMON PROBLEMS - Heteroskedasticity
"""

# Plot the data and fitted line
x_prime = pd.DataFrame({'TV': np.linspace(adv.TV.min(), 
                                             adv.TV.max(), 100)})
y_hat = est.predict(x_prime)
plt.xlabel("TV")
plt.ylabel("Sales")
plt.title("Example of Heteroskedasticity")
plt.scatter(adv.TV, adv.Sales, alpha=0.3) 
plt.plot(x_prime, y_hat, 'r', linewidth=2, alpha=0.9)

# View the residuals
plt.figure()
plt.scatter(est.predict(adv), est.resid, alpha=0.3)
plt.xlabel("Predicted Sales")
plt.ylabel("Residuals")

#####
# Option #1: Log transform response
est = smf.ols(formula='np.log(Sales) ~ TV', data=adv).fit()
y_hat = est.predict(x_prime)
# Plot data
plt.figure()
plt.xlabel("TV")
plt.ylabel("log(Sales)")
plt.title("Log Transformation of y")
plt.scatter(adv.TV, np.log(adv.Sales), alpha=0.3) 
plt.plot(x_prime, y_hat, 'r', linewidth=2, alpha=0.9)

# View the residuals
plt.figure()
plt.scatter(est.predict(adv), est.resid, alpha=0.3)
plt.title("Residuals with Log Transformation of y")
plt.xlabel("Predicted log(Sales)")
plt.ylabel("Residuals")

#####
# Option #2: Weighted least squares
w =  1./(adv.TV)
est_wls = smf.wls(formula='Sales ~ TV', data=adv, weights = w).fit()


# What is the difference?
est = smf.ols(formula='Sales ~ TV', data=adv).fit()
y_hat = est.predict(x_prime)
y_hat_wls = est_wls.predict(x_prime)
plt.xlabel("TV")
plt.ylabel("Sales")
plt.title("OLS (red) vs. WLS (blue")
plt.scatter(adv.TV, adv.Sales, alpha=0.3) 
plt.plot(x_prime, y_hat, 'r', linewidth=2, alpha=0.9)
plt.plot(x_prime, y_hat_wls, 'b', linewidth=2, alpha=0.9)

# What are the pros and cons of these approaches?

"""
QUALITATIVE VARIABLES:
"""

# Weathersit is clearly a categorical variable
plt.hist(bike_dat.weathersit)

# Represent this variable with C() around it
est_m = smf.ols(formula='cnt ~ temp + hum + workingday + C(weathersit)', 
                data=bike_dat).fit()


"""
EXERCISE:
1) Read in the 'hour.csv' file
2) Run the regression with: cnt ~ temp + hum + workingday + hour + C(weathersit)
3) Evaluate the results, how does this compare with the day 
4) Create a binary variable for rush hour defined by 6-9a & 4-6p
5) Run the regression again. Does this new variable improve the results?
"""
