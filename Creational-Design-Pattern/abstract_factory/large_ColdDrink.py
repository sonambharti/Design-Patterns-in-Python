"A Class of ColdDrink"
from interface_coldDrink import IColdDrink
import math


class LargeColdDrink(IColdDrink):  # pylint: disable=too-few-public-methods
    "The Large ColdDrink Concrete Class implements the IColdDrink interface"

    def __init__(self):
        self._height = 60
        self._radius = 6
       
    def get_volumes(self):
        print("\nLarge size Cold Drink.\n")
        volume = math.pi * (self._radius**2) * self._height
        price = 15 * volume
        return {
            "radius": self._radius,
            "height": self._height,
            "volume": volume,
            "price": price
        }