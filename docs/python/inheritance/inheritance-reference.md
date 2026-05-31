# Python Inheritance Reference

## Quick Table

| Term | Meaning | Example |
|------|---------|---------|
| Parent class | class being inherited from | `Product` |
| Child class | class that inherits | `DigitalProduct(Product)` |
| Base class | another name for parent | `Product` |
| Subclass | another name for child | `DigitalProduct` |
| Override | child replaces parent method | `delivery_type()` |
| `super()` | call parent/next class method | `super().__init__()` |
| `isinstance()` | object type check | `isinstance(obj, Product)` |
| `issubclass()` | class relationship check | `issubclass(DigitalProduct, Product)` |
| MRO | method lookup order | `ClassName.mro()` |

## Parent and Child Syntax

```python
class Product:
    pass


class DigitalProduct(Product):
    pass
```

## Inherit Parent Constructor

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class DigitalProduct(Product):
    pass
```

## Extend Parent Constructor With `super()`

```python
class PhysicalProduct(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight
```

## Override Method

```python
class Product:
    def delivery_type(self):
        return "shipping"


class DigitalProduct(Product):
    def delivery_type(self):
        return "download"
```

## Call Parent Method From Override

```python
class Product:
    def summary(self):
        return "Product summary"


class DigitalProduct(Product):
    def summary(self):
        return super().summary() + " with license key"
```

## `isinstance()`

```python
software = DigitalProduct("PDF Editor", 49.99)

print(isinstance(software, DigitalProduct))
print(isinstance(software, Product))
```

## `issubclass()`

```python
print(issubclass(DigitalProduct, Product))
```

## Multiple Inheritance

```python
class Downloadable:
    pass


class Licensed:
    pass


class SoftwareProduct(Downloadable, Licensed):
    pass
```

## MRO

```python
print(SoftwareProduct.mro())
```

Python uses MRO to decide which method to call when multiple parent classes define the same method.

## Common Comparisons

| Pair | Difference |
|------|------------|
| inheritance vs composition | is-a vs has-a |
| overriding vs overloading | child replacement vs same name with different signatures |
| `isinstance()` vs `type()` | inheritance-aware check vs exact type check |
| `super()` vs parent class name | MRO-aware call vs direct parent reference |
| single vs multiple inheritance | one parent vs multiple parents |

## See also

- [Python inheritance: core concepts](core-concepts.md)
- [Python inheritance interview problems](interview-problems.md)
- [Python inheritance FAQ](frequently-asked-questions.md)
