# pylint: disable=too-few-public-methods
"The Bottle Interface"
from abc import ABCMeta, abstractmethod


class IBottle(metaclass=ABCMeta):
    "The Bottle Interface (Product)"

    @staticmethod
    @abstractmethod
    def get_dimensions():
        "A static interface method"