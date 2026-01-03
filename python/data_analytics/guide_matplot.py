"""
Created on Thu Jan  1 10:26:46 2026

@author: cl4pper
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

grades = np.array([2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 9, 9, 10, 10])
answers = np.array([2, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5, 5, 4, 5, 4])

sorted_grades = np.sort(grades)
sorted_answers = np.sort(answers)

max_grade = np.max(sorted_grades)
max_answers = np.max(sorted_answers)

unique_grades = len(np.unique(sorted_grades))

# creates an array from 0 to max grade
x_axis = np.append(np.arange(max_grade), max_grade)

# creates an array from 0 to the max frequency among the array elements
y_axis = np.append(
    np.arange(np.max(np.bincount(answers))), np.max(np.bincount(answers))
)

plt.xlabel("Grades")
plt.ylabel("Answers")
plt.title("Relation Grades x Answers")
plt.yticks(y_axis)

plt.grid(True)

"""
PLOT

Plots y versus x as lines and/or markers.
"""

# plt.plot(sorted_grades, sorted_answers)

"""
SCATTER

A scatter plot of y vs. x with varying marker size and colors.
"""

# this logic calculates the density of each x,y relation
rel_grades_answers = np.vstack([sorted_grades, sorted_answers])
gaussian_relation = gaussian_kde(rel_grades_answers)(rel_grades_answers)

# c=colors, s=size
plt.scatter(
    sorted_grades,
    sorted_answers,
    s=gaussian_relation * 1000,
    c=gaussian_relation,
    alpha=0.5,
)

"""
HISTOGRAM

Bins/groups the data from array and
count the number of values in each bin,
then draws the distribution.
"""

# plt.hist(sorted_grades, bins=x_axis, range=(0, max_grade), orientation='vertical', color='green')

"""
Uncomment the chart call to plot it.
Keep this line bellow to plot the charts.
"""
plt.show()
