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
brics = pd.read_csv(BASE_DIR + csv_path, index_col=0)

print("0. Here we see the whole data:")
print(brics)

print("\n1.a. Here we limit the columns:")
print(brics[["country", "capital"]])  # printing as Pandas DataFrame
# print(brics["country", "capital"]) prints as Pandas Series

print("\n1.b. Here we slice the data rows:")
print(brics[1:4])

print("\n2.a. Using loc approach:")
print(brics.loc[["BR", "CH"], ["capital", "population"]])  # Pandas DataFrame
print(brics.loc["BR"])  # Pandas DataFrame
# print(brics.loc[:, ["capital", "population"]]) is also possible
# print(brics.loc[:, "capital"]) prints as Pandas Series

print("\n2.b. Using iloc approach:")
print(brics.iloc[[0, 3], [1, 3]])
# print(brics.loc[:, [1, 3]]) is also possible

print("\n3. Logic operators:")
large_area = brics["area"] < 10
small_area = brics["area"] > 5
average_area = np.logical_and(small_area, large_area)  # others: logical_or, logical_not
print(brics[average_area].loc[:, ["country"]])

print("\n4.a. Loops:")
for label, row in brics.iterrows():
	print(label + ": " + row["country"])

print("\n4.b. Adding a new column:")
# for more efficincy, look for .apply() - pandas
for label, row in brics.iterrows():
	brics.loc[label, "pop_density"] = row["population"]/row["area"]
print(brics)
