
from typing import TypedDict


class PostT(TypedDict):
	id: int
	userId: int
	title: str
	body: str

class PayloadT(TypedDict):
	posts: list[PostT]
