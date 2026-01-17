import numpy as np

# Initialize
country_names = ['Brazil', 'Germany', 'Russia']
coordinates = [[41.56, 40.48], [36.50, 41.37]]

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
