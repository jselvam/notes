# Python Class Relationships Interview Problems

## 1. Model Association Between Customer and Order

### Problem

A customer places an order, but both objects can exist independently.

```python
class Customer:
    def __init__(self, name):
        self.name = name


class Order:
    def __init__(self, order_id):
        self.order_id = order_id


def place_order(customer, order):
    return f"{customer.name} placed {order.order_id}"


customer = Customer("Selvam")
order = Order("ORD-501")

print(place_order(customer, order))
```

**Relationship:** Association  
**Complexity:** `O(1)` time and space.

## 2. Model Aggregation Between Cart and Product

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)


laptop = Product("Laptop", 999.99)
cart = Cart()
cart.add_product(laptop)
```

`Product` can exist without `Cart`, so this is aggregation.

## 3. Model Composition Between Order and Payment

```python
class Payment:
    def __init__(self, amount):
        self.amount = amount
        self.status = "pending"


class Order:
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.payment = Payment(amount)


order = Order("ORD-501", 999.99)
print(order.payment.status)
```

`Order` creates and owns its `Payment`.

## 4. Model Wishlist and Product

```python
class Wishlist:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)
```

This is aggregation because products can exist outside the wishlist.

## 5. Model Order and Shipping Address

```python
class ShippingAddress:
    def __init__(self, city, pincode):
        self.city = city
        self.pincode = pincode


class Order:
    def __init__(self, order_id, city, pincode):
        self.order_id = order_id
        self.shipping_address = ShippingAddress(city, pincode)
```

This is composition when the address object belongs specifically to that order.

## 6. Avoid Wrong Inheritance

Bad:

```python
class Order(Cart):
    pass
```

Better:

```python
class Order:
    def __init__(self, cart):
        self.cart = cart
```

An order is not a cart. An order has a cart.

## 7. Warehouse and Inventory Items

```python
class InventoryItem:
    def __init__(self, sku, stock):
        self.sku = sku
        self.stock = stock


class Warehouse:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
```

This can be aggregation if inventory items can move between warehouses or exist independently.

## 8. Composition With Internal Line Items

```python
class OrderLine:
    def __init__(self, product_name, quantity):
        self.product_name = product_name
        self.quantity = quantity


class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.lines = []

    def add_line(self, product_name, quantity):
        self.lines.append(OrderLine(product_name, quantity))
```

`OrderLine` belongs to the order, so this is composition.

## Summary

| Scenario | Best relationship |
|----------|-------------------|
| Customer places order | Association |
| Cart contains product references | Aggregation |
| Wishlist contains products | Aggregation |
| Order creates payment | Composition |
| Order creates order lines | Composition |
| Order uses cart | Composition or aggregation depending ownership |
| DigitalProduct extends Product | Inheritance |

## See also

- [Python class relationships: core concepts](core-concepts.md)
- [Python class relationships reference](class-relationships-reference.md)
- [Python class relationships FAQ](frequently-asked-questions.md)
