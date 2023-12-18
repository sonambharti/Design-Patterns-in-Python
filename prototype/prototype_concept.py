"""
The Prototype pattern delegates the cloning process to the actual objects that are being cloned. The pattern declares a common interface for all objects that support cloning. This interface lets you clone an object without coupling your code to the class of that object. Usually, such an interface contains just a single clone method.

clone method can be implemented using 2 methods:
• A shallow copy, copies and creates new references one level deep, 
• A deep copy, copies and creates new references for all levels.

A shallow copy, will create new copies of the objects with new references in memory, but the underlying data, e.g., the actual elements in a list, will point to the same memory location as the original list/object being copied. You will now have two lists, but the elements within the lists will point to the same memory location. So, changing any elements of a copied list will also affect the original list.

Note: Shallow copies are much faster to process than deep copies and deep copies are not always necessary if you are not going to benefit from using it.

doc: https://docs.python.org/3/library/copy.html

"""

# pylint: disable=too-few-public-methods
# pylint: disable=arguments-differ
"Prototype Concept Sample Code"
from abc import ABCMeta, abstractmethod
import copy

class IProtoType(metaclass=ABCMeta):
    "interface with clone method"
    @staticmethod
    @abstractmethod
    def clone():
        """The clone, deep or shallow.
        It is up to you how you want to implement
        the details in your concrete class"""


class MyClass(IProtoType):
    "A Concrete Class"

    def __init__(self, field):
        self.field = field  # any value of any type

    def clone(self):
        " This clone method uses a shallow copy technique "
        return type(self)(
            self.field  # a shallow copy is returned
            # self.field.copy() # this is also a shallow copy, but has
            # also shallow copied the first level of the field. So it
            # is essentially a shallow copy but 2 levels deep. To
            # recursively deep copy collections containing inner
            # collections,
            # eg lists of lists,
            # Use https://docs.python.org/3/library/copy.html instead.
            # See example below.
        )

    def __str__(self):
        return f"{id(self)}\tfield={self.field}\ttype={type(self.field)}"


# The Client
OBJECT1 = MyClass([1, 2, 3, 4])  # Create the object containing a list
print(f"OBJECT1 {OBJECT1}")

OBJECT2 = OBJECT1.clone(1)  # Clone

# Change the value of one of the list elements in OBJECT2,
# to see if it also modifies the list element in OBJECT1.
# If it changed OBJECT1s copy also, then the clone was done
# using a 1 level shallow copy process.
# Modify the clone method above to try a 2 level shallow copy instead
# and compare the output
OBJECT2.field[1] = 101

OBJECT3 = OBJECT1.clone(2) 
# OBJECT3 = copy.deepcopy(OBJECT1)
OBJECT3.field[0] = 200

# Comparing OBJECT1 and OBJECT2
print(f"OBJECT2 {OBJECT2}")
print(f"OBJECT1 {OBJECT1}")
print(f"OBJECT3 {OBJECT3}")
print(f"OBJECT1 {OBJECT1}")