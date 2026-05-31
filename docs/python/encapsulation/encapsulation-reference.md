# Python Encapsulation Reference

## Quick Table

| Technique | Meaning | Example |
|-----------|---------|---------|
| public attribute | normal external access | `self.name` |
| protected/internal attribute | internal by convention | `self._price` |
| private-style attribute | name mangling | `self.__token` |
| getter method | controlled read | `get_price()` |
| setter method | controlled write | `set_price(value)` |
| `@property` | attribute-style getter | `product.price` |
| property setter | validated assignment | `@price.setter` |
| method-based update | protect business rule | `reserve(quantity)` |

## Public Attribute

```python
class Product:
    def __init__(self, name):
        self.name = name
```

Use public attributes for safe, simple data.

## Internal Attribute With `_`

```python
class Product:
    def __init__(self, price):
        self._price = price
```

The underscore says: "This is internal. Do not use directly unless you know why."

## Private-Style Attribute With `__`

```python
class Payment:
    def __init__(self, token):
        self.__token = token
```

Double underscore triggers name mangling.

## Getter and Setter Methods

```python
class Product:
    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self._price = price
```

## `@property`

```python
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
```

## Read-Only Property

```python
class Cart:
    def __init__(self, items):
        self._items = list(items)

    @property
    def item_count(self):
        return len(self._items)
```

No setter means `item_count` is read-only.

## Return Copies for Mutable Data

```python
class Cart:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    @property
    def items(self):
        return list(self._items)
```

Returning a copy prevents outside code from mutating the internal list directly.

## Common Comparisons

| Pair | Difference |
|------|------------|
| encapsulation vs abstraction | protect/control data vs hide implementation detail |
| `_name` vs `__name` | internal convention vs name mangling |
| getter/setter methods vs `@property` | method calls vs attribute-style access |
| public vs internal | supported external API vs implementation detail |
| direct assignment vs setter | no validation vs controlled validation |

## See also

- [Python encapsulation: core concepts](core-concepts.md)
- [Python encapsulation interview problems](interview-problems.md)
- [Python encapsulation FAQ](frequently-asked-questions.md)
