"""
EXERCISE:
1) Read in the 'hour.csv' file
"""
import pandas as pd
import statsmodels.formula.api as smf
hour = pd.read_csv("../DAT3/data/hour.csv")
day = pd.read_csv("../DAT3/data/day.csv")

"""
2) Run the regression with: cnt ~ temp + hum + workingday + hour + C(weathersit)
"""
hmod = smf.ols(formula='cnt ~ temp + hum + workingday + hr + C(weathersit)', data=hour).fit()
"""
3) Evaluate the results, how does this compare with the day

The adjusted R-squared for the hour model (hmod) is lower than that for the 
day model (dmod)
"""

hmod.rsquared_adj #R2 = 0.328
dmod = smf.ols(formula='cnt ~ temp + hum + workingday + C(weathersit)', data=day).fit()
dmod.rsquared_adj #R2 = 0.457

"""
4) Create a binary variable for rush hour defined by 6-9a & 4-6p
"""

# Option #1: Manually specifying (not a best practice)
hour['rush'] = 0
hour['rush'][hour['hr'] == 6] = 1
hour['rush'][hour['hr'] == 7] = 1
hour['rush'][hour['hr'] == 8] = 1
hour['rush'][hour['hr'] == 9] = 1

hour['rush'][hour['hr'] == 16] = 1
hour['rush'][hour['hr'] == 17] = 1
hour['rush'][hour['hr'] == 18] = 1


# Option #2: Specifying a range
hour['rush2'] = 0
hour['rush2'][  ((hour['hr'] >= 6) & (hour['hr'] <= 9)) | 
                ((hour['hr'] >= 16) & (hour['hr'] <= 18))] = 1


# Option #3: Using the where command
import numpy as np
hour['rush3'] = np.where(   ((hour['hr'] >= 6) & (hour['hr'] <= 9)) | 
                            ((hour['hr'] >= 16) & (hour['hr'] <= 18)), 1, 0)

# Option #4: Using a seperate variable (not a best practice)
rush4 = ((hour.hr >= 6) & (hour.hr <=9)) | ((hour.hr >=16) & (hour.hr<=18))

# Option #5: Using the ternary operation within a list comprehension
hour['rush5'] = [1 if hour_it in [6,7,8,9,16,17,18] else 0 for hour_it in hour['hr']]

# Option #6: Using the anonymous function with the .apply command
hour['rush6'] = hour['hr'].apply(lambda x: 1 if (x>=6 and x<=9) or (x>=16 and x<=18) else 0)

"""
5) Run the regression again. Does this new variable improve the results?

Here are the adjusted R2 values
Day:    0.457
Hour1:  0.328 
Hour2:  0.395

Conclusion: The addition of the rush hour variable explains some of the variation,
however, there is more explained variation in the day model.
"""
hmod2 = smf.ols(formula='cnt ~ temp + hum + workingday + C(weathersit) + rush', data=hour).fit()
hmod2.rsquared_adj