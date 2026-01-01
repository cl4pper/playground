"""
Created on Thu Jan  1 10:26:46 2026

@author: cl4pper
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

"""
SCATTER

A scatter plot of y vs. x with varying marker size and colors.
"""

grades=[2,2,4,4,4,4,4,4,4,4,4,4,4,5,6,6,9,9,10]
answers=[2,3,5,5,5,5,5,5,5,5,5,5,5,4,5,5,5,4,5]

# this logic calculates the density of each x,y relation
grades_answers = np.vstack([grades, answers])
gaussian_relation = gaussian_kde(grades_answers)(grades_answers)

# c=colors, s=size
plt.scatter(grades, answers, c=gaussian_relation, s=gaussian_relation * 1000)

"""
HISTOGRAM

Bins/groups the data from array and
count the number of values in each bin,
then draws the distribution.
"""
array = [0,0,6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.5,3.9,4.2,6.5,6.8,7.1,7,8,9,3,9.5,9,9]

# plt.hist(array, bins=10, range=(0, 10), orientation='vertical', color='green')

"""
Uncomment the chart call to plot it.
Keep this line bellow to plot the charts.
"""
plt.show()