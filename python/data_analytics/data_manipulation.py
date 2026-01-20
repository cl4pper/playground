import pandas as pd
import os

BASE_DIR = os.getcwd()
csv_path = "/data_analytics/datasets/brics.csv"
brics = pd.read_csv(BASE_DIR + csv_path, index_col=0)
print(brics)
print(f"\nColumns: {brics.columns}")
print(f"\nValues:\n {brics.values}")
print(f"\n {brics.index}")

print(f"\nShape {brics.shape} and Describe - for quick overviews:\n {brics.describe()}")

print(f"\nHead:\n {brics.head()}")
print(f"\nInfo:\n {brics.info()}")
