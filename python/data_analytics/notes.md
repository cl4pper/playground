# Guide

## Logic, Control and Filtering

### Comparison operators
| Operators  | Conditionals       |
| ---------- | ------------------ |
| >          | if `conditional`:  |
| <          | elif `conditional`:|
| >=         | else               |
| >=         |
| ==         |
| !=         |

### Boolean operators
| Operators   | Example          | Results     |
| ----------- | ---------------- | ----------- |
| and         | True and False   | False       |
| or          | True or False    | True        |
| not         | not False        | True        |

## Loops

### while
```
while condition:
  expression
```

### for
```
# example 1
for values in array:
  expression
```

```
# example 2
# enumerate is a built-in method which returns a tuple containing
# the index and the values from the iterable

for index, value in enumerate(array):
  expression
```

```
# example with numpy
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.array([a, b])

for value in c:
  print(value) # output: [1,2,3][4,5,6]

for value in np.nditer(c):
  print(value) # output: 1,2,3,4,5,6
```

```
# example with dictionary
# the order of interations is not fixed

for key, value in dictionary.items():
  expression
```
