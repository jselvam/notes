# Python Dunder Methods Interview Problems

## 1. Initialize Product With `__init__`

### Problem

Create a `Product` class that stores product ID, name, and price.

```python
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


product = Product(101, "Laptop", 999.99)
print(product.name)
```

**Complexity:** `O(1)` time and space per object.

## 2. Add User-Friendly Display With `__str__`

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


print(Product("Mouse", 25))
```

## 3. Add Debug Display With `__repr__`

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price!r})"


product = Product("Keyboard", 75)
print(repr(product))
```

## 4. Make Cart Work With `len()`

```python
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)


cart = Cart()
cart.add_item("Laptop")
print(len(cart))
```

## 5. Compare Products With `__eq__`

```python
class Product:
    def __init__(self, product_id, name):
        self.product_id = product_id
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.product_id == other.product_id


print(Product(101, "Laptop") == Product(101, "Laptop Pro"))
```

## 6. Sort Products by Price With `__lt__`

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __lt__(self, other):
        return self.price < other.price

    def __repr__(self):
        return f"{self.name}: {self.price}"


products = [Product("Laptop", 999), Product("Mouse", 25)]
print(sorted(products))
```

## 7. Support Cart Indexing With `__getitem__`

```python
class Cart:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]


cart = Cart(["Laptop", "Mouse"])
print(cart[0])
```

## 8. Support `in` With `__contains__`

```python
class Cart:
    def __init__(self, items):
        self.items = items

    def __contains__(self, item):
        return item in self.items


cart = Cart(["Laptop", "Mouse"])
print("Mouse" in cart)
```

## 9. Support Iteration With `__iter__`

```python
class Cart:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        return iter(self.items)


for item in Cart(["Laptop", "Mouse"]):
    print(item)
```

## 10. Merge Carts With `__add__`

```python
class Cart:
    def __init__(self, items):
        self.items = items

    def __add__(self, other):
        return Cart(self.items + other.items)

    def __repr__(self):
        return f"Cart({self.items!r})"


cart1 = Cart(["Laptop"])
cart2 = Cart(["Mouse"])

print(cart1 + cart2)
```

## 11. Use Context Manager Dunder Methods

```python
class OrderSession:
    def __enter__(self):
        print("Open order session")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Close order session")
        return False


with OrderSession():
    print("Process order")
```

## Summary

| Problem pattern | Dunder method |
|-----------------|---------------|
| initialize object | `__init__` |
| readable display | `__str__` |
| debug display | `__repr__` |
| cart size | `__len__` |
| product equality | `__eq__` |
| sorting | `__lt__` |
| indexing | `__getitem__` |
| membership | `__contains__` |
| iteration | `__iter__` |
| context cleanup | `__enter__`, `__exit__` |

## See also

- [Python dunder methods: core concepts](core-concepts.md)
- [Python dunder methods reference](dunder-methods-reference.md)
- [Python dunder methods FAQ](frequently-asked-questions.md)
