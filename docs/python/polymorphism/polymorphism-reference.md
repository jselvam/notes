# Python Polymorphism Reference

## Quick Table

| Topic | Meaning | Example |
|-------|---------|---------|
| Polymorphism | same interface, different behavior | `payment.pay()` |
| Method overriding | child replaces parent method | `delivery_message()` |
| Duck typing | behavior matters more than type | object has `pay()` |
| Built-in polymorphism | built-ins work on many types | `len()` |
| Operator polymorphism | operators vary by type | `+` |
| Dunder methods | customize operators/functions | `__len__`, `__add__` |
| Interface | expected method set | `pay()`, `send()` |

## Same Method, Different Classes

```python
class EmailSender:
    def send(self, message):
        return f"Email sent: {message}"


class SmsSender:
    def send(self, message):
        return f"SMS sent: {message}"
```

## Polymorphic Function

```python
def notify(sender, message):
    return sender.send(message)
```

Any object with `send()` works.

## Inheritance-Based Polymorphism

```python
class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError


class CardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount:.2f} by card"
```

## Duck Typing

```python
class CashOnDelivery:
    def pay(self, amount):
        return f"Pay ${amount:.2f} on delivery"
```

`CashOnDelivery` can work with checkout code if it has `pay()`.

## Built-in Function Polymorphism

```python
print(len("mouse"))
print(len(["mouse", "keyboard"]))
print(len({"mouse": 25, "keyboard": 75}))
```

## Operator Polymorphism

```python
print(5 + 3)
print("PDF " + "Editor")
print(["laptop"] + ["mouse"])
```

## Custom Operator Polymorphism

```python
class Cart:
    def __init__(self, items):
        self.items = items

    def __add__(self, other):
        return Cart(self.items + other.items)

    def __repr__(self):
        return f"Cart({self.items!r})"
```

## Polymorphism With Abstract Base Class

```python
from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, price):
        pass
```

## Common Comparisons

| Pair | Difference |
|------|------------|
| polymorphism vs inheritance | behavior flexibility vs class relationship/reuse |
| polymorphism vs abstraction | same interface with many implementations vs hiding details |
| overriding vs overloading | child method replacement vs same name with different input forms |
| duck typing vs ABC | informal behavior compatibility vs explicit contract |
| operator polymorphism vs method polymorphism | operators vary by type vs method names vary by implementation |

## See also

- [Python polymorphism: core concepts](core-concepts.md)
- [Python polymorphism interview problems](interview-problems.md)
- [Python polymorphism FAQ](frequently-asked-questions.md)
