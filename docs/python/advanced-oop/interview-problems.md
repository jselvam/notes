# Python Advanced OOP Interview Problems

## 1. Print Method Resolution Order

### Problem

Create multiple inheritance and print MRO.

```python
class Product:
    pass


class Downloadable(Product):
    pass


class Licensed(Product):
    pass


class SoftwareProduct(Downloadable, Licensed):
    pass


print(SoftwareProduct.mro())
```

**Complexity:** `O(k)` time where `k` is the inheritance chain length.

## 2. Solve Diamond Problem With MRO

```python
class Product:
    def info(self):
        return "Product"


class Downloadable(Product):
    def info(self):
        return "Downloadable"


class Licensed(Product):
    def info(self):
        return "Licensed"


class SoftwareProduct(Downloadable, Licensed):
    pass


print(SoftwareProduct().info())
print(SoftwareProduct.mro())
```

Python chooses `Downloadable.info()` because of MRO.

## 3. Use `super()` With MRO

```python
class Product:
    def setup(self):
        return ["product"]


class Downloadable(Product):
    def setup(self):
        return super().setup() + ["downloadable"]


class Licensed(Product):
    def setup(self):
        return super().setup() + ["licensed"]


class SoftwareProduct(Downloadable, Licensed):
    pass


print(SoftwareProduct().setup())
```

`super()` follows MRO, not just the immediate parent name.

## 4. Create Discount Mixin

```python
class DiscountMixin:
    def apply_discount(self, price, percent):
        return price - (price * percent / 100)


class Product(DiscountMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price


product = Product("Laptop", 1000)
print(product.apply_discount(product.price, 10))
```

## 5. Create JSON Mixin

```python
class JsonMixin:
    def to_dict(self):
        return self.__dict__.copy()


class Product(JsonMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price


print(Product("Mouse", 25).to_dict())
```

## 6. Use Nested Class for Order Status

```python
class Order:
    class Status:
        CREATED = "created"
        PAID = "paid"
        SHIPPED = "shipped"

    def __init__(self, order_id):
        self.order_id = order_id
        self.status = self.Status.CREATED


order = Order("ORD-501")
print(order.status)
```

## 7. Add Dynamic Attributes

```python
class Product:
    pass


product = Product()
setattr(product, "name", "Keyboard")
setattr(product, "price", 75)

print(product.__dict__)
```

## 8. Use `getattr()` With Default

```python
class Product:
    pass


product = Product()
print(getattr(product, "stock", 0))
```

This avoids `AttributeError` when the attribute is missing.

## 9. Compare `type()` and `isinstance()`

```python
class Product:
    pass


class DigitalProduct(Product):
    pass


software = DigitalProduct()

print(type(software) is Product)
print(isinstance(software, Product))
```

Use `isinstance()` when inheritance should count.

## 10. Use `issubclass()`

```python
print(issubclass(DigitalProduct, Product))
print(issubclass(Product, DigitalProduct))
```

## Summary

| Problem pattern | Advanced OOP concept |
|-----------------|----------------------|
| method lookup | MRO |
| multiple parent paths | diamond problem |
| cooperative parent calls | `super()` |
| reusable small capability | mixin |
| scoped helper class | nested class |
| runtime fields | dynamic attributes |
| object inspection | `type()`, `isinstance()` |
| class inspection | `issubclass()` |

## See also

- [Python advanced OOP: core concepts](core-concepts.md)
- [Python advanced OOP reference](advanced-oop-reference.md)
- [Python advanced OOP FAQ](frequently-asked-questions.md)
