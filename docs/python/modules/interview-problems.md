# Python Modules Interview Problems

## 1. Create a Cart Utility Module

### Problem

Create a reusable module for cart total calculation.

```python
# cart_utils.py
def cart_total(prices):
    return sum(prices)
```

Usage:

```python
import cart_utils

print(cart_utils.cart_total([999, 25]))
```

## 2. Import Specific Function

```python
from math import sqrt

print(sqrt(81))
```

## 3. Import With Alias

```python
import datetime as dt

print(dt.date.today())
```

## 4. Use `__name__ == "__main__"`

```python
def main():
    print("Generate shopping report")


if __name__ == "__main__":
    main()
```

## 5. Build Package Layout

```text
shopping/
  __init__.py
  products.py
  cart.py
  discounts.py
```

Example import:

```python
from shopping.cart import cart_total
```

## 6. Avoid Circular Import

Bad shape:

```text
cart.py imports discounts.py
discounts.py imports cart.py
```

Better:

```text
pricing.py contains shared price helpers
cart.py imports pricing.py
discounts.py imports pricing.py
```

## 7. Read JSON Using Standard Module

```python
import json

data = '{"product": "laptop", "price": 999}'
product = json.loads(data)

print(product)
```

## 8. Count Items With `collections`

```python
from collections import Counter

cart = ["mouse", "mouse", "laptop"]
print(Counter(cart))
```

## Summary

| Pattern | Module idea |
|---------|-------------|
| Reuse code | custom module |
| Clear names | import module |
| Short alias | `import ... as ...` |
| Script entry | `__main__` guard |
| Organize app | package |
| Avoid tangled code | prevent circular imports |

## See also

- [Python modules: core concepts](core-concepts.md)
- [Python modules reference](module-reference.md)
- [Python modules FAQ](frequently-asked-questions.md)
