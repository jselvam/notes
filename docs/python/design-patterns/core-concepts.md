# Python Design Patterns: Core Concepts

Design patterns are reusable ways to solve common software design problems. In Python interviews, they are useful when you can explain **when to use them**, **when not to use them**, and show a small practical example.

This page covers:

- Singleton -> database connection
- Factory -> create product types
- Strategy -> payment with UPI, card, PayPal
- Observer -> order status notifications
- Decorator -> logging and security
- Adapter -> third-party shipping API
- Command -> cancel or undo order

## Why Patterns Matter

Patterns give names to common design ideas. They help teams discuss architecture clearly.

Use patterns to reduce coupling, improve testability, and organize changing behavior. Do not use patterns only to make code look advanced.

## Singleton: Database Connection

Singleton ensures only one shared instance exists.

```python
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connected = True
        return cls._instance


db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)
```

In real Python apps, dependency injection or connection pools are often better than a manual singleton.

## Factory: Create Product Types

Factory centralizes object creation.

```python
class Laptop:
    category = "laptop"


class Monitor:
    category = "monitor"


def product_factory(product_type):
    if product_type == "laptop":
        return Laptop()
    if product_type == "monitor":
        return Monitor()
    raise ValueError("Unknown product type")
```

Use factory when object creation depends on input, configuration, or product type.

## Strategy: Payment Methods

Strategy lets you swap algorithms or behavior at runtime.

```python
class UpiPayment:
    def pay(self, amount):
        return f"Paid {amount} using UPI"


class CardPayment:
    def pay(self, amount):
        return f"Paid {amount} using card"


class Checkout:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def pay(self, amount):
        return self.payment_strategy.pay(amount)
```

Use strategy when multiple implementations share the same behavior name, such as `pay()`.

## Observer: Order Status Notifications

Observer notifies many subscribers when something changes.

```python
class Order:
    def __init__(self):
        self._observers = []
        self.status = "created"

    def attach(self, observer):
        self._observers.append(observer)

    def set_status(self, status):
        self.status = status
        for observer in self._observers:
            observer.update(self)


class EmailNotifier:
    def update(self, order):
        print(f"Email: order is {order.status}")
```

Use observer for events such as order placed, shipped, delivered, or cancelled.

## Decorator: Logging and Security

Decorator adds behavior around a function without changing the function body.

```python
def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@log_action
def cancel_order(order_id):
    return f"Cancelled order {order_id}"
```

Use decorators for logging, authentication, authorization, timing, and validation.

## Adapter: Third-Party Shipping API

Adapter converts one interface into another expected interface.

```python
class ThirdPartyShippingAPI:
    def create_label(self, address):
        return f"Shipping label for {address}"


class ShippingAdapter:
    def __init__(self, api):
        self.api = api

    def ship(self, order):
        return self.api.create_label(order["address"])
```

Use adapter when your code expects `ship(order)` but a third-party API provides a different method name or payload shape.

## Command: Cancel or Undo Order

Command turns a request into an object.

```python
class CancelOrderCommand:
    def __init__(self, order):
        self.order = order
        self.previous_status = order["status"]

    def execute(self):
        self.order["status"] = "cancelled"

    def undo(self):
        self.order["status"] = self.previous_status
```

Use command for undo, retry, queues, transaction logs, and audit trails.

## Pattern Summary

| Pattern | Problem it solves |
|---------|-------------------|
| Singleton | one shared instance |
| Factory | object creation logic |
| Strategy | interchangeable behavior |
| Observer | notify subscribers |
| Decorator | add behavior around functions |
| Adapter | convert incompatible interfaces |
| Command | package actions for execute/undo |

## See also

- [Design patterns reference](design-patterns-reference.md)
- [Design patterns interview problems](interview-problems.md)
- [Design patterns FAQ](frequently-asked-questions.md)
- [Design principles](../design-principles/core-concepts.md)
- [Python OOP](../oop/core-concepts.md)
