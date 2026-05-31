# Python OOP Interview Problems

## 1. Create a Product Class

### Problem

Create a `Product` class with name and price.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


laptop = Product("Laptop", 999.99)
print(laptop.name)
```

**Complexity:** `O(1)` time and space per object.

## 2. Add Product Label Method

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

## 3. Build a Cart Class

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

## 4. Calculate Cart Total

```python
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def total(self):
        return sum(product.price for product in self.items)
```

## 5. Use Inheritance for Digital Product

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class DigitalProduct(Product):
    def delivery_message(self):
        return f"{self.name} will be delivered by download link"


pdf_editor = DigitalProduct("PDF Editor", 49.99)
print(pdf_editor.delivery_message())
```

## 6. Override a Method

```python
class Product:
    def delivery_type(self):
        return "shipping"


class SoftwareProduct(Product):
    def delivery_type(self):
        return "license key"


product = SoftwareProduct()
print(product.delivery_type())
```

## 7. Use Polymorphism for Payments

```python
class CardPayment:
    def pay(self, amount):
        return f"Paid ${amount:.2f} using card"


class CashOnDelivery:
    def pay(self, amount):
        return f"Pay ${amount:.2f} during delivery"


def checkout(payment, amount):
    return payment.pay(amount)


print(checkout(CardPayment(), 999.99))
print(checkout(CashOnDelivery(), 999.99))
```

## 8. Use Encapsulation for Stock

```python
class InventoryItem:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def reserve(self, quantity):
        if quantity > self.stock:
            return False
        self.stock -= quantity
        return True


item = InventoryItem("Keyboard", 10)
print(item.reserve(2))
print(item.stock)
```

## 9. Use `@property` for Formatted Price

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

## 10. Prefer Composition for Order and Cart

```python
class Order:
    def __init__(self, order_id, cart):
        self.order_id = order_id
        self.cart = cart

    def summary(self):
        return f"Order {self.order_id} has {self.cart.total_items()} items"
```

Composition means `Order` has a `Cart`.

## Summary

| Problem pattern | OOP concept |
|-----------------|-------------|
| model product | class and object |
| store data | attributes |
| behavior | methods |
| digital product | inheritance |
| payment methods | polymorphism |
| stock handling | encapsulation |
| computed value | `@property` |
| order has cart | composition |

## See also

- [Python OOP: core concepts](core-concepts.md)
- [Python OOP reference](oop-reference.md)
- [Python OOP FAQ](frequently-asked-questions.md)
