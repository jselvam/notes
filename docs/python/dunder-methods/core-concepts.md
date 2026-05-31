# Python Dunder Methods: Core Concepts

Dunder methods are special Python methods with double underscores before and after their names, such as `__init__`, `__str__`, and `__len__`.

They are also called **magic methods** or **special methods**. Python calls them automatically when you use built-in syntax or built-in functions.

In an online computer shopping system, dunder methods help objects behave naturally:

- `Product("Laptop", 999.99)` initializes product data with `__init__`
- `print(product)` uses `__str__`
- `len(cart)` uses `__len__`
- `product1 == product2` uses `__eq__`
- `cart[0]` uses `__getitem__`

## What Does Dunder Mean?

**Dunder** means **double underscore**.

```python
__init__
__str__
__repr__
__len__
```

You normally do not call dunder methods directly. Python calls them through syntax or functions.

## `__init__()`

`__init__()` initializes a newly created object.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


product = Product("Laptop", 999.99)
print(product.name)
```

Interview point: `__init__()` does not create the object. It initializes the object after creation.

## `__str__()`

`__str__()` controls the user-friendly string version of an object.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


print(Product("Mouse", 25))
```

## `__repr__()`

`__repr__()` controls the developer-friendly representation.

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

## `__len__()`

`__len__()` lets an object work with `len()`.

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
cart.add_item("Mouse")

print(len(cart))
```

## `__eq__()`

`__eq__()` defines equality with `==`.

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

## Container-Like Objects

Methods such as `__getitem__`, `__iter__`, and `__contains__` make custom objects behave like containers.

```python
class Cart:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __contains__(self, item):
        return item in self.items


cart = Cart(["Laptop", "Mouse"])

print(cart[0])
print("Mouse" in cart)
```

## Common Gotchas

### Do not invent random dunder names

Only implement documented special methods.

### Return the correct type

`__len__()` must return a non-negative integer.

### `__repr__()` should help debugging

Make it clear and unambiguous when possible.

## Practice Problems

1. Add `__init__()` to a `Product` class.
2. Add `__str__()` for a readable product label.
3. Add `__repr__()` for debugging.
4. Add `__len__()` to a `Cart`.
5. Add `__eq__()` to compare products by product ID.

## See also

- [Python dunder methods reference](dunder-methods-reference.md)
- [Python dunder methods interview problems](interview-problems.md)
- [Python dunder methods FAQ](frequently-asked-questions.md)
- [Python classes and objects](../classes-and-objects/core-concepts.md)
