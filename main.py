from uuid import uuid4

from models.order import Order
from models.order_review import OrderReview
from models.package import Package
from models.user import User
from services import service_orders, service_reviewes, service_main

if __name__ == "__main__":
    service_reviewes.delete_all_reviews()
    service_orders.delete_all_orders()

    order_key = str(uuid4())
    user_key = str(uuid4())

    user = User(
        name="Vasyan",
        user_key=user_key
    )

    order = Order(
        name="Apple",
        key=order_key,
        description="best apple",
        package=Package.SOFT,
        color=1
    )
    service_orders.create_order(order)
    review = OrderReview(
        key=str(uuid4()),
        comment="test comment",
        rating=3,
        order_key=order_key,
        user_key=user_key
    )
    service_reviewes.create_review(review)

    a = service_reviewes.read_review(order_key)
    print(a)
    b = service_orders.read_order(order_key)
    print(b)

    c = service_orders.read_all_orders_by_filter("asdasddas")
    print(c)
    c1 = service_orders.read_all_orders_by_filter("Apple")
    print(c1)

    c3 = service_reviewes.read_review_by_user(user_key)
    print(c3)

    k = service_main.get_all_essences()
    print(k)

    x = service_orders.read_order(str(uuid4()))
