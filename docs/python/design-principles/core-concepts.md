# Python Design Principles: Core Concepts

Design principles help you write Python code that is easier to understand, test, change, and explain in interviews.

This page covers:

- SOLID principles
- DRY: Don't Repeat Yourself
- KISS: Keep It Simple, Stupid
- Composition over inheritance

Examples use an online computer shopping system.

## Why Design Principles Matter

In interviews, design principles show that you can think beyond syntax. They help answer questions like:

- How do you organize code?
- How do you reduce bugs?
- How do you make code easier to extend?
- How do you avoid over-engineering?

## SOLID Principles

SOLID is a group of five object-oriented design principles.

| Letter | Principle | Main idea |
|--------|-----------|-----------|
| S | Single Responsibility Principle | one class should have one reason to change |
| O | Open/Closed Principle | open for extension, closed for modification |
| L | Liskov Substitution Principle | subclasses should work wherever parent classes are expected |
| I | Interface Segregation Principle | avoid forcing classes to implement unused behavior |
| D | Dependency Inversion Principle | depend on abstractions, not concrete details |

## Single Responsibility Principle

A class should focus on one job.

Bad design:

```python
class Order:
    def calculate_total(self):
        pass

    def save_to_database(self):
        pass

    def send_email(self):
        pass
```

Better design:

```python
class Order:
    def calculate_total(self):
        pass


class OrderRepository:
    def save(self, order):
        pass


class EmailService:
    def send_confirmation(self, order):
        pass
```

Now pricing, database storage, and email logic can change independently.

## Open/Closed Principle

Code should be extendable without editing tested existing code.

```python
class Discount:
    def apply(self, total):
        return total


class StudentDiscount(Discount):
    def apply(self, total):
        return total * 0.9


class FestivalDiscount(Discount):
    def apply(self, total):
        return total * 0.8
```

New discounts can be added as new classes.

## Liskov Substitution Principle

A subclass should not break expectations of the parent class.

```python
class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError


class CardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} by card"
```

Any `PaymentMethod` should support `pay(amount)` in a meaningful way.

## Interface Segregation Principle

Do not force a class to depend on methods it does not need.

Bad idea:

```python
class Machine:
    def print_invoice(self):
        pass

    def scan_invoice(self):
        pass
```

A simple receipt printer should not need `scan_invoice()`.

Better:

```python
class Printer:
    def print_invoice(self):
        pass


class Scanner:
    def scan_invoice(self):
        pass
```

## Dependency Inversion Principle

High-level logic should depend on abstractions.

```python
class NotificationService:
    def send(self, message):
        raise NotImplementedError


class EmailNotification(NotificationService):
    def send(self, message):
        print(f"Email: {message}")


class OrderProcessor:
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def place_order(self):
        self.notification_service.send("Order placed")
```

`OrderProcessor` does not care whether the notification is email, SMS, or push.

## DRY

DRY means **Don't Repeat Yourself**. Avoid copying the same logic in many places.

Repeated code:

```python
laptop_total = 1000 - (1000 * 0.1)
mouse_total = 50 - (50 * 0.1)
```

DRY code:

```python
def apply_discount(price, discount_percent):
    return price - (price * discount_percent / 100)
```

## KISS

KISS means **Keep It Simple, Stupid**. Prefer simple code that solves the real problem.

```python
def is_free_shipping(total):
    return total >= 500
```

Do not create complex class hierarchies for simple rules.

## Composition Over Inheritance

Composition means building objects by combining smaller objects.

```python
class DiscountPolicy:
    def apply(self, total):
        return total * 0.9


class Cart:
    def __init__(self, discount_policy):
        self.discount_policy = discount_policy

    def final_total(self, total):
        return self.discount_policy.apply(total)
```

The cart has a discount policy instead of inheriting from many discount-specific cart classes.

## Common Interview Summary

- Use SRP to keep classes focused.
- Use OCP to add new behavior without editing old code.
- Use LSP so subclasses remain compatible.
- Use ISP to avoid large, forced interfaces.
- Use DIP to depend on abstractions.
- Use DRY to remove duplicated knowledge.
- Use KISS to avoid unnecessary complexity.
- Use composition when behavior changes independently.

## See also

- [Design principles reference](design-principles-reference.md)
- [Design principles interview problems](interview-problems.md)
- [Design principles FAQ](frequently-asked-questions.md)
- [Python OOP](../oop/core-concepts.md)
- [Class relationships](../class-relationships/core-concepts.md)
