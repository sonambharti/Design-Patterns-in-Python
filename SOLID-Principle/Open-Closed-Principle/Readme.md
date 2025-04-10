# Open - Closed Principle (OCP)

-   The Open-Closed Principle states that a class should be open for extension but closed for modification. <br>
-   It is introduced by **Bertrand Meyer**. 

##  Introduction

The Open-Closed Principle (OCP) is one of the five SOLID principles of object-oriented design. It states:
<br>
````
"Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification."
````
<br>
This means that we should be able to add new functionality without modifying existing code, which helps in maintaining and scaling software.
<br>
There are few points to OCP: <br>
-   This principle is useful when you want to add new functionality to a class without changing its existing code. <br>
-   To achieve this, you can use inheritance and polymorphism. For example, you can create a new class that inherits from the existing class and overrides its methods to add new functionality. <br>

**Note:**
-   BAD CODE : All the functionality like filter_by_color() , filter_by_size() ,filter_by_size_and_color() are fixed for fixed number of features like size and color.
-   GOOD CODE: Seperate classes for defining each functionality so that open for adding new functionality without any changes or modifications in existing code.

##  Issues with This Code

-   **Violation of OCP**: Every time we need a new filter criterion, we must modify `ProductFilter` by adding a new method. <br>
-   **Scalability Issues**: If we introduce more criteria (e.g., weight, price), the number of filtering methods grows exponentially, leading to a "state space explosion." <br>


##  Applying the Open-Closed Principle
-   To follow OCP, we introduce an abstraction: Specification Pattern. We create separate specification classes for each filtering criterion and make the filter class work with any specification.

##  Combining Specifications
-   To filter by multiple criteria, we introduce the `AndSpecification` class...

##  Benefits of OCP

1.  **Extensibility**: New filter criteria can be added without modifying existing classes. <br>
2.  **Code Reusability**: Specifications can be reused across different filtering operations. <br>
3.  **Scalability**: The approach avoids the exponential growth of filtering methods. <br>
4.  **Maintainability**: The code remains cleaner and easier to understand.

##  Conclusion

By following the Open-Closed Principle, we ensure that: <br>

-   ProductFilter is open for extension (new specifications can be added). <Br>
-   ProductFilter is closed for modification (existing code remains unchanged). <br>

This approach leads to better software design, making it more adaptable and future-proof.