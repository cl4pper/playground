import json
import os

BASE_DIR = os.getcwd()

with open(BASE_DIR + '/file_reader/data.json', 'r') as file:
	data = json.load(file)

print(data)
