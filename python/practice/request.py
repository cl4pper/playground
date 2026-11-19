class Request:
	"""Base class to setup a request

	__init__
	domain(string): URL domain name

	__methods__
	set_path: append path to the URL
	:pathname: string

	review_url: return URL in parts

	(?) compose_url: initiate URL as a whole
	"""
	ENDPOINT: str

	def __init__(self, domain: str) -> None:
		self.domain = domain
		Request.ENDPOINT = domain

	def set_path(self, pathname: str) -> None:
		self.pathname = pathname
		Request.ENDPOINT = self.domain + pathname

	@classmethod
	def compose_url(cls, url: str):
		Request.ENDPOINT = url
		cls(url)

	def review_url(self) -> str:
		return f"URL: {Request.ENDPOINT}\ndomain: {self.domain}\npathname: {self.pathname}"

# placeholder = Request('https://jsonplaceholder.typicode.com/')
