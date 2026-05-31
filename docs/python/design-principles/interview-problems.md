# Python Design Principles Interview Problems

## 1. Refactor a Class Using SRP

### Problem

An `Order` class calculates totals, saves to a database, and sends emails. Refactor it.

### Solution

```python
class Order:
    def __init__(self, items):
        self.items = items

    def total(self):
        return sum(item["price"] * item["quantity"] for item in self.items)


class OrderRepository:
    def save(self, order):
        print("Order saved")


class EmailService:
    def send_confirmation(self, order):
        print(f"Order total: {order.total()}")
```

### Interview Point

SRP makes each class easier to test and change.

## 2. Add Discounts Using OCP

### Problem

Support multiple discount types without editing checkout logic.

### Solution

```python
class Discount:
    def apply(self, total):
        return total


class FestivalDiscount(Discount):
    def apply(self, total):
        return total * 0.8


class StudentDiscount(Discount):
    def apply(self, total):
        return total * 0.9


def checkout(total, discount):
    return discount.apply(total)
```

### Complexity

`O(1)` per discount calculation.

## 3. Identify an LSP Violation

### Problem

Why is this a bad subclass?

```python
class PaymentMethod:
    def pay(self, amount):
        pass


class CashOnDelivery(PaymentMethod):
    def pay(self, amount):
        raise NotImplementedError("Pay later")
```

### Answer

If client code expects every `PaymentMethod` to support `pay(amount)`, `CashOnDelivery` breaks that expectation.

## 4. Split a Fat Interface Using ISP

### Problem

Separate printer and scanner behavior.

### Solution

```python
class Printer:
    def print_invoice(self):
        raise NotImplementedError


class Scanner:
    def scan_invoice(self):
        raise NotImplementedError


class ReceiptPrinter(Printer):
    def print_invoice(self):
        print("Printing receipt")
```

### Interview Point

Classes should not implement methods they do not need.

## 5. Apply DIP to Notification Logic

### Problem

Make `OrderProcessor` independent of email-specific logic.

### Solution

```python
class OrderProcessor:
    def __init__(self, notifier):
        self.notifier = notifier

    def place_order(self):
        self.notifier.send("Order placed")


class EmailNotifier:
    def send(self, message):
        print(f"Email: {message}")
```

### Interview Point

Inject dependencies instead of creating concrete services inside high-level logic.

## 6. Remove Repeated Discount Logic Using DRY

```python
def apply_discount(price, percent):
    return price - (price * percent / 100)


prices = [1000, 50, 120]
discounted = [apply_discount(price, 10) for price in prices]
print(discounted)
```

DRY keeps one source of truth for discount calculation.

## 7. Keep a Rule Simple Using KISS

```python
def qualifies_for_free_shipping(total):
    return total >= 500
```

This does not need a class hierarchy unless shipping rules become complex.

## 8. Replace Inheritance With Composition

### Problem

Avoid `FestivalDiscountCart`, `StudentDiscountCart`, and `BulkDiscountCart`.

### Solution

```python
class Cart:
    def __init__(self, discount_policy):
        self.discount_policy = discount_policy

    def final_total(self, total):
        return self.discount_policy.apply(total)
```

### Interview Point

Composition lets behavior change at runtime.

## 9. Choose Between DRY and Readability

### Answer

Do not create an abstraction just because two lines look similar. Use DRY when the same business rule or knowledge is repeated.

## 10. Explain SOLID in One Shopping Example

### Answer

Use separate classes for order calculation, payment, notification, persistence, and discounts. Then inject dependencies so checkout can use different payment and notification implementations without rewriting checkout logic.

## Summary

| Problem | Principle |
|---------|-----------|
| split order responsibilities | SRP |
| add discounts safely | OCP |
| avoid broken subclasses | LSP |
| split large interfaces | ISP |
| inject services | DIP |
| remove repeated rules | DRY |
| avoid unnecessary patterns | KISS |
| prefer has-a behavior | composition |

## See also

- [Design principles: core concepts](core-concepts.md)
- [Design principles reference](design-principles-reference.md)
- [Design principles FAQ](frequently-asked-questions.md)
