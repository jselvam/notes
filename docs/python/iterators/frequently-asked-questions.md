# Python Iterators: Frequently Asked Interview Questions

## Basic Level

### 1. What is an iterator?

An iterator returns values one at a time using `next()`.

### 2. What is an iterable?

An iterable is an object that can return an iterator.

### 3. Is a list iterable?

Yes.

### 4. Is a list an iterator?

No. Use `iter(list)` to get an iterator.

### 5. What does `iter()` do?

It returns an iterator.

### 6. What does `next()` do?

It returns the next value from an iterator.

### 7. What happens when an iterator ends?

It raises `StopIteration`.

### 8. What is a generator?

A generator is an iterator created with `yield`.

### 9. Are strings iterable?

Yes.

### 10. Are dictionaries iterable?

Yes. Iterating a dictionary gives keys by default.

## Intermediate Level

### 11. How does a `for` loop work internally?

It calls `iter()` and then repeatedly calls `next()`.

### 12. Can an iterator be reused?

Usually no. Once exhausted, it remains exhausted.

### 13. How do you provide a default to `next()`?

```python
print(next(iterator, None))
```

### 14. What is lazy evaluation?

Values are produced only when requested.

### 15. Why are generators memory efficient?

They do not build all values at once.

### 16. What is a generator expression?

A lazy expression like a list comprehension.

```python
values = (x * 2 for x in range(3))
```

### 17. What is `yield`?

It pauses a function and returns a value, resuming later.

### 18. What is `yield from`?

It delegates yielding to another iterable.

### 19. What is `itertools`?

A standard library module for efficient iterator tools.

### 20. What is `islice()`?

It slices an iterator lazily.

## Advanced Level

### 21. How do you make a custom iterator?

Implement `__iter__()` and `__next__()`.

### 22. How do you make a custom iterable?

Implement `__iter__()` to return an iterator.

### 23. What should `__iter__()` return for an iterator?

It usually returns `self`.

### 24. What should `__next__()` do when done?

Raise `StopIteration`.

### 25. What is an infinite iterator?

An iterator that never naturally stops.

### 26. How do you safely use infinite iterators?

Limit them with `break`, `islice`, or a condition.

### 27. What is iterator exhaustion?

The state after all values have been consumed.

### 28. What is the main interview trap?

Trying to reuse an exhausted iterator.

### 29. Iterator or list?

Use iterator for lazy memory-efficient processing; list when you need indexing or repeated traversal.

### 30. What should you remember?

Iterable creates iterator; iterator produces values; generator is the easiest way to write one.

## See also

- [Python iterators: core concepts](core-concepts.md)
- [Python iterator reference](iterator-reference.md)
- [Python iterator interview problems](interview-problems.md)
