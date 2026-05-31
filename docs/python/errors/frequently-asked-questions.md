# Python Error Types: Frequently Asked Interview Questions

## Basic Level

### 1. What is an error in Python?

An error is a problem that stops normal program execution.

### 2. What is an exception?

An exception is a Python object raised when something goes wrong at runtime.

### 3. What is `TypeError`?

`TypeError` happens when an operation is used with the wrong type.

### 4. What is `ValueError`?

`ValueError` happens when the type is correct but the value is invalid.

### 5. What is `NameError`?

`NameError` happens when a variable or function name is not defined.

### 6. What is `KeyError`?

`KeyError` happens when a dictionary key is missing.

### 7. What is `IndexError`?

`IndexError` happens when a sequence index is out of range.

### 8. What is `AttributeError`?

`AttributeError` happens when an object does not have the requested attribute or method.

### 9. What is `ZeroDivisionError`?

It happens when code divides by zero.

### 10. What is `FileNotFoundError`?

It happens when Python cannot find the requested file.

## Intermediate Level

### 11. What is `ModuleNotFoundError`?

It happens when Python cannot find the module being imported.

### 12. What is `ImportError`?

It is a broader import failure, often caused by importing a missing name from an existing module.

### 13. What is `SyntaxError`?

It happens when Python code is not valid syntax.

### 14. What is `IndentationError`?

It happens when indentation is invalid.

### 15. What is `TabError`?

It happens when tabs and spaces are mixed inconsistently.

### 16. What is `UnboundLocalError`?

It happens when a local variable is referenced before it gets a value.

### 17. What is `RecursionError`?

It happens when recursion goes too deep, often because a base case is missing.

### 18. What is `StopIteration`?

It signals that an iterator has no more values.

### 19. What is `AssertionError`?

It happens when an `assert` condition is false.

### 20. What is `PermissionError`?

It happens when the program does not have permission for a file or operation.

## Advanced Level

### 21. What is the difference between `TypeError` and `ValueError`?

`TypeError` means the type is wrong. `ValueError` means the type is acceptable but the value is invalid.

### 22. What is the difference between `KeyError` and `IndexError`?

`KeyError` is for missing dictionary keys. `IndexError` is for invalid sequence positions.

### 23. What is the difference between `ImportError` and `ModuleNotFoundError`?

`ModuleNotFoundError` is a specific kind of import failure where the module cannot be found.

### 24. What is the difference between `SyntaxError` and runtime errors?

`SyntaxError` prevents code from starting. Runtime errors happen while code is running.

### 25. Why should you not catch all errors silently?

It hides bugs and makes debugging difficult.

### 26. Which error happens for `int("abc")`?

`ValueError`.

### 27. Which error happens for `"10" + 5`?

`TypeError`.

### 28. Which error happens for `products[99]`?

`IndexError` if the list is shorter than 100 items.

### 29. Which error happens for `product["price"]` when `price` is missing?

`KeyError`.

### 30. Which error happens for calling a missing method?

`AttributeError`.

## Pro Level

### 31. What is the base class for most normal exceptions?

`Exception`.

### 32. What is `BaseException`?

It is the root of Python's exception hierarchy. Most application code should catch `Exception`, not `BaseException`.

### 33. Why avoid bare `except:`?

It catches too much, including interrupts that should usually stop the program.

### 34. Can you create custom error types?

Yes, by subclassing `Exception`.

```python
class OutOfStockError(Exception):
    pass
```

### 35. When should you raise `ValueError`?

Raise it when a function receives a valid type but an invalid value.

### 36. When should you raise `TypeError`?

Raise it when a function receives an unsupported type.

### 37. What is exception chaining?

It links a new exception to the original cause using `raise NewError() from error`.

### 38. What is a traceback?

A traceback shows the call stack where an error occurred.

### 39. How do errors help in interviews?

They show whether you understand debugging, input validation, and choosing specific exception handlers.

### 40. What should you remember?

Know common error types, why they happen, how to fix them, and when to catch or raise them.

## Final Interview Checklist

- Know `TypeError` vs `ValueError`.
- Know `KeyError` vs `IndexError`.
- Know `ImportError` vs `ModuleNotFoundError`.
- Use specific `except` blocks.
- Avoid silent broad catches.
- Use custom exceptions for business-specific failures.

## See also

- [Python error types: core concepts](core-concepts.md)
- [Python error types reference](error-types-reference.md)
- [Python error types interview problems](interview-problems.md)
- [Python exception handling](../exception-handling/core-concepts.md)
