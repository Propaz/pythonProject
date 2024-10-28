from typing import List
from uuid import UUID

from db.sqlitedict import SqliteDict
from models.order import Order

db = SqliteDict('orders.db', autocommit=True)


def create_order(order: Order):
    db[order.key] = order


def read_order(key: UUID) -> Order:
    return db[key]


def read_all_orders() -> List[Order]:
    return list(db.values())


def update_order():
    pass


def delete_order():
    pass

def delete_all_orders():
    db.clear()
