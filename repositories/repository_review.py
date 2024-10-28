from typing import List
from uuid import UUID

from db.sqlitedict import SqliteDict
from models.order_review import OrderReview

db = SqliteDict('review.db', autocommit=True)


def create_review(review: OrderReview):
    db[review.order_key] = review


def read_review(order_key: UUID) -> OrderReview:
    return db[order_key]


def read_all_reviews() -> List[OrderReview]:
    return list(db.values())


def update_review():
    pass


def delete_review():
    pass


def delete_all_reviews():
    db.clear()
