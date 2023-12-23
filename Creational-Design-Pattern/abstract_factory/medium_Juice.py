"A Class of Juice"
from interface_juice import IJuice
import math


class MediumJuice(IJuice):  # pylint: disable=too-few-public-methods
    "The Medium Juice Concrete Class implements the IJuice interface"

    def __init__(self):
        self._height = 50
        self._radius = 5
       
    def get_volumes(self):
        print("\nMedium size Juice.\n")
        volume = math.pi * (self._radius**2) * self._height
        price = 20 * volume
        return {
            "radius": self._radius,
            "height": self._height,
            "volume": volume,
            "price": price
        }