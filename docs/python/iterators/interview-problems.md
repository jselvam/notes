# Python Iterator Interview Problems

## 1. Manually Iterate Products

```python
def manual_iterate(products):
    iterator = iter(products)
    result = []

    while True:
        try:
            result.append(next(iterator))
        except StopIteration:
            break

    return result


print(manual_iterate(["laptop", "mouse"]))
```

## 2. Generator for Product IDs

```python
def product_ids(start, stop):
    for product_id in range(start, stop + 1):
        yield product_id


print(list(product_ids(101, 105)))
```

## 3. First N Products From Iterator

```python
from itertools import islice


def first_n_products(products, n):
    return list(islice(iter(products), n))


print(first_n_products(["laptop", "mouse", "keyboard"], 2))
```

## 4. Custom Cart Iterator

```python
class Cart:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        return iter(self.items)


cart = Cart(["laptop", "mouse"])

for item in cart:
    print(item)
```

## 5. Infinite Order Number Generator

```python
def order_numbers(start=1):
    current = start

    while True:
        yield current
        current += 1


orders = order_numbers(1001)
print(next(orders))
print(next(orders))
```

## 6. Filter In-Stock Products Lazily

```python
def in_stock_products(products):
    for product in products:
        if product["stock"] > 0:
            yield product


products = [
    {"name": "laptop", "stock": 2},
    {"name": "mouse", "stock": 0},
]

print(list(in_stock_products(products)))
```

## 7. Iterator Exhaustion

```python
products = iter(["laptop"])

print(next(products, None))
print(next(products, None))
```

## 8. Chain Two Product Iterables

```python
from itertools import chain


hardware = ["laptop", "mouse"]
software = ["office-suite"]

print(list(chain(hardware, software)))
```

## Summary

| Pattern | Iterator idea |
|---------|---------------|
| Manual loop | `iter()` + `next()` |
| Lazy values | generator with `yield` |
| Limit output | `itertools.islice` |
| Infinite sequence | `while True` + `yield` |
| Custom iterable | `__iter__()` |
| Exhaustion | `StopIteration` |

## See also

- [Python iterators: core concepts](core-concepts.md)
- [Python iterator reference](iterator-reference.md)
- [Python iterator FAQ](frequently-asked-questions.md)
