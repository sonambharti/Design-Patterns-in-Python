# Liskov Substitution Principle (LSP)
The Liskov Substitution Principle (LSP) states that subtypes should be substitutable for their base types. In other words, any code that uses a base type should be able to work with a subtype without knowing the difference. <br>
-   It is introduced by **Barbara Liskov** in **1987**. <br>
-   It is a fundamental principle of object-oriented programming (OOP) and is used to ensure that subtypes behave in a way that is consistent with their base types. <br>

##  Introduction

The Liskov Substitution Principle (LSP) is one of the five SOLID principles of object-oriented design. It states:
```
"Objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program."
```
This means that a subclass should extend the behavior of its superclass without altering its expected behavior. <br>


**Note:**
-   BAD CODE : Objects of superclass is replaceable eith the object of subclass but at the same time it affects the correctness of the program.
-   GOOD CODE: Seperate classes for each functionality that can impact superclass and subclass.

##  🚫 Problem: Violation of LSP

We create a Square class as a subclass of Rectangle, assuming "a square is-a rectangle". However, the Square class overrides the width and height setters in a way that breaks the expected behavior.

##  🔍 Why This Violates LSP
-   Square inherits from Rectangle but changes behavior of the width and height setters.<br>
-   use_it() assumes changing height does not affect width, which is true for rectangles but not for squares.<br>
-   This breaks substitutability, which violates LSP.<br>

In short,  Issues with This Code are:
We have created a Square class as a subclass of Rectangle, assuming "a square is-a rectangle". However, the Square class overrides the width and height setters in a way that breaks the expected behavior. <br>

1. **Violation of LSP**: Square overrides width and height setters incorrectly, which causes an unexpected side effect when modifying dimensions. <br>
2. **Unexpected Behavior**: The use_it() function expects the behavior of a Rectangle, but modifying height of Square changes width too. <br>
3. **Breaking Substitution**: Square cannot be reliably used in place of Rectangle without unexpected results. <br>

##   Applying the Liskov Substitution Principle
-   To follow LSP, we need to ensure that subclasses do not alter the behavior of their superclass. Instead of making Square inherit from Rectangle, we should refactor the design to avoid inheritance where it does not make sense. <br>
-   Use composition over inheritance when necessary. <br>

###  Benefits of The Refactored Approach

1.  No Unexpected Side Effects: Square no longer inherits from Rectangle, preventing modification conflicts. <br>
2.  Proper Substitution: Rectangle and Square can now be used interchangeably without breaking expectations. <br>
3.  Better Abstraction: Using a common base class (Shape) ensures that all shapes adhere to a common contract (area property). <br>

##  Conclusion

By following the Liskov Substitution Principle, we ensure that:
-   Subclasses behave as expected when used in place of their parent classes. <br>
-   Inheritance is only used where it makes logical sense. <br>
-   Code remains predictable, maintainable, and extensible. <br>

This approach leads to better software design, reducing unintended side effects and ensuring the correctness of our program.

