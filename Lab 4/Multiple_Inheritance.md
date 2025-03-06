# Multiple Inheritance in Python

**Multiple Inheritance** is a feature in Python where a class can inherit attributes and methods from more than one parent class. This allows for greater flexibility and code reuse but can also introduce complexity, especially when dealing with method conflicts.

---

## Key Concepts

1. **Syntax**:
   ```python
   class Parent1:
       pass

   class Parent2:
       pass

   class Child(Parent1, Parent2):  # Inherits from both Parent1 and Parent2
       pass
   ```

2. **Method Resolution Order (MRO)**:
   - MRO determines the order in which Python searches for methods and attributes in a class hierarchy.
   - Python uses the **C3 Linearization algorithm** to compute the MRO.
   - You can view the MRO of a class using the `__mro__` attribute or the `mro()` method.

   Example:
   ```python
   class A:
       pass

   class B(A):
       pass

   class C(A):
       pass

   class D(B, C):
       pass

   print(D.__mro__)
   # Output: (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
   ```

3. **Diamond Problem**:
   - A common issue in multiple inheritance where a class inherits from two classes that both inherit from a common base class.
   - Python resolves this using MRO, ensuring each class is only visited once.

   Example:
   ```python
   class A:
       def greet(self):
           print("Hello from A")

   class B(A):
       def greet(self):
           print("Hello from B")

   class C(A):
       def greet(self):
           print("Hello from C")

   class D(B, C):
       pass

   d = D()
   d.greet()  # Output: Hello from B (follows MRO: D -> B -> C -> A)
   ```

---

## Advantages of Multiple Inheritance

1. **Code Reuse**:
   - Allows combining functionality from multiple classes.
2. **Flexibility**:
   - Enables modeling complex relationships between classes.
3. **Mixins**:
   - Small classes (mixins) can be used to add specific behaviors to multiple classes.

---

## Disadvantages of Multiple Inheritance

1. **Complexity**:
   - Can make the code harder to understand and maintain.
2. **Name Conflicts**:
   - If two parent classes have methods or attributes with the same name, conflicts can arise.
3. **Tight Coupling**:
   - Overuse can lead to tightly coupled code, making it harder to modify.

---

## Best Practices

1. **Use Mixins**:
   - Use small, focused classes (mixins) to add specific behaviors.
2. **Avoid Deep Hierarchies**:
   - Keep inheritance hierarchies shallow to reduce complexity.
3. **Favor Composition Over Inheritance**:
   - Use composition (e.g., including objects as attributes) when multiple inheritance introduces too much complexity.

---

## Example of Multiple Inheritance

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Flyable:
    def fly(self):
        print("Flying")

class Bird(Animal, Flyable):  # Inherits from both Animal and Flyable
    pass

bird = Bird()
bird.speak()  # Output: Animal speaks
bird.fly()    # Output: Flying
```

---

## Summary of MRO

- **MRO** determines the order in which Python searches for methods and attributes in a class hierarchy.
- It follows the **C3 Linearization algorithm**.
- Use `__mro__` or `mro()` to inspect the MRO of a class.
- MRO ensures that each class in the hierarchy is visited only once, resolving conflicts in multiple inheritance.

---