import unittest

from request import Request

DOMAIN = "https://jsonplaceholder.typicode.com/"


class RequestTest(unittest.TestCase):
	def setUp(self) -> None:
		# ENDPOINT is shared class state, so reset it between tests
		Request.ENDPOINT = ""

	def test_init_sets_domain_and_endpoint(self) -> None:
		request = Request(DOMAIN)

		self.assertEqual(request.domain, DOMAIN)
		self.assertEqual(Request.ENDPOINT, DOMAIN)

	def test_set_path_appends_path_to_domain(self) -> None:
		request = Request(DOMAIN)
		request.set_path("posts")

		self.assertEqual(request.pathname, "posts")
		self.assertEqual(Request.ENDPOINT, DOMAIN + "posts")

	def test_set_path_replaces_previous_path(self) -> None:
		request = Request(DOMAIN)
		request.set_path("posts")
		request.set_path("users")

		self.assertEqual(request.pathname, "users")
		self.assertEqual(Request.ENDPOINT, DOMAIN + "users")

	def test_review_url_shows_url_domain_and_pathname(self) -> None:
		request = Request(DOMAIN)
		request.set_path("posts")

		self.assertEqual(
			request.review_url(),
			f"URL: {DOMAIN}posts\ndomain: {DOMAIN}\npathname: posts",
		)

	def test_review_url_before_set_path_raises(self) -> None:
		request = Request(DOMAIN)

		with self.assertRaises(AttributeError):
			request.review_url()

	def test_compose_url_sets_endpoint(self) -> None:
		url = DOMAIN + "comments"
		Request.compose_url(url)

		self.assertEqual(Request.ENDPOINT, url)

	def test_endpoint_is_shared_between_instances(self) -> None:
		first = Request(DOMAIN)
		Request("https://example.com/")

		first.set_path("posts")
		self.assertEqual(Request.ENDPOINT, DOMAIN + "posts")
		self.assertEqual(first.ENDPOINT, Request.ENDPOINT)


if __name__ == "__main__":
	unittest.main()
