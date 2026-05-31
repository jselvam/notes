# Python Dunder Methods Reference

## Quick Table

| Method | Triggered by | Use case |
|--------|--------------|----------|
| `__init__` | object creation after `__new__` | initialize attributes |
| `__str__` | `str(obj)`, `print(obj)` | user-friendly display |
| `__repr__` | `repr(obj)`, debugger | developer-friendly display |
| `__len__` | `len(obj)` | object size |
| `__bool__` | `bool(obj)`, `if obj` | truthiness |
| `__eq__` | `==` | equality |
| `__lt__` | `<` | sorting/comparison |
| `__hash__` | `hash(obj)`, set/dict key | hashability |
| `__getitem__` | `obj[index]` | indexing |
| `__setitem__` | `obj[index] = value` | indexed assignment |
| `__iter__` | `iter(obj)`, `for` loop | iteration |
| `__next__` | `next(obj)` | iterator values |
| `__contains__` | `in` | membership |
| `__add__` | `+` | custom addition |
| `__enter__` | `with obj` start | context manager setup |
| `__exit__` | `with obj` end | context manager cleanup |

## Object Initialization

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
```

## Display Methods

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price!r})"
```

## Truthiness

```python
class Cart:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)


cart = Cart([])
print(bool(cart))
```

If `__bool__()` is not defined, Python can use `__len__()` for truthiness.

## Equality

```python
class Product:
    def __init__(self, product_id):
        self.product_id = product_id

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.product_id == other.product_id
```

## Sorting

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __lt__(self, other):
        return self.price < other.price


products = [Product("Laptop", 999), Product("Mouse", 25)]
products.sort()
```

## Indexing and Membership

```python
class Cart:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __contains__(self, item):
        return item in self.items
```

## Iteration

```python
class Cart:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        return iter(self.items)
```

## Operator Overloading

```python
class Cart:
    def __init__(self, items):
        self.items = items

    def __add__(self, other):
        return Cart(self.items + other.items)
```

## Context Manager

```python
class OrderSession:
    def __enter__(self):
        print("Start order session")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("End order session")
        return False


with OrderSession():
    print("Processing order")
```

## Common Comparisons

| Pair | Difference |
|------|------------|
| `__init__` vs `__new__` | initialize object vs create object |
| `__str__` vs `__repr__` | user display vs developer/debug display |
| `__eq__` vs `is` | equality rule vs identity |
| `__len__` vs `__bool__` | size vs direct truthiness |
| `__iter__` vs `__next__` | iterable behavior vs iterator step |

## See also

- [Python dunder methods: core concepts](core-concepts.md)
- [Python dunder methods interview problems](interview-problems.md)
- [Python dunder methods FAQ](frequently-asked-questions.md)
