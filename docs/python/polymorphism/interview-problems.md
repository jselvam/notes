# Python Polymorphism Interview Problems

## 1. Payment Method Polymorphism

### Problem

Create multiple payment methods with the same `pay()` method.

```python
class CardPayment:
    def pay(self, amount):
        return f"Paid ${amount:.2f} by card"


class UPIPayment:
    def pay(self, amount):
        return f"Paid ${amount:.2f} by UPI"


def checkout(payment_method, amount):
    return payment_method.pay(amount)


print(checkout(CardPayment(), 999.99))
print(checkout(UPIPayment(), 999.99))
```

**Complexity:** `O(1)` time and space.

## 2. Product Delivery Polymorphism

```python
class Product:
    def delivery_message(self):
        return "Standard delivery"


class DigitalProduct(Product):
    def delivery_message(self):
        return "Download link sent by email"


class PhysicalProduct(Product):
    def delivery_message(self):
        return "Product shipped by courier"


products = [DigitalProduct(), PhysicalProduct()]

for product in products:
    print(product.delivery_message())
```

## 3. Notification Sender Polymorphism

```python
class EmailSender:
    def send(self, message):
        return f"Email sent: {message}"


class SmsSender:
    def send(self, message):
        return f"SMS sent: {message}"


def notify(sender, message):
    return sender.send(message)


print(notify(EmailSender(), "Order shipped"))
print(notify(SmsSender(), "Order shipped"))
```

## 4. Duck Typing Without Inheritance

```python
class WalletPayment:
    def pay(self, amount):
        return f"Paid ${amount:.2f} using wallet"


def checkout(payment_method, amount):
    return payment_method.pay(amount)


print(checkout(WalletPayment(), 500))
```

The object works because it has the expected `pay()` method.

## 5. Discount Strategy Polymorphism

```python
class PercentageDiscount:
    def __init__(self, percent):
        self.percent = percent

    def apply(self, price):
        return price - (price * self.percent / 100)


class FlatDiscount:
    def __init__(self, amount):
        self.amount = amount

    def apply(self, price):
        return max(0, price - self.amount)


def final_price(discount, price):
    return discount.apply(price)


print(final_price(PercentageDiscount(10), 1000))
print(final_price(FlatDiscount(100), 1000))
```

## 6. Built-in `len()` Polymorphism

```python
print(len("laptop"))
print(len(["laptop", "mouse"]))
print(len({"name": "Laptop"}))
```

The same `len()` function works for different object types.

## 7. Operator Polymorphism

```python
print(10 + 5)
print("lap" + "top")
print(["laptop"] + ["mouse"])
```

The same `+` operator behaves differently for numbers, strings, and lists.

## 8. Custom Cart Addition

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

## 9. Polymorphism With Abstract Base Class

```python
from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount:.2f} by card"
```

## 10. Add New Payment Without Changing Checkout

```python
class CashOnDelivery:
    def pay(self, amount):
        return f"Pay ${amount:.2f} on delivery"


print(checkout(CashOnDelivery(), 250))
```

Polymorphism lets new implementations work with existing code.

## Summary

| Problem pattern | Polymorphism idea |
|-----------------|-------------------|
| payment methods | same `pay()` method |
| delivery behavior | method overriding |
| notification senders | same `send()` method |
| discount strategies | interchangeable `apply()` |
| built-in functions | `len()` on many types |
| operators | `+` behaves by type |
| custom operators | dunder methods |
| Python style | duck typing |

## See also

- [Python polymorphism: core concepts](core-concepts.md)
- [Python polymorphism reference](polymorphism-reference.md)
- [Python polymorphism FAQ](frequently-asked-questions.md)
