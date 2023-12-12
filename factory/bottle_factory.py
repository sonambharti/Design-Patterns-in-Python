"The Factory Class"
from small_bottle import SmallBottle
from medium_bottle import MediumBottle
from large_bottle import LargeBottle


class BottleFactory:  # pylint: disable=too-few-public-methods
    "The Factory Class"

    @staticmethod
    def get_chair(bottle):
        "A static method to get a chair"
        if bottle == 'LargeBottle':
            return LargeBottle()
        if bottle == 'MediumBottle':
            return MediumBottle()
        if bottle == 'SmallBottle':
            return SmallBottle()
        return None