# pylint: disable=too-few-public-methods
"The Juice Interface"
from abc import ABCMeta, abstractmethod


class IJuice(metaclass=ABCMeta):
    "The Juice Interface (Product)"

    @staticmethod
    @abstractmethod
    def get_volumes():
        "A static interface method"