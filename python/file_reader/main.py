import json

from utils.constants import DATA_DIR
from utils.types import PayloadT

with open(DATA_DIR, 'r') as file:
	data: PayloadT = json.load(file)

for post in data['posts']:
	print(post['id'])
