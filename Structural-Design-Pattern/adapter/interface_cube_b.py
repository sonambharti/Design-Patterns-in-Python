# pylint: disable=too-few-public-methods
"An interface to implement"
from abc import ABCMeta, abstractmethod


class ICubeB(metaclass=ABCMeta):
    "An interface for an object"
    @staticmethod
    @abstractmethod
    def create(width, height, depth):
        "Manufactures a Cube with coords offset [0, 0, 0]"
