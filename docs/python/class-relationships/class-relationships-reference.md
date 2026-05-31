# Python Class Relationships Reference

## Quick Table

| Relationship | Simple phrase | Example | Lifetime |
|--------------|---------------|---------|----------|
| Association | uses-a | `Customer` places `Order` | both independent |
| Aggregation | has-a, weak ownership | `Cart` has `Product` | child independent |
| Composition | owns-a, strong ownership | `Order` owns `Payment` | child tied to owner |
| Inheritance | is-a | `DigitalProduct` is a `Product` | class hierarchy |

## Association Pattern

Association is often represented by passing one object to a method or function.

```python
class Customer:
    def __init__(self, name):
        self.name = name


class SupportTicket:
    def __init__(self, ticket_id):
        self.ticket_id = ticket_id


def assign_ticket(customer, ticket):
    return f"Ticket {ticket.ticket_id} assigned to {customer.name}"
```

## Aggregation Pattern

Aggregation stores references to existing objects.

```python
class Product:
    def __init__(self, name):
        self.name = name


class Wishlist:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
```

The `Product` object is created outside and passed in.

## Composition Pattern

Composition creates contained objects inside the owner.

```python
class ShippingAddress:
    def __init__(self, city):
        self.city = city


class Order:
    def __init__(self, order_id, city):
        self.order_id = order_id
        self.shipping_address = ShippingAddress(city)
```

The `Order` creates its own `ShippingAddress`.

## Inheritance vs Composition

Inheritance:

```python
class DigitalProduct(Product):
    pass
```

Composition:

```python
class Order:
    def __init__(self, payment):
        self.payment = payment
```

Use inheritance for **is-a** relationships. Use composition for **has-a** relationships.

## Relationship Decision Table

| Question | Likely relationship |
|----------|---------------------|
| Does class A only use class B? | Association |
| Does class A contain class B but B can live alone? | Aggregation |
| Does class A create and own class B? | Composition |
| Is class A a special type of class B? | Inheritance |

## Common Examples

| Classes | Relationship |
|---------|--------------|
| `Customer` and `Order` | Association |
| `Cart` and `Product` | Aggregation |
| `Wishlist` and `Product` | Aggregation |
| `Order` and `Payment` | Composition |
| `Order` and `ShippingAddress` | Composition |
| `DigitalProduct` and `Product` | Inheritance |
| `Warehouse` and `InventoryItem` | Aggregation or composition depending on ownership |

## Common Interview Comparisons

| Pair | Difference |
|------|------------|
| association vs aggregation | uses-a vs weak has-a |
| aggregation vs composition | independent child vs owner-controlled child |
| composition vs inheritance | has-a vs is-a |
| association vs dependency | association is a structural relationship; dependency can be temporary usage |

## See also

- [Python class relationships: core concepts](core-concepts.md)
- [Python class relationships interview problems](interview-problems.md)
- [Python class relationships FAQ](frequently-asked-questions.md)
