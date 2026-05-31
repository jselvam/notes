# Python Design Patterns Reference

## Quick Reference

| Pattern | Category | Shopping-system example | Main benefit |
|---------|----------|-------------------------|--------------|
| Singleton | creational | database connection | one shared instance |
| Factory | creational | product type creation | hide object creation logic |
| Strategy | behavioral | UPI, card, PayPal payment | switch behavior easily |
| Observer | behavioral | order status notifications | notify many listeners |
| Decorator | structural/function pattern | logging and security | add behavior without editing target |
| Adapter | structural | shipping API wrapper | make incompatible APIs usable |
| Command | behavioral | cancel/undo order | represent action as object |

## Singleton Reference

```python
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### Use When

- a shared object should exist once
- setup is expensive
- repeated creation may cause inconsistent state

### Be Careful

Singleton can hide dependencies and make tests harder. Prefer explicit dependency injection when possible.

## Factory Reference

```python
class ProductFactory:
    @staticmethod
    def create(product_type):
        products = {
            "laptop": Laptop,
            "mouse": Mouse,
            "monitor": Monitor,
        }
        try:
            return products[product_type]()
        except KeyError:
            raise ValueError("Unknown product type")
```

### Use When

- object type depends on input
- creation logic is repeated
- calling code should not know concrete classes

## Strategy Reference

```python
class PayPalPayment:
    def pay(self, amount):
        return f"Paid {amount} by PayPal"


class Checkout:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def complete_payment(self, amount):
        return self.payment_strategy.pay(amount)
```

### Use When

- different algorithms share the same operation
- behavior should change at runtime
- long `if/elif` chains choose behavior

## Observer Reference

```python
class SmsNotifier:
    def update(self, order):
        print(f"SMS: order status changed to {order.status}")
```

### Use When

- many objects need to react to an event
- subject should not know all concrete subscribers
- event notifications may grow over time

## Decorator Reference

```python
def require_admin(func):
    def wrapper(user, *args, **kwargs):
        if user["role"] != "admin":
            raise PermissionError("Admin required")
        return func(user, *args, **kwargs)
    return wrapper
```

### Use When

- add logging, security, validation, caching, or timing
- behavior wraps a function or method
- core business logic should stay clean

## Adapter Reference

```python
class ShippingAdapter:
    def __init__(self, third_party_api):
        self.third_party_api = third_party_api

    def ship(self, order):
        payload = {"to": order["address"], "weight": order["weight"]}
        return self.third_party_api.create_shipment(payload)
```

### Use When

- third-party API has different method names
- third-party payload shape differs from your domain model
- you want to isolate external API changes

## Command Reference

```python
class CommandHistory:
    def __init__(self):
        self.commands = []

    def run(self, command):
        command.execute()
        self.commands.append(command)

    def undo_last(self):
        command = self.commands.pop()
        command.undo()
```

### Use When

- actions need undo
- commands must be queued or retried
- actions need audit logs
- UI actions map to backend operations

## Common Comparisons

| Comparison | Difference |
|------------|------------|
| Factory vs Strategy | factory creates objects; strategy uses interchangeable behavior |
| Strategy vs State | strategy is selected behavior; state changes behavior based on internal state |
| Decorator pattern vs Python decorator | Python decorator syntax is a common way to implement wrapping behavior |
| Adapter vs Facade | adapter changes interface; facade simplifies a complex subsystem |
| Command vs function call | command stores the action and can support undo, queue, retry, or logging |
| Singleton vs global variable | singleton controls instance creation; globals are simple shared names |

## Interview Warning

Do not just define a pattern. Explain the problem, show the code shape, and mention the trade-off.

## See also

- [Design patterns: core concepts](core-concepts.md)
- [Design patterns interview problems](interview-problems.md)
- [Design patterns FAQ](frequently-asked-questions.md)
- [Design principles](../design-principles/core-concepts.md)
