import numpy as np

"""
Boolean operators:

| Operators   | Example          | Results     |
| ----------- | ---------------- | ----------- |
| and         | True and False   | False       |
| or          | True or False    | True        |
| not         | not False        | True        |
"""

wages = np.array([10000, 5000, 7000, 4500, 9200, 8100, 2300, 1800, 3500, 3800])

high_ref = 7000
low_ref = 3000

high_wages = wages > high_ref
low_wages = wages < low_ref
medium_wages = np.logical_and(wages >= low_ref, wages <= high_ref)
# others: logical_or, logical_not

print(f"high wages: {wages[high_wages]}")
print(f"low wages: {wages[low_wages]}")
print(f"medium wages: {wages[medium_wages]}")
