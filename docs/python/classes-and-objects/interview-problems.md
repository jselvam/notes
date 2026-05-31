# Python Classes and Objects Interview Problems

## 1. Create a Product Class

### Problem

Create a class to store product name and price.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


product = Product("Laptop", 999.99)
print(product.name)
print(product.price)
```

**Complexity:** `O(1)` time and space per object.

## 2. Add a Product Label Method

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def label(self):
        return f"{self.name}: ${self.price:.2f}"


product = Product("Mouse", 25)
print(product.label())
```

## 3. Create Multiple Objects

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

## 4. Use a Class Attribute

```python
class Product:
    currency = "USD"

    def __init__(self, name, price):
        self.name = name
        self.price = price


product = Product("Keyboard", 75)
print(product.currency)
```

## 5. Avoid Shared Mutable Class Attribute

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

Each cart object should have its own `items` list.

## 6. Build a Cart Object

```python
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def total_items(self):
        return len(self.items)


cart = Cart()
cart.add_item("Laptop")
cart.add_item("Mouse")
print(cart.total_items())
```

## 7. Calculate Cart Total From Product Objects

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def total(self):
        return sum(product.price for product in self.items)


cart = Cart()
cart.add_item(Product("Laptop", 999.99))
cart.add_item(Product("Mouse", 25.00))

print(cart.total())
```

## 8. Add `__str__` for Product Display

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


print(Product("Monitor", 199.99))
```

## 9. Inventory Stock Update

```python
class InventoryItem:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def add_stock(self, quantity):
        self.stock += quantity

    def sell(self, quantity):
        if quantity > self.stock:
            return False
        self.stock -= quantity
        return True


item = InventoryItem("Keyboard", 10)
print(item.sell(3))
print(item.stock)
```

## 10. Customer Object With Address

```python
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.addresses = []

    def add_address(self, address):
        self.addresses.append(address)


customer = Customer("Selvam", "selvam@example.com")
customer.add_address("Chennai")

print(customer.addresses)
```

## Summary

| Problem pattern | Concept |
|-----------------|---------|
| product blueprint | class |
| product instance | object |
| product fields | instance attributes |
| display product | method, `__str__` |
| shared currency | class attribute |
| cart items | per-object mutable attribute |
| stock changes | methods update state |

## See also

- [Python classes and objects: core concepts](core-concepts.md)
- [Python classes and objects reference](classes-and-objects-reference.md)
- [Python classes and objects FAQ](frequently-asked-questions.md)
