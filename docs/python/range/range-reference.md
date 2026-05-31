# Python `range` Reference: Interview Notes

## Quick Table

| Form | Meaning | Example |
|------|---------|---------|
| `range(stop)` | `0` to `stop - 1` | `range(5)` |
| `range(start, stop)` | `start` to `stop - 1` | `range(1, 6)` |
| `range(start, stop, step)` | Step by value | `range(0, 10, 2)` |
| negative step | Count backwards | `range(5, 0, -1)` |

## Examples

```python
print(list(range(5)))          # [0, 1, 2, 3, 4]
print(list(range(1, 6)))       # [1, 2, 3, 4, 5]
print(list(range(0, 10, 2)))   # [0, 2, 4, 6, 8]
print(list(range(5, 0, -1)))   # [5, 4, 3, 2, 1]
```

## Range With Indexes

```python
cart = ["laptop", "mouse", "keyboard"]

for index in range(len(cart)):
    print(index, cart[index])
```

Prefer `enumerate()` when possible:

```python
for index, item in enumerate(cart):
    print(index, item)
```

## Range for Batches

```python
products = ["p1", "p2", "p3", "p4", "p5"]
batch_size = 2

for start in range(0, len(products), batch_size):
    batch = products[start:start + batch_size]
    print(batch)
```

## Range for Retry Attempts

```python
for attempt in range(1, 4):
    print(f"Payment attempt {attempt}")
```

## Common Interview Questions

### Is `range` memory efficient?

Yes. It stores start, stop, and step, not every value.

### Can `range` use float values?

No. `range()` works with integers.

### Can `step` be zero?

No. `range(..., step=0)` raises `ValueError`.

```python
# range(1, 10, 0)  # ValueError
```

## See also

- [Python range core concepts](core-concepts.md)
- [Python range interview problems](interview-problems.md)
- [Python range FAQ](frequently-asked-questions.md)
