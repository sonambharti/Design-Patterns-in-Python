#   Dependency Inversion Principle (DIP)
In object-oriented design, the dependency inversion principle is a specific methodology for loosely coupled software modules. When following this principle, the conventional dependency relationships established from high-level, policy-setting modules to low-level, dependency modules are reversed, thus rendering high-level modules independent of the low-level module implementation details.

## Introduction
Dependency Inversion Principle (DIP) states:
```
"High-level modules should not depend on low-level modules. Both should depend on abstractions."
"Abstractions should not depend on details. Details should depend on abstractions."
```
In simpler terms: <br>

-   High-level classes (e.g., business logic) should not be tightly coupled with low-level classes (e.g., data access). <br>
-   Both should communicate through an interface or abstract class.<br>

##  🧠 Understanding in Simple Terms:
-   A **high-level module** is your business logic – e.g., a class that processes user data or coordinates features.
-   A **low-level module** is a **detail implementation** – like database access, file reading, or data retrieval.
-   If a high-level module depends directly on a low-level one, then any change in the implementation can **break** or **require** change in your high-level logic. <br>
```
Instead of high-level depending directly on low-level, both should rely on an interface (abstraction) that defines how they communicate.
```

**Note:**
-   BAD CODE : A coffee machine (high-level) is directly wired to a specific brand of coffee beans (low-level).
-   GOOD CODE: The coffee machine uses a "BeanProvider" interface. Now you can plug in any brand that implements this interface.


##  🚫 Violation in Original Code
Problem: <br>
1.  Research is a high-level module, meant to perform business logic. <br>
2.  It directly depends on the low-level module Relationships, including its internal data structure (relations list). <br>
3.  This violates DIP because the high-level module is tightly coupled with implementation details of the low-level module. <br>


##  ✅ Refactored Design (DIP Compliant)
We introduce an abstraction (`RelationshipBrowser`) and let both the high-level and low-level modules depend on it, not on each other directly. <br>

Structure: <br>
-   `RelationshipBrowser`: Abstract base class (interface) <br>
-   `Relationships`: Low-level implementation that inherits `RelationshipBrowser` <br>
-   `Research`: High-level class that depends only on `RelationshipBrowser` <br>

### ✅ DIP-Compliant Refactoring:
1.  Create an interface (abstract class) that defines how relationships should be queried.
2.  Make the low-level class implement this interface.
3.  Let the high-level class depend only on the abstraction.
<br>
Now Research is: ✅ Decoupled from internal data <br>
✅ Easier to test   <br>
✅ Easier to change (e.g., switch to a DB backend) <br>
✅ Following the Dependency Inversion Principle <br>

##  ✅ Benefits of DIP:
-   Loosely coupled components
-   Easier testing (can mock the RelationshipBrowser)
-   Swappable backends (e.g., DB or in-memory)
-   Scalable and maintainable design

##  🔚 Conclusion
The Dependency Inversion Principle is all about decoupling high-level policies from low-level details using **abstractions**. <br>

By applying DIP: <br>
-   You write cleaner, modular code
-   Changes in data storage or format won’t affect your core logic
-   Your system becomes easier to extend, test, and maintain
<br>
Your example demonstrates DIP beautifully. By introducing an abstraction (`RelationshipBrowser`) between the `Research` (high-level logic) and `Relationships` (low-level data), the design becomes far more flexible and robust.