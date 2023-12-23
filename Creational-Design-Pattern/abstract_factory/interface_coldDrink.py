# pylint: disable=too-few-public-methods
"The Cold Drink Interface"
from abc import ABCMeta, abstractmethod


class IColdDrink(metaclass=ABCMeta):
    "The Cold Drink Interface (Product)"

    @staticmethod
    @abstractmethod
    def get_volumes():
        "A static interface method"