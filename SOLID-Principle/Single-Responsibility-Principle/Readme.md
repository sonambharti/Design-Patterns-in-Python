# Single Responsibility Principle (SRP)

- This is also known as **SoC** (Seperation of Concerns).
- Each module or class should have only one reason to change.
- This means that a class should have only one job or responsibility.
- This principle is used to make the code more maintainable and easier to understand.
- It is also known as the **Single Job Principle**.
- It is introduced by **Robert C. Martin**.


**Note:**
-   BAD CODE : All the functionality like add_entry() , remove_entry() , save(), load(), load_from_web() are present in same file.
-   GOOD CODE: Seperate file for each functionality.

##  Issues with The Bad Code
-   Journal class has multiple responsibilities: <br>
    i.  Managing journal entries (`add_entry`, `remove_entry`) <br>
    ii. Handling file operations (`save`, `load`, `load_from_web`) <br>
-   Why is this a problem?
    i.  If file handling changes (e.g., using a database instead of a file), we would need to modify the `Journal` class.
    ii. It violates the principle that a class should have only one reason to change.

## Applying the Single Responsibility Principle in Good Code
-   To follow SRP, we separate concerns by creating a new class for persistence.


## Benefits of SRP

1. **Improved Maintainability**: Changes to journal entries do not affect file operations and vice versa.
2. **Better Readability**: Each class has a clear and specific responsibility.
3. **Easy Testing**: Journal logic can be tested separately from file operations.
4. **Flexible Design**: If persistence changes (e.g., saving to a database instead of a file), we only modify `PersistenceManager` without affecting `Journal`.

##  Conclusion
By following SRP, we ensure that: <br>
    -   Journal handles only journal-related operation <br>
    -   PersistenceManager is responsible for file operations. <br>

This approach makes our code cleaner, more modular, and easier to manage in the long run.