# Python Polymorphism: Core Concepts

Polymorphism means **many forms**. In OOP, it allows different objects to use the same method name or operation while each object provides its own behavior.

In an online computer shopping system, polymorphism helps with:

- different payment methods using `pay()`
- different product types using `delivery_message()`
- different notification senders using `send()`
- different discounts using `apply()`
- different objects working with Python functions such as `len()` or operators such as `+`

## Simple Polymorphism

Different classes can define the same method name.

```python
class CardPayment:
    def pay(self, amount):
        return f"Paid ${amount:.2f} by card"


class UPIPayment:
    def pay(self, amount):
        return f"Paid ${amount:.2f} by UPI"
```

Both classes have `pay()`, but each implementation is different.

## Polymorphic Function

```python
def checkout(payment_method, amount):
    return payment_method.pay(amount)


print(checkout(CardPayment(), 999.99))
print(checkout(UPIPayment(), 999.99))
```

The `checkout()` function depends on behavior, not the exact class.

## Method Overriding

Polymorphism often appears through inheritance and method overriding.

```python
class Product:
    def delivery_message(self):
        return "Standard delivery"


class DigitalProduct(Product):
    def delivery_message(self):
        return "Download link sent by email"


class PhysicalProduct(Product):
    def delivery_message(self):
        return "Product shipped by courier"
```

## Duck Typing

Python often uses duck typing: if an object has the needed method, it can be used.

```python
class WalletPayment:
    def pay(self, amount):
        return f"Paid ${amount:.2f} using wallet"


def checkout(payment_method, amount):
    return payment_method.pay(amount)


print(checkout(WalletPayment(), 100))
```

`WalletPayment` does not need to inherit from a parent class. It only needs a compatible `pay()` method.

## Built-in Polymorphism

The same function can work differently for different types.

```python
print(len("laptop"))
print(len(["laptop", "mouse"]))
print(len({"name": "Laptop", "price": 999}))
```

`len()` works on strings, lists, and dictionaries.

## Operator Polymorphism

The `+` operator behaves differently depending on the object type.

```python
print(10 + 20)
print("lap" + "top")
print([1, 2] + [3, 4])
```

Custom classes can support operators with dunder methods such as `__add__`.

## Why Polymorphism Matters

Polymorphism makes code flexible.

```python
payment_methods = [CardPayment(), UPIPayment(), WalletPayment()]

for payment_method in payment_methods:
    print(payment_method.pay(500))
```

New payment types can be added without rewriting the loop.

## Common Gotchas

### Same method name should mean same idea

If several classes use `pay()`, each method should represent payment behavior.

### Do not force inheritance when duck typing is enough

In Python, compatible behavior is often enough.

### Polymorphism is not only inheritance

It can come from duck typing, built-in functions, operators, and dunder methods.

## Practice Problems

1. Create `CardPayment`, `UPIPayment`, and `WalletPayment` with `pay()`.
2. Write a `checkout()` function that accepts any payment object.
3. Create product classes that override `delivery_message()`.
4. Show how `len()` is polymorphic.
5. Explain duck typing with a shopping example.

## See also

- [Python polymorphism reference](polymorphism-reference.md)
- [Python polymorphism interview problems](interview-problems.md)
- [Python polymorphism FAQ](frequently-asked-questions.md)
- [Python inheritance](../inheritance/core-concepts.md)
