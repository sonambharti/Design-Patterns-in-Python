# Decorator Design Pattern

The decorator pattern adds extensibility without modifying the original object.
The decorator forwards requests to the enclosed object and can perform extra actions.

Terminology:
i.    Component: The object that may be decorated.
ii.   Component Interface: An interface for objects.
iii.  Decorator: The class that applies the extra responsibilities to the component being decorated. It also implements the same component interface.

## Decorator UML Diagram 
                ![Decorator Design Pattern](decorator.png)

                
                
# Example to show Concept of Decorator Design Pattern

## Output:
```
python3 ./decorator/decorator_concept.py
Component Method
Decorator Method(Component Method)
```


# Overview to run the code to design a Decorator Use Case
## Output:
```
python3 ./decorator/client.py 
22
110
44
56
-1
156
15
154
10
12
54
```

