# Python Generators, Decorators, and Context Managers: Frequently Asked Questions

## Basic Level

### 1. What is a generator?

A generator is an iterator that produces values lazily, one at a time.

### 2. Which keyword creates a generator function?

`yield`.

### 3. What does `yield` do?

`yield` returns a value and pauses the function so it can continue later.

### 4. What is the difference between `yield` and `return`?

`yield` pauses and can produce many values. `return` exits the function with one final result.

### 5. What is a generator expression?

A generator expression is a lazy comprehension written with parentheses.

### 6. Give a generator expression example.

```python
prices = (price * 0.9 for price in [100, 200, 300])
```

### 7. What is a decorator?

A decorator wraps a function or class to add behavior.

### 8. What does `@decorator` mean?

It means the function or class below it is passed into the decorator.

### 9. What is a context manager?

A context manager manages setup and cleanup around a block of code.

### 10. Which statement uses context managers?

The `with` statement.

## Intermediate Level

### 11. Why use generators?

Use generators to save memory and process data lazily.

### 12. Are generators reusable?

Usually no. Once consumed, a generator is exhausted.

### 13. What happens when a generator has no more values?

Python raises `StopIteration`.

### 14. List comprehension vs generator expression?

List comprehension builds a full list immediately. Generator expression produces values lazily.

### 15. What is a function decorator used for?

Logging, validation, authorization, caching, timing, and retry logic.

### 16. Why use `functools.wraps`?

It preserves metadata such as function name and docstring after wrapping.

### 17. What is a decorator with arguments?

It is a decorator factory that returns the actual decorator.

### 18. What is decorator chaining?

Decorator chaining means applying multiple decorators to the same function or class.

### 19. What order do chained decorators apply?

They apply from bottom to top.

### 20. What is a class decorator?

A class decorator receives a class and returns the class or a modified replacement.

## Advanced Level

### 21. What is lazy evaluation?

Lazy evaluation delays work until the value is actually requested.

### 22. When is a generator better than a list?

When processing large data or streams where all values are not needed at once.

### 23. When is a list better than a generator?

When you need indexing, length, repeated iteration, or all values in memory.

### 24. Can generators read large files?

Yes. They are useful for reading and processing one line or record at a time.

### 25. What is a closure in decorators?

A closure remembers variables from an outer function after the outer function has returned.

### 26. Why can decorators be hard to debug?

They add hidden wrapper layers around the original function.

### 27. How do you keep decorators readable?

Keep them small, use `functools.wraps`, and avoid too many stacked decorators.

### 28. What methods implement a context manager?

`__enter__()` and `__exit__()`.

### 29. What does `__enter__()` do?

It performs setup and returns the object used after `as`.

### 30. What does `__exit__()` do?

It performs cleanup and receives exception information if an error occurred.

## Pro Level

### 31. What arguments does `__exit__()` receive?

`exc_type`, `exc_value`, and `traceback`.

### 32. How can `__exit__()` suppress an exception?

Return `True` from `__exit__()`.

### 33. Should `__exit__()` usually suppress exceptions?

No. Suppress exceptions only when it is intentional and documented.

### 34. Why is `with open(...)` preferred?

It closes the file automatically, even when an exception occurs.

### 35. How are context managers related to `try/finally`?

Context managers package `try/finally` style setup and cleanup into reusable objects.

### 36. Can decorators be classes?

Yes. A class can implement `__call__()` and be used as a decorator.

### 37. Can context managers be functions?

Yes, with `contextlib.contextmanager`, a generator function can define setup and cleanup.

### 38. What is a common generator interview warning?

Do not assume a generator can be iterated many times like a list.

### 39. What is a common decorator interview warning?

Decorator order matters when decorators are chained.

### 40. What is the final interview summary?

Generators handle lazy data, decorators add reusable behavior, and context managers guarantee cleanup.

## Final Interview Checklist

- Explain `yield` clearly.
- Know generator functions vs generator expressions.
- Know `next()` and `StopIteration`.
- Compare generator expressions with list comprehensions.
- Write a function decorator with `*args`, `**kwargs`, and `functools.wraps`.
- Explain decorator chaining order.
- Know class decorators.
- Explain `with`, `__enter__()`, and `__exit__()`.
- Know when `__exit__()` suppresses exceptions.
- Use shopping-system examples such as product streams, order logging, admin checks, and inventory locks.

## See also

- [Advanced functions: core concepts](core-concepts.md)
- [Advanced functions reference](advanced-functions-reference.md)
- [Advanced functions interview problems](interview-problems.md)
- [Python functions](../functions/core-concepts.md)
- [Dunder methods](../dunder-methods/core-concepts.md)
