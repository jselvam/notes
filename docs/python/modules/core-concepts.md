# Python Modules: Core Concepts

A **module** is a Python file (`.py`) that contains code such as functions, classes, constants, and variables. Modules help organize code into reusable files.

In an online computer shopping system, modules can separate:

- product logic
- cart calculations
- coupon validation
- payment helpers
- inventory utilities
- report generation

## What Is a Module?

Any Python file can be imported as a module.

```python
# cart_utils.py
def cart_total(prices):
    return sum(prices)
```

Use it from another file:

```python
import cart_utils

print(cart_utils.cart_total([999, 25]))
```

## Import Styles

```python
import math
from math import sqrt
import datetime as dt
from collections import Counter
```

## Built-in Modules

Python includes many standard library modules.

```python
import math
import datetime
import random
import json
```

## Custom Modules

Create a file and import it by filename without `.py`.

```python
# discounts.py
def apply_discount(price, percent):
    return price - price * percent / 100
```

```python
from discounts import apply_discount

print(apply_discount(1000, 10))
```

## Module Search Path

Python looks for modules in locations listed in `sys.path`.

```python
import sys

print(sys.path)
```

## `__name__ == "__main__"`

Use this block for code that should run only when the file is executed directly.

```python
def main():
    print("Run shopping script")


if __name__ == "__main__":
    main()
```

When imported, the `main()` block does not run.

## Packages

A package is a folder of modules.

```text
shopping/
  __init__.py
  cart.py
  products.py
  discounts.py
```

Import:

```python
from shopping.cart import cart_total
```

## Common Interview Points

### What is the difference between module and package?

A module is one Python file. A package is a directory containing modules.

### Why use modules?

They organize code, improve reuse, and reduce large files.

### What is `__name__ == "__main__"`?

It detects whether a file is run directly or imported.

## Practice Problems

1. Create a `cart_utils.py` module with `cart_total`.
2. Import `sqrt` from `math`.
3. Import `datetime` using an alias.
4. Explain when `__name__ == "__main__"` runs.
5. Create a package layout for a shopping app.

## See also

- [Python modules reference](module-reference.md)
- [Python modules interview problems](interview-problems.md)
- [Python modules FAQ](frequently-asked-questions.md)
- [Python functions: core concepts](../functions/core-concepts.md)
