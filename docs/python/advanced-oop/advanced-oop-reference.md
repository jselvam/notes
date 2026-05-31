# Python Advanced OOP Reference

## Quick Table

| Concept | Meaning | Example |
|---------|---------|---------|
| MRO | method lookup order | `ClassName.mro()` |
| Diamond Problem | multiple paths to same parent | `A -> B, C -> D` |
| Mixin | small reusable behavior class | `DiscountMixin` |
| Nested class | class inside another class | `Order.Status` |
| Dynamic attribute | attribute added at runtime | `product.name = "Laptop"` |
| Introspection | inspect objects at runtime | `type(obj)` |
| `type()` | exact object type | `type(product)` |
| `isinstance()` | object is instance/subclass | `isinstance(obj, Product)` |
| `issubclass()` | class relationship check | `issubclass(DigitalProduct, Product)` |

## MRO

```python
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D.mro())
```

Python uses C3 linearization to create a consistent method lookup order.

## Diamond Problem

```python
class Product:
    def source(self):
        return "Product"


class Downloadable(Product):
    def source(self):
        return "Downloadable"


class Licensed(Product):
    def source(self):
        return "Licensed"


class SoftwareProduct(Downloadable, Licensed):
    pass


print(SoftwareProduct().source())
print(SoftwareProduct.mro())
```

## Mixin Pattern

```python
class JsonMixin:
    def to_dict(self):
        return self.__dict__.copy()


class Product(JsonMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price
```

Mixins should usually be small and focused.

## Nested Class Pattern

```python
class Order:
    class Status:
        CREATED = "created"
        PAID = "paid"

    def __init__(self):
        self.status = self.Status.CREATED
```

## Dynamic Attributes

```python
class Product:
    pass


product = Product()
setattr(product, "name", "Laptop")

print(getattr(product, "name"))
```

Useful helpers:

```python
hasattr(product, "name")
getattr(product, "name", None)
setattr(product, "price", 999)
```

## Introspection Helpers

```python
print(type(product))
print(dir(product))
print(product.__dict__)
```

## `type()` vs `isinstance()`

```python
class Product:
    pass


class DigitalProduct(Product):
    pass


software = DigitalProduct()

print(type(software) is Product)
print(isinstance(software, Product))
```

`isinstance()` respects inheritance. Exact `type()` checks do not.

## Common Comparisons

| Pair | Difference |
|------|------------|
| MRO vs inheritance | MRO is lookup order; inheritance is relationship |
| mixin vs parent class | mixin adds capability; parent often models identity |
| nested class vs normal class | nested class is scoped inside another class |
| dynamic attribute vs declared in `__init__` | runtime flexibility vs predictable object shape |
| `type()` vs `isinstance()` | exact type vs inheritance-aware check |
| `isinstance()` vs `issubclass()` | object check vs class check |

## See also

- [Python advanced OOP: core concepts](core-concepts.md)
- [Python advanced OOP interview problems](interview-problems.md)
- [Python advanced OOP FAQ](frequently-asked-questions.md)
