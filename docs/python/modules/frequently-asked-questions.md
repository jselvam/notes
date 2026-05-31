# Python Modules: Frequently Asked Interview Questions

## Basic Level

### 1. What is a module?

A module is a Python file containing reusable code.

### 2. What file extension does a Python module use?

`.py`.

### 3. How do you import a module?

```python
import math
```

### 4. How do you import a function from a module?

```python
from math import sqrt
```

### 5. How do you import with alias?

```python
import datetime as dt
```

### 6. What is the standard library?

Python's built-in collection of modules.

### 7. What is a custom module?

A module you create in your own project.

### 8. What is a package?

A directory that groups modules.

### 9. What is `__init__.py`?

A file used in packages, especially traditional package layouts.

### 10. Why use modules?

To organize code and reuse functionality.

## Intermediate Level

### 11. What is `__name__`?

A special variable holding the module name.

### 12. What is `__name__ == "__main__"`?

A guard that runs code only when the file is executed directly.

### 13. What is `sys.path`?

The list of paths Python searches for imports.

### 14. What is `sys.modules`?

A cache of loaded modules.

### 15. Does Python import a module every time?

No. It reuses the cached module from `sys.modules`.

### 16. What is a circular import?

Two modules depend on each other during import.

### 17. Why are circular imports bad?

They can cause partially initialized modules and import errors.

### 18. How do you avoid circular imports?

Move shared code to a third module or restructure dependencies.

### 19. Why avoid `from module import *`?

It hides where names come from and can cause name conflicts.

### 20. What is an absolute import?

An import using the full package path.

## Advanced Level

### 21. What is a relative import?

An import relative to the current package.

```python
from .cart import cart_total
```

### 22. Where should imports be placed?

Usually at the top of the file.

### 23. When is local import useful?

To avoid optional dependencies, reduce startup cost, or break circular imports carefully.

### 24. What is module namespace?

The set of names defined inside a module.

### 25. What is `dir(module)`?

It lists names available in a module.

### 26. What is `help(module)`?

It shows documentation for a module.

### 27. What is a third-party module?

A module installed from outside the standard library, often via `pip`.

### 28. What is `pip`?

Python's package installer.

### 29. What is `requirements.txt`?

A file listing project dependencies.

### 30. What should you remember?

Modules organize code, packages group modules, imports should be clear, and `__main__` protects script-only code.

## See also

- [Python modules: core concepts](core-concepts.md)
- [Python modules reference](module-reference.md)
- [Python modules interview problems](interview-problems.md)
