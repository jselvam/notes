# Python Dunder Methods: Frequently Asked Interview Questions

## Basic Level

### 1. What is a dunder method?

A dunder method is a special method with double underscores before and after its name, such as `__init__`.

### 2. What does dunder mean?

Dunder means double underscore.

### 3. What is `__init__()`?

`__init__()` initializes object attributes after an object is created.

### 4. Does `__init__()` create the object?

No. `__new__()` creates the object; `__init__()` initializes it.

### 5. What should `__init__()` return?

It should return `None` implicitly. Do not return another value.

### 6. What is `__str__()`?

It returns a user-friendly string representation.

### 7. What is `__repr__()`?

It returns a developer-friendly representation useful for debugging.

### 8. What is `__len__()`?

It defines behavior for `len(obj)`.

### 9. What is `__eq__()`?

It defines behavior for `obj1 == obj2`.

### 10. Should you call dunder methods directly?

Usually no. Use the syntax or built-in function that triggers them.

## Intermediate Level

### 11. What is the difference between `__str__()` and `__repr__()`?

`__str__()` is for readable user output. `__repr__()` is for debugging and developer output.

### 12. What happens if `__str__()` is missing?

Python may fall back to `__repr__()` for string display.

### 13. What should `__repr__()` ideally return?

It should be clear and unambiguous; when possible, it should look like code that can recreate the object.

### 14. What is `__bool__()`?

It defines truthiness for `bool(obj)` and `if obj`.

### 15. What happens if `__bool__()` is missing?

Python may use `__len__()` to decide truthiness.

### 16. What is `__getitem__()`?

It defines indexing behavior like `obj[index]`.

### 17. What is `__contains__()`?

It defines membership behavior for `in`.

### 18. What is `__iter__()`?

It defines iteration behavior for loops and `iter(obj)`.

### 19. What is `__next__()`?

It returns the next value from an iterator.

### 20. What is `__add__()`?

It defines behavior for the `+` operator.

## Advanced Level

### 21. What is operator overloading?

Operator overloading means defining how operators like `+`, `==`, or `<` behave for custom objects.

### 22. What is `__lt__()`?

It defines less-than comparison with `<`, often used for sorting.

### 23. What is `__hash__()`?

It defines a hash value so objects can be used in sets or as dictionary keys.

### 24. What is the rule for `__eq__()` and `__hash__()`?

If two objects are equal, they must have the same hash value.

### 25. What is `NotImplemented`?

`NotImplemented` tells Python that the operation is unsupported for the given other object, allowing fallback behavior.

### 26. What are `__enter__()` and `__exit__()`?

They define context manager behavior for `with`.

### 27. What should `__exit__()` return?

Return `True` to suppress an exception, or `False` to let it propagate.

### 28. What is `__call__()`?

It makes an object callable like a function.

### 29. What is a common dunder-method mistake?

Defining dunder methods with the wrong return type, such as returning a string from `__len__()`.

### 30. What should you remember?

Use dunder methods to make custom objects work naturally with Python syntax and built-ins.

## Final Interview Checklist

- `__init__()` initializes object state.
- `__new__()` creates the object.
- `__str__()` is user-friendly.
- `__repr__()` is developer-friendly.
- `__len__()` powers `len()`.
- `__bool__()` powers truthiness.
- `__eq__()` powers `==`.
- `__lt__()` helps sorting.
- `__getitem__()` powers indexing.
- `__iter__()` powers loops.
- `__enter__()` and `__exit__()` power `with`.

## See also

- [Python dunder methods: core concepts](core-concepts.md)
- [Python dunder methods reference](dunder-methods-reference.md)
- [Python dunder methods interview problems](interview-problems.md)
- [Python classes and objects](../classes-and-objects/core-concepts.md)
