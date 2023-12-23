# pylint: disable=too-few-public-methods
"A Class of Bottle"
from interface_bottle import IBottle


class LargeBottle(IBottle):
    "The Large Bottle Concrete Class implements the IBottle interface"

    def __init__(self):
        self._height = 80
        self._radius = 8
        

    def get_dimensions(self):
        return {
            "radius": self._radius,
            "height": self._height
        }