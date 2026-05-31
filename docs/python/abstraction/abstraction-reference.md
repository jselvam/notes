# Python Data Abstraction Reference

## Quick Table

| Topic | Meaning | Example |
|-------|---------|---------|
| Abstraction | hide implementation details | `payment.pay(amount)` |
| Interface | expected behavior | `pay()`, `send()` |
| Abstract class | class that cannot be fully used directly | `class PaymentMethod(ABC)` |
| Abstract method | method child classes must implement | `@abstractmethod` |
| Concrete class | usable implementation | `CardPayment` |
| `ABC` | abstract base class helper | `from abc import ABC` |
| `@property` | attribute-style abstraction | `cart.total` |
| Duck typing | behavior matters more than exact type | object has `.pay()` |

## `abc` Module

```python
from abc import ABC, abstractmethod
```

Use `ABC` and `@abstractmethod` when you want to define required behavior.

## Abstract Class

```python
from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
```

You cannot instantiate a class while it still has unimplemented abstract methods.

## Concrete Class

```python
class CardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount:.2f} by card"
```

## Abstract Notification Sender

```python
class NotificationSender(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailSender(NotificationSender):
    def send(self, message):
        return f"Email sent: {message}"
```

## Duck Typing Abstraction

Python often uses duck typing instead of formal interfaces.

```python
def checkout(payment_method, amount):
    return payment_method.pay(amount)
```

Any object with a `pay()` method can be used.

## Property-Based Abstraction

```python
class Product:
    def __init__(self, price, tax_rate):
        self.price = price
        self.tax_rate = tax_rate

    @property
    def price_with_tax(self):
        return self.price + (self.price * self.tax_rate)
```

The caller does not need to know the formula details.

## Service Abstraction

```python
class InventoryService:
    def reserve(self, product_id, quantity):
        return True
```

The caller uses `reserve()` without knowing whether inventory is stored in memory, a file, or a database.

## Common Comparisons

| Pair | Difference |
|------|------------|
| abstraction vs encapsulation | hide implementation vs control data access |
| abstract class vs concrete class | contract vs usable implementation |
| inheritance vs abstraction | reuse/relationship vs hiding details behind interface |
| duck typing vs ABC | informal behavior check vs explicit contract |
| property vs method | attribute-style computed value vs action call |

## See also

- [Python data abstraction: core concepts](core-concepts.md)
- [Python data abstraction interview problems](interview-problems.md)
- [Python data abstraction FAQ](frequently-asked-questions.md)
