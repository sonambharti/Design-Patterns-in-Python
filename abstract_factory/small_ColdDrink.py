"A Class of ColdDrink"
from interface_coldDrink import IColdDrink
import math


class SmallColdDrink(IColdDrink):  # pylint: disable=too-few-public-methods
    "The Small ColdDrink Concrete Class implements the IColdDrink interface"

    def __init__(self):
        self._height = 40
        self._radius = 4
       
    def get_volumes(self):
        print("\nSmall size Cold Drink.\n")
        volume = math.pi * (self._radius**2) * self._height
        price = 15 * volume
        return {
            "radius": self._radius,
            "height": self._height,
            "volume": volume,
            "price": price
        }