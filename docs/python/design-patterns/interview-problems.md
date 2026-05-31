# Python Design Patterns Interview Problems

## 1. Implement Singleton for Database Connection

### Problem

Create one shared database connection object.

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

### Interview Point

Singleton controls instance creation, but dependency injection is often easier to test.

## 2. Create Product Types With Factory

```python
class Laptop:
    def label(self):
        return "Laptop"


class Mouse:
    def label(self):
        return "Mouse"


class ProductFactory:
    @staticmethod
    def create(product_type):
        mapping = {"laptop": Laptop, "mouse": Mouse}
        if product_type not in mapping:
            raise ValueError("Unknown product type")
        return mapping[product_type]()


product = ProductFactory.create("laptop")
print(product.label())
```

### Complexity

Dictionary lookup is average `O(1)`.

## 3. Implement Strategy for Payments

```python
class UpiPayment:
    def pay(self, amount):
        return f"Paid {amount} with UPI"


class CardPayment:
    def pay(self, amount):
        return f"Paid {amount} with card"


class PayPalPayment:
    def pay(self, amount):
        return f"Paid {amount} with PayPal"


class Checkout:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def pay(self, amount):
        return self.payment_strategy.pay(amount)
```

### Interview Point

Strategy replaces long payment-method conditionals.

## 4. Implement Observer for Order Status

```python
class Order:
    def __init__(self):
        self.status = "created"
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def change_status(self, status):
        self.status = status
        for observer in self.observers:
            observer.update(self)


class EmailNotifier:
    def update(self, order):
        print(f"Email: {order.status}")


class SmsNotifier:
    def update(self, order):
        print(f"SMS: {order.status}")
```

## 5. Add Logging With Decorator

```python
def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@log_action
def place_order(order_id):
    return f"Placed order {order_id}"
```

## 6. Add Security With Decorator

```python
def require_admin(func):
    def wrapper(user, *args, **kwargs):
        if user.get("role") != "admin":
            raise PermissionError("Admin required")
        return func(user, *args, **kwargs)
    return wrapper


@require_admin
def cancel_any_order(user, order_id):
    return f"Cancelled order {order_id}"
```

## 7. Adapt a Third-Party Shipping API

```python
class ThirdPartyShippingAPI:
    def create_label(self, destination):
        return f"Label created for {destination}"


class ShippingAdapter:
    def __init__(self, api):
        self.api = api

    def ship(self, order):
        return self.api.create_label(order["address"])
```

### Interview Point

Adapter protects your application from third-party interface changes.

## 8. Implement Command for Cancel Order

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

## 9. Build Command History for Undo

```python
class CommandHistory:
    def __init__(self):
        self.history = []

    def execute(self, command):
        command.execute()
        self.history.append(command)

    def undo_last(self):
        if self.history:
            self.history.pop().undo()
```

## 10. Choose the Right Pattern

### Problem

Which pattern fits each case?

| Scenario | Pattern |
|----------|---------|
| one database connection | Singleton |
| create laptop/mouse/monitor objects | Factory |
| choose UPI/card/PayPal | Strategy |
| notify email/SMS/push | Observer |
| add logging/security | Decorator |
| wrap shipping provider | Adapter |
| cancel and undo order | Command |

## Summary

In interviews, first explain the changing part of the system, then choose the pattern that isolates that change.

## See also

- [Design patterns: core concepts](core-concepts.md)
- [Design patterns reference](design-patterns-reference.md)
- [Design patterns FAQ](frequently-asked-questions.md)
