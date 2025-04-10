# Interface Segregation Principle (ISP)
The ISP states that a client should not be forced to depend on interfaces that it does not use.

## Introduction
Interface Segregation Principle (ISP) states:
```
"Clients should not be forced to depend on methods they do not use."
```

In simpler terms: Rather than having one large interface, it's better to have multiple smaller, specific interfaces so that classes only need to implement methods they actually use.


**Note:**
-   BAD CODE : Only one class have all the `abstract methods /interfaces` which can raise issue.
-   GOOD CODE: Seperate `classes / interfaces` for each functionality that can impact subclass.


##  🚫 Problem: Violating ISP
Any subclass of Machine is forced to implement all three methods, even if it only needs one. <br>
Here, OldFashionedPrinter is forced to implement scan() and fax() even though it only supports printing. This is a clear violation of ISP.


##  ✅ Refactored: Applying ISP
Instead of one large interface, we split responsibilities into smaller, specific interfaces. <br>
Small Interfaces like Printer and Scanners. Then, classes can implement only the interfaces they need, like 

### Use Composition Over Inheritance:
Instead of creating a big class implementing everything, use composition like we did in `MultiFunctionMachine`




## Conclusion
Large interfaces cause code to become brittle and confusing. ISP promotes more modular, maintainable, and testable designs by ensuring that classes only implement the behavior they actually need. <br>

Let me know if you'd like this as a markdown file or visual diagram too!