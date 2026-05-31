# Python Inheritance Interview Problems

## 1. Create Product and DigitalProduct

### Problem

Create a child class that reuses parent product behavior.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def label(self):
        return f"{self.name}: ${self.price:.2f}"


class DigitalProduct(Product):
    pass


product = DigitalProduct("PDF Editor", 49.99)
print(product.label())
```

**Complexity:** `O(1)` time and space per object.

## 2. Add Child-Specific Method

```python
class DigitalProduct(Product):
    def download_link(self):
        return f"/downloads/{self.name.lower().replace(' ', '-')}"


software = DigitalProduct("Office Suite", 99.99)
print(software.download_link())
```

## 3. Override Delivery Type

```python
class Product:
    def delivery_type(self):
        return "standard shipping"


class DigitalProduct(Product):
    def delivery_type(self):
        return "email download link"


print(DigitalProduct().delivery_type())
```

## 4. Use `super()` in Child Constructor

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class PhysicalProduct(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight


monitor = PhysicalProduct("Monitor", 199.99, 2.5)
print(monitor.name)
print(monitor.weight)
```

## 5. Use `super()` in Overridden Method

```python
class Product:
    def summary(self):
        return "Product"


class SubscriptionProduct(Product):
    def summary(self):
        return super().summary() + " with monthly renewal"


print(SubscriptionProduct().summary())
```

## 6. Use `isinstance()`

```python
software = DigitalProduct("Antivirus", 29.99)

print(isinstance(software, DigitalProduct))
print(isinstance(software, Product))
```

## 7. Use `issubclass()`

```python
print(issubclass(DigitalProduct, Product))
```

## 8. Multiple Inheritance for Software Product

```python
class Downloadable:
    def download(self):
        return "Download started"


class Licensed:
    def license_key(self):
        return "LICENSE-123"


class SoftwareProduct(Downloadable, Licensed):
    pass


software = SoftwareProduct()
print(software.download())
print(software.license_key())
```

## 9. Inspect MRO

```python
print(SoftwareProduct.mro())
```

Use MRO to understand method lookup order.

## 10. Choose Composition Over Inheritance

```python
class Cart:
    def __init__(self, items):
        self.items = items


class Order:
    def __init__(self, order_id, cart):
        self.order_id = order_id
        self.cart = cart
```

`Order` has a `Cart`, so composition is clearer than inheritance.

## Summary

| Problem pattern | Inheritance idea |
|-----------------|------------------|
| digital product | child class |
| shared product behavior | parent class |
| custom delivery | method override |
| shared initialization | `super().__init__()` |
| type relationship | `isinstance()`, `issubclass()` |
| multiple capabilities | multiple inheritance |
| has-a relationship | composition |

## See also

- [Python inheritance: core concepts](core-concepts.md)
- [Python inheritance reference](inheritance-reference.md)
- [Python inheritance FAQ](frequently-asked-questions.md)
