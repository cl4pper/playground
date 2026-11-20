import requests
from request import Request


class Get(Request):
	"""Launch a GET request -> extends Request
	__init__
	domain(string): URL domain name

	__methods__
	private call_endpoint

	get_data: returns data in json format
	"""
	def __init__(self, domain: str) -> None:
		super().__init__(domain)

	def _call_endpoint(self):
		return requests.get(super().ENDPOINT)

	def get_data(self):
		print(f"Requesting from {super().ENDPOINT}")
		data = self._call_endpoint()
		return data.json()

# req = Get('https://jsonplaceholder.typicode.com/')
# req.set_path('posts')
