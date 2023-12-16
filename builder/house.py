"The Product"


class House():  # pylint: disable=too-few-public-methods
    "The Product"

    def __init__(self, building_type="Apartment", doors=0,
                 windows=0, wall_material="Brick"):
        # brick, wood, straw, ice
        self.wall_material = wall_material
        # Apartment, Bungalow, Caravan, Hut, Castle, Duplex,
        # HouseBoat, Igloo
        self.building_type = building_type
        self.doors = doors
        self.windows = windows

    def construction(self):
        "Returns a string describing the construction"
        print(f"\nThis is a {self.wall_material} "\
            f"{self.building_type} with {self.doors} "\
            f"door(s) and {self.windows} window(s).\n")
        price = 0
        if(self.building_type == "Igloo"):
            price = 4500
        elif(self.building_type == "Castle"):
            price = 5500
        if(self.building_type == "House Boat"):
            price = 7500
        return f"The charges for {self.building_type} is {price} per room per night."
