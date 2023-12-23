# pylint: disable=too-few-public-methods
"The Abstract Factory Interface"
from abc import ABCMeta, abstractmethod


class IBeveragesFactory(metaclass=ABCMeta):
    "Abstract Beverages Factory Interface"

    @staticmethod
    @abstractmethod
    def get_beverages(beverage):
        "The static Abstract factory interface method"