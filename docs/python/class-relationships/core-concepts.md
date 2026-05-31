# Python Relationships Between Classes: Core Concepts

Classes often work together. In OOP, common relationships between classes are **association**, **aggregation**, and **composition**.

In an online computer shopping system, these relationships appear between:

- `Customer` and `Order`
- `Order` and `Cart`
- `Cart` and `Product`
- `Order` and `Payment`
- `Warehouse` and `InventoryItem`

## Relationship Summary

| Relationship | Meaning | Object lifetime |
|--------------|---------|-----------------|
| Association | one class uses or knows another | independent |
| Aggregation | one class has another, but child can live alone | independent child |
| Composition | one class owns another strongly | child depends on owner |

## Association

Association means one class is connected to or uses another class.

Example: a `Customer` places an `Order`.

```python
class Customer:
    def __init__(self, name):
        self.name = name


class Order:
    def __init__(self, order_id):
        self.order_id = order_id


def place_order(customer, order):
    return f"{customer.name} placed order {order.order_id}"


customer = Customer("Selvam")
order = Order("ORD-501")

print(place_order(customer, order))
```

The `Customer` and `Order` can exist separately.

## Aggregation

Aggregation is a **has-a** relationship where the contained object can exist independently.

Example: a `Cart` has `Product` objects, but products can exist without that cart.

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

The `Product` object can exist before, during, and after the `Cart`.

## Composition

Composition is a stronger **has-a** relationship. The owning object creates and controls the lifetime of the contained object.

Example: an `Order` creates its own `Payment` record.

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

Here, `Payment` is part of the `Order` design and is created inside `Order`.

## Association vs Aggregation vs Composition

```text
Association: Customer uses Order
Aggregation: Cart has Products
Composition: Order owns Payment
```

## Choosing the Right Relationship

Ask these questions:

1. Does one object only use another temporarily? Use association.
2. Does one object contain another, but the child can live independently? Use aggregation.
3. Does one object own another and control its lifecycle? Use composition.

## Common Gotchas

### Do not force inheritance

`Order` should not inherit from `Cart`. An order has a cart or cart items.

### Composition is often clearer than inheritance

Use composition when one object contains another.

### Lifetime matters

If the child object can exist independently, aggregation is usually a better description than composition.

## Practice Problems

1. Model `Customer` and `Order` with association.
2. Model `Cart` and `Product` with aggregation.
3. Model `Order` and `Payment` with composition.
4. Explain why `Order` should not inherit from `Cart`.
5. Identify the relationship between `Warehouse` and `InventoryItem`.

## See also

- [Python class relationships reference](class-relationships-reference.md)
- [Python class relationships interview problems](interview-problems.md)
- [Python class relationships FAQ](frequently-asked-questions.md)
- [Python inheritance](../inheritance/core-concepts.md)
