"Factory Design Pattern Client Code"

from bottle_factory import BottleFactory

# The Client
BOTTLE = BottleFactory.get_chair("SmallBottle")
print(BOTTLE.get_dimensions())