# pylint: disable=too-few-public-methods
"Abstract Beverages Factory"
from interface_beverages_factory import IBeveragesFactory
from coldDrink_factory import ColdDrinkFactory
from juice_factory import JuiceFactory


class BeveragesFactory(IBeveragesFactory):
    "The Abstract Factory Concrete Class"

    @staticmethod
    def get_beverages(drink):
        "Static get_factory method"
        try:
            if drink in ['SmallColdDrink', 'MediumColdDrink', 'BigColdDrink']:
                return ColdDrinkFactory.get_coldDrinks(drink)
            if drink in ['SmallJuice', 'MediumJuice', 'BigJuice']:
                return JuiceFactory.get_juices(drink)
            raise Exception('No Factory Found')
        except Exception as _e:
            print(_e)
        return None
