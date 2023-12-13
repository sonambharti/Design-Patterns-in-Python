"The Factory Class"
from small_ColdDrink import SmallColdDrink
from medium_ColdDrink import MediumColdDrink
from large_ColdDrink import LargeColdDrink


class ColdDrinkFactory:  # pylint: disable=too-few-public-methods
    "The Factory Class"

    @staticmethod
    def get_volumes(coldDrink):
        "A static method to get a chair"
        try:
            if coldDrink == 'LargeColdDrink':
                return LargeColdDrink()
            if coldDrink == 'MediumColdDrink':
                return MediumColdDrink()
            if coldDrink == 'SmallColdDrink':
                return SmallColdDrink()
            raise Exception('Cold Drink size Not Found')
        except Exception as _e:
            print(_e)
        return None