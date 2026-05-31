# Python Design Principles Reference

## Quick Table

| Principle | Meaning | Python interview example |
|-----------|---------|--------------------------|
| SRP | one class, one main responsibility | separate `Order`, `OrderRepository`, `EmailService` |
| OCP | extend without modifying existing code | add a new discount class |
| LSP | subclass must behave like parent | every payment method supports `pay()` |
| ISP | small focused interfaces | separate printer and scanner behavior |
| DIP | depend on abstractions | inject notification service |
| DRY | avoid duplicated knowledge | one discount function |
| KISS | prefer simple readable code | simple shipping rule function |
| Composition | combine objects instead of deep inheritance | cart has a discount policy |

## SOLID Reference

### S: Single Responsibility Principle

One class should have one reason to change.

```python
class InvoiceCalculator:
    def total(self, items):
        return sum(item.price * item.quantity for item in items)
```

Do not mix total calculation, database save, and email sending in one class.

### O: Open/Closed Principle

Add new behavior with new code instead of changing stable code.

```python
class Discount:
    def apply(self, total):
        return total


class BulkOrderDiscount(Discount):
    def apply(self, total):
        return total * 0.85
```

### L: Liskov Substitution Principle

Child classes should be usable anywhere the parent is expected.

```python
def checkout(payment_method, amount):
    return payment_method.pay(amount)
```

Every payment method passed to `checkout()` should support `pay(amount)`.

### I: Interface Segregation Principle

Prefer small focused interfaces.

```python
class Refundable:
    def refund(self, amount):
        raise NotImplementedError


class Payable:
    def pay(self, amount):
        raise NotImplementedError
```

Not every payment provider must support refunds.

### D: Dependency Inversion Principle

High-level classes should not directly depend on low-level details.

```python
class OrderService:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def checkout(self, amount):
        return self.payment_gateway.pay(amount)
```

The gateway can be Stripe, PayPal, mock payment, or offline payment.

## DRY Reference

DRY removes duplicated rules.

```python
def tax_amount(total, tax_rate):
    return total * tax_rate / 100
```

If tax logic changes, update one function.

## KISS Reference

KISS favors simple direct solutions.

```python
def has_stock(stock_count):
    return stock_count > 0
```

Do not use patterns or inheritance unless they solve a real problem.

## Composition Over Inheritance Reference

Composition is usually easier to change than deep inheritance.

```python
class ShippingPolicy:
    def cost(self, total):
        return 0 if total >= 500 else 50


class Order:
    def __init__(self, shipping_policy):
        self.shipping_policy = shipping_policy

    def shipping_cost(self, total):
        return self.shipping_policy.cost(total)
```

## Common Comparisons

| Comparison | Key difference |
|------------|----------------|
| DRY vs KISS | DRY reduces duplication; KISS reduces unnecessary complexity |
| OCP vs DIP | OCP focuses on extension; DIP focuses on dependencies |
| Inheritance vs composition | inheritance is "is-a"; composition is "has-a" |
| SRP vs DRY | SRP separates responsibilities; DRY removes repeated knowledge |
| abstraction vs over-engineering | abstraction hides useful details; over-engineering adds unnecessary layers |

## Interview Warnings

- Do not say SOLID means "always use classes".
- Do not force inheritance when simple functions work.
- Do not remove all repetition if it makes code harder to read.
- Do not use metaclasses or advanced patterns for basic business rules.
- Explain trade-offs with examples.

## See also

- [Design principles: core concepts](core-concepts.md)
- [Design principles interview problems](interview-problems.md)
- [Design principles FAQ](frequently-asked-questions.md)
- [Composition relationships](../class-relationships/core-concepts.md)
