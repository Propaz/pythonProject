from typing import List
from uuid import UUID

from models.order import Order
from models.package import Package
from repositories import repository_orders


def create_order(order: Order):
    repository_orders.create_order(order)


def read_order(key: UUID) -> Order:
    return repository_orders.read_order(key)


def read_all_orders_by_package(package: Package):
    all_orders = repository_orders.read_all_orders()
    return [order for order in all_orders if order.package == package]


def read_all_orders_by_keys(keys: List[UUID]) -> List[Order]:
    all_orders = repository_orders.read_all_orders()
    return [order for order in all_orders if order.key in keys]


def read_all_orders_by_filter(orders_filter_by_name: str) -> List[Order]:
    all_order = repository_orders.read_all_orders()
    return [
        order for order in all_order if orders_filter_by_name in order.name
    ]


def update_order():
    repository_orders.update_order()


def delete_all_orders():
    repository_orders.delete_all_orders()


def delete_order(key: UUID):
    repository_orders.delete_order()
