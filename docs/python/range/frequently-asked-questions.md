# Python `range`: Frequently Asked Interview Questions

## Basic Level

### 1. What is `range` in Python?

`range` represents an immutable sequence of integers.

```python
print(range(5))
```

### 2. Is `range` a list?

No. It is a range object.

### 3. How do you convert `range` to list?

```python
print(list(range(5)))
```

### 4. What does `range(5)` produce?

Numbers `0` through `4`.

### 5. Is stop value included?

No. Stop is exclusive.

### 6. What does `range(1, 5)` produce?

`1, 2, 3, 4`.

### 7. What does step do?

It controls how much the value changes each iteration.

```python
print(list(range(0, 10, 2)))
```

### 8. Can step be negative?

Yes.

```python
print(list(range(5, 0, -1)))
```

### 9. Can step be zero?

No. It raises `ValueError`.

### 10. Can `range` use floats?

No. Use integers only.

## Intermediate Level

### 11. Why is `range` memory efficient?

It stores start, stop, and step instead of all values.

### 12. When should you use `range(len(items))`?

Use it when you truly need indexes.

### 13. What is better when you need index and value?

Use `enumerate()`.

```python
for index, item in enumerate(["laptop", "mouse"]):
    print(index, item)
```

### 14. Can you check membership in range?

Yes.

```python
print(5 in range(1, 10))
```

### 15. Is range immutable?

Yes.

### 16. Can range be sliced?

Yes, slicing returns another range.

```python
print(range(10)[2:8:2])
```

### 17. Can range be reversed?

Use `reversed()` or negative step.

### 18. What does `len(range(10))` return?

`10`.

### 19. What is `range(0)`?

An empty range.

### 20. What is a common off-by-one bug?

Forgetting that stop is exclusive.

## Advanced Level

### 21. How do you process batches with range?

```python
for start in range(0, len(items), batch_size):
    batch = items[start:start + batch_size]
```

### 22. How do you loop backwards by index?

```python
for i in range(len(items) - 1, -1, -1):
    print(items[i])
```

### 23. What is range useful for in FizzBuzz?

Looping from `1` to `n`.

### 24. What is range useful for in pagination?

Generating page numbers.

### 25. What is range useful for in retry logic?

Looping fixed attempts.

### 26. Is range hashable?

Yes, range objects are hashable in modern Python.

### 27. Can ranges be compared?

Yes, ranges compare by sequence equality.

```python
print(range(0, 3, 1) == range(0, 3))
```

### 28. What is the time complexity of iterating range?

**O(n)** for `n` generated values.

### 29. What is the space complexity of range itself?

**O(1)**.

### 30. What should you remember in interviews?

Stop is exclusive, step cannot be zero, and `range` is lazy/memory efficient.

## See also

- [Python range core concepts](core-concepts.md)
- [Python range reference](range-reference.md)
- [Python range interview problems](interview-problems.md)
