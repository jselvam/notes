# Python-Specific OOP Features: Frequently Asked Interview Questions

## Basic Level

### 1. What is `@dataclass`?

`@dataclass` is a decorator that auto-generates common methods for data-focused classes.

### 2. Which module provides dataclasses?

The `dataclasses` module.

### 3. What methods can dataclasses generate?

They commonly generate `__init__()`, `__repr__()`, and comparison-related methods depending on options.

### 4. What is `field(default_factory=list)`?

It creates a new list for each object, avoiding shared mutable defaults.

### 5. What does `frozen=True` do?

It makes dataclass instances mostly immutable after creation.

### 6. What is `__slots__`?

`__slots__` restricts allowed attributes and can reduce memory usage.

### 7. What is a property?

A property lets a method be accessed like an attribute.

### 8. What is a property setter?

A setter controls and validates assignment to a property.

### 9. What is a descriptor?

A descriptor is an object that controls attribute access with `__get__`, `__set__`, or `__delete__`.

### 10. What is a metaclass?

A metaclass is a class that controls how classes are created.

## Intermediate Level

### 11. When should you use dataclasses?

Use them for classes that mostly store data with little custom behavior.

### 12. When should you avoid dataclasses?

Avoid them when a class has complex behavior or needs carefully designed initialization.

### 13. What problem does `default_factory` solve?

It prevents multiple objects from sharing the same mutable default list or dictionary.

### 14. Can dataclasses use slots?

Yes, modern Python supports `@dataclass(slots=True)`.

### 15. Why use `__slots__`?

Use it to reduce memory usage and prevent accidental dynamic attributes.

### 16. What is the downside of `__slots__`?

Objects become less flexible because undeclared attributes cannot be added normally.

### 17. When is `@property` better than a normal method?

Use `@property` for cheap computed values that should look like attributes.

### 18. When is a method better than `@property`?

Use a method for expensive work, side effects, or actions requiring parameters.

### 19. Why use descriptors?

Descriptors let you reuse attribute validation or access logic across many classes.

### 20. Are properties descriptors?

Yes. Python's `property` is implemented using the descriptor protocol.

## Advanced Level

### 21. What methods define a descriptor?

`__get__`, `__set__`, and `__delete__`.

### 22. What is `__set_name__()`?

It lets a descriptor know the attribute name it was assigned to in the owner class.

### 23. What is a data descriptor?

A descriptor that defines `__set__` or `__delete__`.

### 24. What is a non-data descriptor?

A descriptor that only defines `__get__`.

### 25. What are metaclasses used for?

They are used by frameworks, ORMs, validation systems, and APIs that need to customize class creation.

### 26. What is the default metaclass in Python?

`type`.

### 27. What is the relationship between class and metaclass?

A class creates objects. A metaclass creates classes.

### 28. Should metaclasses be common in application code?

No. Prefer simpler tools unless class creation must be customized.

### 29. What is a common interview mistake?

Using metaclasses when a decorator, base class, or normal function would be simpler.

### 30. What should you remember?

Dataclasses reduce boilerplate, slots restrict attributes, properties control attribute access, descriptors generalize properties, and metaclasses customize class creation.

## Final Interview Checklist

- Use `@dataclass` for data-focused classes.
- Use `field(default_factory=list)` for mutable defaults.
- Use `frozen=True` for immutable records.
- Use `__slots__` for fixed, memory-conscious objects.
- Use `@property` for computed or validated attributes.
- Use descriptors for reusable attribute behavior.
- Use metaclasses only for advanced class-creation control.

## See also

- [Python-specific OOP: core concepts](core-concepts.md)
- [Python-specific OOP reference](python-specific-oop-reference.md)
- [Python-specific OOP interview problems](interview-problems.md)
- [Python advanced OOP](../advanced-oop/core-concepts.md)
