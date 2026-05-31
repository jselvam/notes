# Python Classes and Objects: Frequently Asked Interview Questions

## Basic Level

### 1. What is a class?

A class is a blueprint for creating objects.

### 2. What is an object?

An object is an instance of a class.

### 3. How do you define a class?

```python
class Product:
    pass
```

### 4. How do you create an object?

```python
product = Product()
```

### 5. What is an attribute?

An attribute is data stored on an object or class.

### 6. What is a method?

A method is a function defined inside a class.

### 7. What is `self`?

`self` refers to the current object.

### 8. What is `__init__()`?

`__init__()` initializes object attributes.

### 9. Is `self` a keyword?

No. `self` is a naming convention, but it should be used for readability.

### 10. Can a class be empty?

Yes, use `pass`.

## Intermediate Level

### 11. What is an instance attribute?

An instance attribute belongs to a specific object.

### 12. What is a class attribute?

A class attribute belongs to the class and is shared by instances.

### 13. How do you access an attribute?

Use dot notation.

```python
print(product.name)
```

### 14. How do you update an attribute?

Assign a new value with dot notation.

```python
product.price = 899.99
```

### 15. Can Python objects get new attributes dynamically?

Yes, unless the class restricts it with features such as `__slots__`.

### 16. Why avoid mutable class attributes for instance data?

They are shared across objects and can cause unexpected behavior.

### 17. What is `__str__()`?

It returns a user-friendly string for an object.

### 18. What is `__repr__()`?

It returns a developer-friendly representation.

### 19. What is the difference between `__str__()` and `__repr__()`?

`__str__()` is for users. `__repr__()` is for debugging and developers.

### 20. What happens if an instance method does not include `self`?

Calling it on an object usually raises `TypeError`.

## Advanced Level

### 21. Are classes objects in Python?

Yes. Classes themselves are objects.

### 22. Can methods modify object state?

Yes. Methods can update attributes through `self`.

### 23. What is object state?

Object state is the current data stored in its attributes.

### 24. What is object behavior?

Object behavior is what the object can do through methods.

### 25. What is the difference between object state and behavior?

State is data. Behavior is action.

### 26. What is an instance?

An instance is another word for an object created from a class.

### 27. What is instantiation?

Instantiation is the process of creating an object from a class.

### 28. When should you create a class?

Create a class when data and behavior naturally belong together.

### 29. When should you avoid a class?

Avoid a class when a simple function or dictionary is clearer.

### 30. What should you remember?

Know class, object, attribute, method, `self`, `__init__`, class attributes, instance attributes, and mutable class attribute pitfalls.

## Final Interview Checklist

- Class is a blueprint.
- Object is an instance.
- `__init__()` initializes object data.
- `self` points to the current object.
- Instance attributes belong to one object.
- Class attributes are shared.
- Methods define behavior.
- Avoid mutable class attributes for per-object state.
- Use `__str__()` for readable object display.

## See also

- [Python classes and objects: core concepts](core-concepts.md)
- [Python classes and objects reference](classes-and-objects-reference.md)
- [Python classes and objects interview problems](interview-problems.md)
- [Python OOP core concepts](../oop/core-concepts.md)
