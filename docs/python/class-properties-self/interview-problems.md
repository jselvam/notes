# Python Class Properties and self Interview Problems

## 1. Store Product Data With `self`

### Problem

Create a `Product` class that stores name and price per object.

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

**Complexity:** `O(1)` time and space per object.

## 2. Add a Shared Class Property

```python
class Product:
    currency = "USD"

    def __init__(self, name, price):
        self.name = name
        self.price = price


product = Product("Keyboard", 75)
print(product.currency)
print(Product.currency)
```

## 3. Use `self` in an Instance Method

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def label(self):
        return f"{self.name}: ${self.price:.2f}"


print(Product("Monitor", 199.99).label())
```

## 4. Create a Computed Property

```python
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def formatted_price(self):
        return f"${self.price:.2f}"


product = Product(999.9)
print(product.formatted_price)
```

## 5. Validate Price With Setter

```python
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value


product = Product(100)
product.price = 120
print(product.price)
```

## 6. Validate Stock With Setter

```python
class InventoryItem:
    def __init__(self, stock):
        self.stock = stock

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError("Stock cannot be negative")
        self._stock = value
```

## 7. Avoid Shared Cart Items

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

    def add_item(self, item):
        self.items.append(item)
```

Each cart gets its own `items` list.

## 8. Read-Only Cart Total

```python
class Cart:
    def __init__(self, prices):
        self.prices = prices

    @property
    def total(self):
        return sum(self.prices)


cart = Cart([999.99, 25.00])
print(cart.total)
```

## 9. Explain Method Binding

```python
class Product:
    def label(self):
        return "Product label"


product = Product()
print(product.label())
```

When `product.label()` is called, Python passes `product` automatically as `self`.

## 10. Use Class Property for Tax Rate

```python
class Product:
    tax_rate = 0.18

    def __init__(self, price):
        self.price = price

    @property
    def price_with_tax(self):
        return self.price + (self.price * self.tax_rate)


product = Product(1000)
print(product.price_with_tax)
```

## Summary

| Problem pattern | Concept |
|-----------------|---------|
| per-product data | instance properties |
| shared currency/tax | class properties |
| current object | `self` |
| computed value | `@property` |
| validation | property setter |
| avoid shared lists | instance mutable attributes |
| method call binding | Python passes object as `self` |

## See also

- [Python class properties and self: core concepts](core-concepts.md)
- [Python class properties and self reference](class-properties-self-reference.md)
- [Python class properties and self FAQ](frequently-asked-questions.md)
