from dataclasses import dataclass


@dataclass
class OrderReview:
    key: str
    comment: str
    rating: int
    order_key: str
    user_key: str
