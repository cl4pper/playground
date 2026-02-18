import pandas as pd
import os

BASE_DIR = os.getcwd()
csv_path = "/datasets/brics.csv"
brics = pd.read_csv(BASE_DIR + csv_path, index_col=0)

print(brics)
print(f"\nColumns: {brics.columns}")
print(f"\nValues:\n {brics.values}")
print(f"\n {brics.index}")

print(f"\nShape {brics.shape} and Describe - for quick overviews:\n {brics.describe()}")

print(f"\nHead:\n {brics.head()}")
print(f"\nInfo:\n {brics.info()}")

# Sorting and subsetting
print(f"\nSorting by area(largest on):\n{brics.sort_values(['area'], ascending=[False])}")
print(f"\nSubsetting columns:\n{brics[['area', 'population']]}")
print(f"\nSubsetting rows - all rows:\n{brics[['area']] > 8}")
print(f"\nSubsetting rows - by conditional:\n{brics[brics['area'] > 8]}")
print(f"\nSubsetting by .isin():\n{brics[brics['country'].isin(['China', 'Russia'])]}")

# Adding new columns
brics["pop/area"] = round(brics["population"]/brics["area"], 2)
print(f"\nAdding a new column pop/area:\n {brics}")
