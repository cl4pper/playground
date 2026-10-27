import json


class Reader:
	"""
		Reader:
		Reads file content and return a dict

		read_json: reads a json file and returns a dict
	"""
	def __init__(self, file: str, type: str) -> None:
		self.file = file

	def read_json(self):
		with open(self.file, 'r') as file:
			return json.load(file)
