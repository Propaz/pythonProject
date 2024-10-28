from dataclasses import dataclass

from models.package import Package


@dataclass
class Order:
    key: str
    name: str
    description: str
    color: int
    package: Package
