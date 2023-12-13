"Abstract Factory Use Case Example Code"
from beverages_factory import BeveragesFactory


Beverages = BeveragesFactory.get_beverages("SmallColdDrink")
print(f"{Beverages.__class__} : {Beverages.get_volumes()}")

Beverages = BeveragesFactory.get_beverages("MediumJuice")
print(f"{Beverages.__class__} : {Beverages.get_volumes()}")