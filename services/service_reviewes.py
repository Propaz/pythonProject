from typing import List, Set
from uuid import UUID

from models.order_review import OrderReview
from repositories import repository_review


def create_review(review: OrderReview):
    repository_review.create_review(review)


def read_review(order_key: UUID) -> OrderReview:
    return repository_review.read_review(order_key)


def read_review_by_user(user_key: UUID) -> List[OrderReview]:
    all_reviews = repository_review.read_all_reviews()
    return [review for review in all_reviews if review.user_key == user_key]


def read_all_reviews_by_order_keys(orders_keys: List[str]):
    all_reviews = repository_review.read_all_reviews()
    return [review for review in all_reviews if review.order_key in set(orders_keys)]


def update_review():
    repository_review.update_review()


def delete_review(key: UUID):
    repository_review.delete_review()


def delete_all_reviews():
    repository_review.delete_all_reviews()
