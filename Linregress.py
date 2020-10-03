#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Linear regression using Scipy
from numpy.random import seed
from numpy.random import randn as rnd

#Set seed value
seed(32)

x = rnd(1000)
y = (3*x + 4) + rnd(1000)
# We add rnd(1000) to make small errors in the values, otherwise
# We would obtain a line

#Let us generate a plot to see the distribution 
import matplotlib.pyplot as plt
plt.scatter(x, y)
plt.show()

# To see how much correlated values are
from scipy.stats import pearsonr
corr_coef, p_value = pearsonr(x, y)

print(f"p_value: {p_value}, corr_coef: {corr_coef}")

# We see that corr coef is about 94% and p_value is below 0.05

# Now we will try and predict the linear regression line

from scipy.stats import linregress

slope, intercept, r_value, p_value, std_err = linregress(x,y)

print(f"Equation predicted is : y = {slope}*x + {intercept}")
print(f"Actual Equation is: y = 3*x + 4")

# Now we print the regression line
y_preds = slope*x + intercept
plt.scatter(x, y)
plt.plot(x, y_preds, c = 'orange')
plt.show()

# Let us get the r-squared score to check accuracy of regression
print('accuracy is {}'.format(r_value**2))