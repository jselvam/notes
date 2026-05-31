# Python Class Properties and self Reference

## Quick Table

| Topic | Meaning | Example |
|-------|---------|---------|
| `self` | current object | `self.name = name` |
| Instance property | per-object data | `self.price` |
| Class property | shared class data | `currency = "USD"` |
| Instance method | method that receives `self` | `def label(self):` |
| `@property` | computed attribute | `product.formatted_price` |
| setter | controlled assignment | `@price.setter` |
| internal attribute | convention for internal data | `self._price` |

## Instance Properties

```python
class Product:
    def __init__(self, product_id, name):
        self.product_id = product_id
        self.name = name
```

Each object gets its own `product_id` and `name`.

## Class Properties

```python
class Product:
    category = "computer"

    def __init__(self, name):
        self.name = name
```

All `Product` objects can access `category`.

## Access Class Property

```python
print(Product.category)
```

Access through an object also works:

```python
product = Product("Laptop")
print(product.category)
```

## Change Instance Property

```python
product = Product("Laptop")
product.name = "Gaming Laptop"
```

## Instance Method Uses `self`

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def final_price(self, discount):
        return self.price - (self.price * discount / 100)
```

## `@property`

```python
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def formatted_price(self):
        return f"${self.price:.2f}"
```

## Setter

```python
class InventoryItem:
    def __init__(self, stock):
        self.stock = stock

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError("Stock cannot be negative")
        self._stock = value
```

## Read-Only Property

If a property has no setter, it is read-only from normal assignment.

```python
class Cart:
    def __init__(self, items):
        self.items = items

    @property
    def item_count(self):
        return len(self.items)
```

## Common Comparisons

| Pair | Difference |
|------|------------|
| instance property vs class property | per-object vs shared |
| method vs property | action call vs attribute-style computed value |
| `self.price` vs local `price` | object state vs temporary variable |
| `_price` vs `price` | internal storage vs public property |
| read-only property vs setter property | computed only vs controlled update |

## See also

- [Python class properties and self: core concepts](core-concepts.md)
- [Python class properties and self interview problems](interview-problems.md)
- [Python class properties and self FAQ](frequently-asked-questions.md)
