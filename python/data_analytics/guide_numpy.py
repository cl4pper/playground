import numpy as np

# Initialize
country_names = ['Brazil', 'Germany', 'Russia']
coordinates = [[41.56, 40.48], [36.51, 41.37]]

# Get dimension & shape
class ArrayElement:
	def __init__(self, name, array) -> None:
		self.name = name
		self.array = np.array(array)

	def get_self(self):
		return self.array

	def get_length(self) -> int:
		return len(self.array)

	def get_dimension(self) -> int:
		return self.array.ndim

	def get_shape(self) -> int:
		return self.array.shape

	def get_type(self):
		return self.array.dtype

	def get_item_size(self):
		return self.array.itemsize

	def get_total_size(self):
		return self.array.nbytes

	def get_config(self):
		return {
			"name": self.name,
			"type": self.get_type(),
			"length": self.get_length(),
			"item_size": self.get_item_size(),
			"total_size": self.get_total_size(),
			"dimension": self.get_dimension(),
			"shape": self.get_shape()
		}

array_country_names = ArrayElement('country_names', country_names)
print(array_country_names.get_config())
array_coodinates = ArrayElement('coordinates', coordinates)
print(array_coodinates.get_config())

# Accessing rows, columns, etc
# arr[row, column]
array_int = [1,2,3,4,5,6,7,8,9]
print(f"first row from coordinates {array_coodinates.get_self()[0, :]}")
print(f"first column from coordinates {array_coodinates.get_self()[:, 0]}")
# array[2, 2:8:2] -> get elements on row 2, from the element 2 until element 8, stepping by 2
