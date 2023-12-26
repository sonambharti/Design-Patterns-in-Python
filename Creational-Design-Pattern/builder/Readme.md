# Builder Design Pattern

The Builder Pattern is to separate the construction of a complex object from its representation so that you can use the same construction process to create different representations.
Terminology:
• Product: The Product being built.
• Builder Interface: The Interface that the Concrete builder should implement.
• Builder: Provides methods to build and retrieve the concrete product. Implements the Builder Interface.
• Director: Has a construct() method that when called creates a customized product using the methods of the Builder.

## Builder UML Diagram 
                ![Builder Design Pattern Diagram](<Builder Design Pattern.png>)
                
# Type of Houses Example to show Concept of Builder Design Pattern

## Output:
```
python3 ./builder/builder_concept.py
['a', 'b', 'c']
```


# Overview to run the code to design a House type and its prices
## Output:
```
python3 ./builder/client.py 
This is a Ice Igloo with 1 door(s) and 0 window(s).

The charges for Igloo is 4500 per room per night.

This is a Sandstone Castle with 100 door(s) and 200 window(s).

The charges for Castle is 5500 per room per night.

This is a Wood House Boat with 6 door(s) and 8 window(s).

The charges for House Boat is 7500 per room per night.
```
