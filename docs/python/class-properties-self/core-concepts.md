# Python Class Properties and self Parameter: Core Concepts

Class properties and the `self` parameter are central to writing useful Python classes.

In an online computer shopping system, they help model product details, cart state, stock changes, formatted prices, customer data, and order summaries.

## What Is `self`?

`self` refers to the current object.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


laptop = Product("Laptop", 999.99)
mouse = Product("Mouse", 25.00)

print(laptop.name)
print(mouse.name)
```

`laptop` and `mouse` are different objects, so each object has its own `name` and `price`.

## Why Is `self` Needed?

`self` tells Python which object should store or read the data.

```python
class CartItem:
    def __init__(self, product_name, quantity):
        self.product_name = product_name
        self.quantity = quantity
```

Without `self`, Python would only create local variables inside the method.

## Instance Properties

Instance properties belong to a specific object.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
```

Here, `name` and `price` are instance properties.

## Class Properties

Class properties are shared by all objects of a class.

```python
class Product:
    currency = "USD"

    def __init__(self, name, price):
        self.name = name
        self.price = price


product = Product("Keyboard", 75)
print(product.currency)
```

Use class properties for values that are common to all instances.

## Instance Method and `self`

Instance methods receive `self` as the first parameter.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def label(self):
        return f"{self.name}: ${self.price:.2f}"
```

When you call `product.label()`, Python automatically passes `product` as `self`.

## The `@property` Decorator

`@property` lets a method be accessed like an attribute.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def formatted_price(self):
        return f"${self.price:.2f}"


product = Product("Monitor", 199.9)
print(product.formatted_price)
```

Use `@property` for computed values that should look like read-only attributes.

## Property Setter

A setter validates or controls updates.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value


product = Product("Mouse", 25)
product.price = 30
print(product.price)
```

The `_price` name is a convention that means "internal use".

## Common Gotchas

### `self` is not a keyword

`self` is a strong naming convention. Use it so Python developers understand your code.

### Do not use mutable class properties for per-object data

Bad:

```python
class Cart:
    items = []
```

Good:

```python
class Cart:
    def __init__(self):
        self.items = []
```

### `@property` should not hide expensive work

If a calculation is slow or has side effects, prefer a normal method.

## Practice Problems

1. Create a `Product` class with instance properties.
2. Add a shared class property called `currency`.
3. Add a `label()` method that uses `self`.
4. Add a `formatted_price` property.
5. Add a setter that prevents negative stock.

## See also

- [Python class properties and self reference](class-properties-self-reference.md)
- [Python class properties and self interview problems](interview-problems.md)
- [Python class properties and self FAQ](frequently-asked-questions.md)
- [Python classes and objects](../classes-and-objects/core-concepts.md)
