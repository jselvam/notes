# Python Iterator Reference: Interview Notes

## Quick Table

| Concept | Meaning | Example |
|---------|---------|---------|
| Iterable | Can produce iterator | `list`, `tuple`, `dict`, `range`, `str` |
| Iterator | Produces next value | `iter(items)` |
| `iter()` | Creates iterator | `iter(["laptop"])` |
| `next()` | Gets next value | `next(iterator)` |
| `StopIteration` | End signal | raised when exhausted |
| Generator | Iterator made with `yield` | `def f(): yield x` |

## `iter()`

```python
products = ["laptop", "mouse"]
iterator = iter(products)

print(iterator)
```

## `next()`

```python
products = ["laptop", "mouse"]
iterator = iter(products)

print(next(iterator))
print(next(iterator))
```

## Safe `next()` With Default

```python
products = iter([])

print(next(products, "no product"))
```

## Generator Function

```python
def product_ids():
    yield 101
    yield 102


ids = product_ids()
print(next(ids))
```

## Generator Expression

```python
prices = [999, 25, 75]
expensive = (price for price in prices if price >= 100)

print(next(expensive))
```

## `itertools`

`itertools` provides efficient iterator helpers.

```python
from itertools import islice

products = iter(["laptop", "mouse", "keyboard", "monitor"])
first_two = list(islice(products, 2))

print(first_two)
```

## Common Interview Questions

### Is a list an iterator?

No. A list is iterable. `iter(list)` returns an iterator.

### Can an iterator be reused?

Usually no. Once exhausted, it stays exhausted.

### Why use generators?

They are lazy and memory efficient.

## See also

- [Python iterators: core concepts](core-concepts.md)
- [Python iterator interview problems](interview-problems.md)
- [Python iterator FAQ](frequently-asked-questions.md)
