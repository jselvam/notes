# Python Modules Reference: Interview Notes

## Quick Table

| Syntax | Meaning |
|--------|---------|
| `import module` | Import whole module |
| `import module as alias` | Import with shorter name |
| `from module import name` | Import one object |
| `from module import *` | Import all public names; usually avoid |
| `python file.py` | Run file directly |
| `__name__ == "__main__"` | Direct-run guard |

## Import Whole Module

```python
import math

print(math.sqrt(16))
```

## Import Specific Name

```python
from math import sqrt

print(sqrt(16))
```

## Import With Alias

```python
import datetime as dt

print(dt.date.today())
```

## Avoid Star Imports

```python
from math import *
```

Avoid this in production code because it hides where names come from.

## Standard Library Examples

```python
import json
import random
from datetime import datetime
from collections import Counter
```

## `__name__`

```python
print(__name__)
```

If the file is run directly, `__name__` is `"__main__"`. If imported, it is the module name.

## `sys.path`

```python
import sys

for path in sys.path:
    print(path)
```

## `__init__.py`

`__init__.py` marks a directory as a package in traditional Python package layouts.

```text
shopping/
  __init__.py
  cart.py
```

## Common Interview Questions

### What is import caching?

Python loads a module once and stores it in `sys.modules`.

### What is circular import?

Two modules import each other in a way that can break initialization.

### What is a package?

A directory of modules.

## See also

- [Python modules: core concepts](core-concepts.md)
- [Python modules interview problems](interview-problems.md)
- [Python modules FAQ](frequently-asked-questions.md)
