"The Factory Class"
from small_Juice import SmallJuice
from medium_Juice import MediumJuice
from large_Juice import LargeJuice


class JuiceFactory:  # pylint: disable=too-few-public-methods
    "The Factory Class"

    @staticmethod
    def get_volumes(Juice):
        "A static method to get a chair"
        try:
            if Juice == 'LargeJuice':
                return LargeJuice()
            if Juice == 'MediumJuice':
                return MediumJuice()
            if Juice == 'SmallJuice':
                return SmallJuice()
            raise Exception('Juice size Not Found')
        except Exception as _e:
            print(_e)
        return None