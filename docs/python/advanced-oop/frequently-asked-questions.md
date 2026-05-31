# Python Advanced OOP: Frequently Asked Interview Questions

## Basic Level

### 1. What is MRO?

MRO stands for Method Resolution Order. It is the order Python uses to find methods in an inheritance hierarchy.

### 2. How do you view MRO?

```python
print(ClassName.mro())
```

### 3. What is the diamond problem?

It happens when a class inherits from multiple classes that share the same parent.

### 4. How does Python handle the diamond problem?

Python uses MRO to choose a consistent method lookup order.

### 5. What is a mixin?

A mixin is a small class that adds reusable behavior to other classes.

### 6. Should mixins be used alone?

Usually no. Mixins are normally meant to add behavior to another class.

### 7. What is a nested class?

A nested class is a class defined inside another class.

### 8. What are dynamic attributes?

Dynamic attributes are attributes added to an object at runtime.

### 9. What is introspection?

Introspection means inspecting objects, classes, and attributes at runtime.

### 10. What does `type()` do?

`type()` returns the exact type of an object.

## Intermediate Level

### 11. What does `isinstance()` do?

It checks whether an object is an instance of a class or subclass.

### 12. What does `issubclass()` do?

It checks whether one class is a subclass of another class.

### 13. What is the difference between `type()` and `isinstance()`?

`type()` checks exact type. `isinstance()` respects inheritance.

### 14. Why is `isinstance()` often preferred?

It works with subclasses and polymorphism.

### 15. What is `dir()`?

`dir()` lists many attributes and methods available on an object.

### 16. What is `__dict__`?

`__dict__` stores an object's writable attributes in many normal Python classes.

### 17. What does `getattr()` do?

It reads an attribute by name and can provide a default.

### 18. What does `setattr()` do?

It sets an attribute by name.

### 19. What does `hasattr()` do?

It checks whether an object has an attribute.

### 20. Why can dynamic attributes be risky?

They can make object shape unpredictable and harder to debug.

## Advanced Level

### 21. What algorithm does Python use for MRO?

Python uses C3 linearization.

### 22. What is cooperative multiple inheritance?

It is a design where classes use `super()` consistently so calls follow MRO correctly.

### 23. Why can calling parent class names directly be risky?

It can bypass MRO and break multiple-inheritance cooperation.

### 24. What makes a good mixin?

A good mixin is small, focused, reusable, and does not require too much hidden state.

### 25. What is a bad mixin design?

A mixin that depends on many undocumented attributes or mixes unrelated behavior.

### 26. When should you use nested classes?

Use them when the inner class is tightly scoped to the outer class, such as `Order.Status`.

### 27. When should you avoid nested classes?

Avoid them when the inner class is important enough to be reused independently.

### 28. How does introspection help debugging?

It reveals object type, available attributes, class relationships, and runtime state.

### 29. What is a common advanced OOP interview trap?

Assuming `super()` always means "immediate parent"; it actually follows MRO.

### 30. What should you remember?

Understand MRO, use mixins carefully, avoid overusing dynamic attributes, and prefer `isinstance()` for inheritance-aware checks.

## Final Interview Checklist

- MRO controls method lookup.
- Diamond problem is resolved by MRO.
- `super()` follows MRO.
- Mixins add small reusable behavior.
- Nested classes group tightly related helper types.
- Dynamic attributes are flexible but can be risky.
- `type()` checks exact type.
- `isinstance()` checks object plus inheritance.
- `issubclass()` checks class relationships.
- `dir()`, `getattr()`, `setattr()`, `hasattr()`, and `__dict__` support introspection.

## See also

- [Python advanced OOP: core concepts](core-concepts.md)
- [Python advanced OOP reference](advanced-oop-reference.md)
- [Python advanced OOP interview problems](interview-problems.md)
- [Python inheritance](../inheritance/core-concepts.md)
