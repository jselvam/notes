# Python Encapsulation Interview Problems

## 1. Protect Product Price

### Problem

Prevent product price from becoming negative.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value


product = Product("Laptop", 999.99)
product.price = 899.99
print(product.price)
```

**Complexity:** `O(1)` time and space.

## 2. Make Stock Read-Only

```python
class InventoryItem:
    def __init__(self, name, stock):
        self.name = name
        self._stock = stock

    @property
    def stock(self):
        return self._stock


item = InventoryItem("Mouse", 10)
print(item.stock)
```

Outside code can read stock but should not directly modify `_stock`.

## 3. Reserve Stock Through a Method

```python
class InventoryItem:
    def __init__(self, name, stock):
        self.name = name
        self._stock = stock

    def reserve(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if quantity > self._stock:
            return False
        self._stock -= quantity
        return True

    @property
    def stock(self):
        return self._stock


item = InventoryItem("Keyboard", 5)
print(item.reserve(2))
print(item.stock)
```

## 4. Return Copy of Cart Items

```python
class Cart:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    @property
    def items(self):
        return list(self._items)


cart = Cart()
cart.add_item("Laptop")
external_items = cart.items
external_items.append("Mouse")

print(cart.items)
```

The cart's internal list is protected from external mutation.

## 5. Validate Coupon Code Assignment

```python
class Coupon:
    def __init__(self, code):
        self.code = code

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        value = value.strip().upper()
        if len(value) < 4:
            raise ValueError("Coupon code is too short")
        self._code = value


coupon = Coupon(" save10 ")
print(coupon.code)
```

## 6. Hide Payment Token With Name Mangling

```python
class Payment:
    def __init__(self, token):
        self.__token = token

    def masked_token(self):
        return "****" + self.__token[-4:]


payment = Payment("tok_123456789")
print(payment.masked_token())
```

Double underscore reduces accidental access.

## 7. Encapsulate Cart Total

```python
class Cart:
    def __init__(self, prices):
        self._prices = list(prices)

    @property
    def total(self):
        return sum(self._prices)


cart = Cart([999.99, 25.00])
print(cart.total)
```

## 8. Use Method Instead of Direct Status Change

```python
class Order:
    def __init__(self):
        self._status = "created"

    @property
    def status(self):
        return self._status

    def mark_paid(self):
        if self._status != "created":
            raise ValueError("Only created orders can be marked paid")
        self._status = "paid"


order = Order()
order.mark_paid()
print(order.status)
```

## Summary

| Problem pattern | Encapsulation idea |
|-----------------|--------------------|
| negative price | property setter validation |
| stock protection | read-only property |
| stock update rules | method-based mutation |
| cart item protection | return copy |
| payment token hiding | double underscore |
| order status rules | controlled method |

## See also

- [Python encapsulation: core concepts](core-concepts.md)
- [Python encapsulation reference](encapsulation-reference.md)
- [Python encapsulation FAQ](frequently-asked-questions.md)
