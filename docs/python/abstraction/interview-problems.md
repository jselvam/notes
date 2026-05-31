# Python Data Abstraction Interview Problems

## 1. Create Abstract Payment Method

### Problem

Create an abstract payment type that forces every payment method to implement `pay()`.

```python
from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount:.2f} by card"


print(CardPayment().pay(999.99))
```

**Complexity:** `O(1)` time and space.

## 2. Add Another Payment Implementation

```python
class UPIPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount:.2f} by UPI"


print(UPIPayment().pay(299.99))
```

Both payment classes expose the same `pay()` abstraction.

## 3. Checkout Depends on Abstraction

```python
def checkout(payment_method, amount):
    return payment_method.pay(amount)


print(checkout(CardPayment(), 999.99))
print(checkout(UPIPayment(), 999.99))
```

The checkout logic does not know implementation details.

## 4. Abstract Notification Sender

```python
from abc import ABC, abstractmethod


class NotificationSender(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailSender(NotificationSender):
    def send(self, message):
        return f"Email sent: {message}"


class SmsSender(NotificationSender):
    def send(self, message):
        return f"SMS sent: {message}"
```

## 5. Inventory Service Hides Storage Details

```python
class InventoryService:
    def __init__(self):
        self._stock = {101: 5}

    def reserve(self, product_id, quantity):
        available = self._stock.get(product_id, 0)
        if quantity > available:
            return False
        self._stock[product_id] = available - quantity
        return True


inventory = InventoryService()
print(inventory.reserve(101, 2))
```

The caller does not need to know that `_stock` is a dictionary.

## 6. Cart Total as Property Abstraction

```python
class Cart:
    def __init__(self, prices):
        self._prices = prices

    @property
    def total(self):
        return sum(self._prices)


cart = Cart([999.99, 25.00])
print(cart.total)
```

## 7. Duck Typing for Payment

```python
class WalletPayment:
    def pay(self, amount):
        return f"Paid ${amount:.2f} using wallet"


def checkout(payment_method, amount):
    return payment_method.pay(amount)


print(checkout(WalletPayment(), 100))
```

No inheritance is required if the object has the expected behavior.

## 8. Abstract Discount Strategy

```python
from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, price):
        pass


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent):
        self.percent = percent

    def apply(self, price):
        return price - (price * self.percent / 100)


discount = PercentageDiscount(10)
print(discount.apply(1000))
```

## Summary

| Problem pattern | Abstraction idea |
|-----------------|------------------|
| payment methods | common `pay()` interface |
| checkout flow | depends on behavior, not details |
| notifications | common `send()` interface |
| inventory | hide storage details |
| cart total | computed property |
| discount strategy | interchangeable algorithm |
| Python style | ABC or duck typing |

## See also

- [Python data abstraction: core concepts](core-concepts.md)
- [Python data abstraction reference](abstraction-reference.md)
- [Python data abstraction FAQ](frequently-asked-questions.md)
