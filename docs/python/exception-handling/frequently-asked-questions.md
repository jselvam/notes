# Python Exception Handling: Frequently Asked Interview Questions

## Basic Level

### 1. What is an exception?

An exception is a runtime error or unusual condition that interrupts normal program flow.

### 2. What is exception handling?

Exception handling is the process of catching and responding to exceptions.

### 3. What does `try` do?

`try` wraps code that may raise an exception.

### 4. What does `except` do?

`except` catches and handles matching exceptions.

### 5. What does `else` do?

`else` runs only when the `try` block finishes without an exception.

### 6. What does `finally` do?

`finally` runs whether an exception happens or not.

### 7. Can `try` exist without `except`?

Yes, if it has `finally`.

### 8. Can `try` have multiple `except` blocks?

Yes, and this is common when different errors need different handling.

### 9. What is `ValueError`?

It means the type is correct but the value is invalid.

### 10. What is `KeyError`?

It happens when a dictionary key is missing.

## Intermediate Level

### 11. When should you use `else`?

Use `else` for success-path code that should run only if no exception occurs.

### 12. When should you use `finally`?

Use `finally` for cleanup such as closing files or releasing resources.

### 13. What is the difference between `except Exception` and bare `except`?

`except Exception` catches most normal exceptions. Bare `except` catches more, including things like keyboard interrupts, so it is usually avoided.

### 14. Why catch specific exceptions?

Specific exceptions avoid hiding unrelated bugs.

### 15. How do you access the exception object?

```python
try:
    int("bad")
except ValueError as error:
    print(error)
```

### 16. How do you catch multiple exception types in one block?

```python
except (TypeError, ValueError):
    pass
```

### 17. What does `raise` do?

It raises an exception manually.

### 18. What does re-raise mean?

Calling `raise` inside an `except` block raises the same exception again.

### 19. What is a custom exception?

A custom exception is a user-defined exception class, usually inheriting from `Exception`.

### 20. Should exceptions be used for normal control flow?

Usually no. Use exceptions for exceptional or error-like cases.

## Advanced Level

### 21. Does `finally` run after `return`?

Yes. `finally` runs even if `try` or `except` returns.

### 22. What happens if `finally` raises an exception?

The `finally` exception can override the original exception.

### 23. What happens if `finally` returns a value?

It can override a return value from `try` or `except`, so avoid returning from `finally`.

### 24. What is exception chaining?

Exception chaining shows that one exception happened while handling another.

### 25. How do you raise a new exception from another?

```python
raise ValueError("Invalid order") from error
```

### 26. What is `try` with `with` used for?

`with` handles resource cleanup automatically; `try` handles errors around that work.

### 27. Is `finally` needed for file closing when using `with`?

Usually no. `with open(...)` closes the file automatically.

### 28. What is a common exception-handling mistake?

Catching every exception and silently ignoring it.

### 29. How is exception handling useful in a shopping app?

It handles invalid input, missing product data, payment failures, and file/API errors gracefully.

### 30. What should you remember for interviews?

Know when `try`, `except`, `else`, and `finally` run; catch specific exceptions; use `raise` for invalid business rules; avoid silent broad catches.

## See also

- [Python exception handling: core concepts](core-concepts.md)
- [Python exception handling reference](exception-handling-reference.md)
- [Python exception handling interview problems](interview-problems.md)
