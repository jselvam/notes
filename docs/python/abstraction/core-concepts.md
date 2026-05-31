# Python Data Abstraction: Core Concepts

Data abstraction is an OOP concept that hides implementation details and exposes only the important behavior to the user of a class or module.

In an online computer shopping system, abstraction lets code use simple operations such as:

- `payment.pay(amount)`
- `inventory.reserve(product_id, quantity)`
- `cart.total`
- `order.cancel()`
- `notification.send(message)`

The caller does not need to know the internal details of payment gateways, inventory databases, discount rules, or notification providers.

## Why Abstraction Matters

Without abstraction, high-level code becomes tightly connected to low-level details.

```python
payment_gateway_url = "https://payment.example.com"
api_key = "secret"
amount = 999.99

# Checkout code should not need to know all gateway details.
```

With abstraction:

```python
payment.pay(999.99)
```

The checkout flow only knows what it needs: "pay this amount".

## Simple Abstraction With a Class

```python
class PaymentService:
    def pay(self, amount):
        return f"Paid ${amount:.2f}"


payment = PaymentService()
print(payment.pay(999.99))
```

The caller uses `pay()` without knowing how payment is processed.

## Abstract Base Classes

Python provides abstract base classes through the `abc` module.

```python
from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
```

An abstract method defines what child classes must implement.

## Concrete Implementation

```python
class CardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount:.2f} by card"


class UPIPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount:.2f} by UPI"
```

Both classes expose the same method: `pay()`.

## Use Abstraction in Checkout

```python
def checkout(payment_method, amount):
    return payment_method.pay(amount)


print(checkout(CardPayment(), 999.99))
print(checkout(UPIPayment(), 999.99))
```

The checkout function does not care whether payment uses card, UPI, or another provider.

## Abstraction With Properties

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

The caller uses `cart.total` without knowing how the total is calculated.

## Abstraction vs Encapsulation

| Concept | Focus |
|---------|-------|
| Abstraction | hide implementation details |
| Encapsulation | protect and control access to data |

They often work together.

## Common Gotchas

### Do not over-design small code

If only one implementation exists and the logic is simple, a normal class or function may be enough.

### Abstract classes should define behavior, not details

An abstract class should say what must be done, not how every child must do it.

### Keep interfaces small

Avoid forcing child classes to implement methods they do not need.

## Practice Problems

1. Create an abstract `PaymentMethod` with `pay()`.
2. Implement `CardPayment` and `UPIPayment`.
3. Write a checkout function that accepts any payment method.
4. Create an abstract `NotificationSender` with `send()`.
5. Explain abstraction vs encapsulation.

## See also

- [Python data abstraction reference](abstraction-reference.md)
- [Python data abstraction interview problems](interview-problems.md)
- [Python data abstraction FAQ](frequently-asked-questions.md)
- [Python encapsulation](../encapsulation/core-concepts.md)
