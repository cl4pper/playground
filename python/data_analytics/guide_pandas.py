import os

import numpy as np
import pandas as pd

"""
brics = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98],
}

brics_table = pd.DataFrame(brics)
brics_table.index = ["BR", "RU", "IN", "CH", "SA"]  # set index of each row
"""

BASE_DIR = os.getcwd()
csv_path = "/datasets/brics.csv"
# path = "/Users/cl4pper/Desktop/Projects/playground/python/data_analytics/datasets/brics.csv"
brics = pd.read_csv(BASE_DIR + csv_path, index_col=0)

print("Here we see the whole data:")
print(brics)

print("\nHere we limit the columns:")
print(brics[["country", "capital"]])  # printing as Pandas DataFrame
# print(brics["country", "capital"]) prints as Pandas Series

print("\nHere we slice the data rows:")
print(brics[1:4])

print("\nUsing loc approach:")
print(brics.loc[["BR", "CH"], ["capital", "population"]])  # Pandas DataFrame
print(brics.loc["BR"])  # Pandas DataFrame
# print(brics.loc[:, ["capital", "population"]]) is also possible
# print(brics.loc[:, "capital"]) prints as Pandas Series

print("\nUsing iloc approach:")
print(brics.iloc[[0, 3], [1, 3]])
# print(brics.loc[:, [1, 3]]) is also possible

print("\nLogic operators:")
large_area = brics["area"] < 10
small_area = brics["area"] > 5
average_area = np.logical_and(small_area, large_area)  # others: logical_or, logical_not
print(brics[average_area].loc[:, ["country"]])
