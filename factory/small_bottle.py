# pylint: disable=too-few-public-methods
"A Class of Bottle"
from interface_bottle import IBottle


class SmallBottle(IBottle):
    "The small bottle Concrete Class implements the IBottle interface"

    def __init__(self):
        self._height = 50
        self._radius = 5
        

    def get_dimensions(self):
        return {
            "radius": self._radius,
            "height": self._height
        }