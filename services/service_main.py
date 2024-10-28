from dataclasses import dataclass

from models.order import Order
from models.order_review import OrderReview
from services import service_orders, service_reviewes


@dataclass
class AccReview:
    order: Order
    order_review: OrderReview


def get_all_essences():
    all_orders = service_orders.read_all_orders_by_filter("Apple")
    all_orders_keys = [order.key for order in all_orders]

    all_reviews = service_reviewes.read_all_reviews_by_order_keys(all_orders_keys)

    return [AccReview(order=o,order_review=r) for o in all_orders for r in all_reviews]
