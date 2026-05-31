# Python Error Types: Core Concepts

Python errors are exceptions raised when code cannot continue normally. Knowing common error types helps in debugging, interviews, and writing clean `try` / `except` blocks.

In an online computer shopping system, errors may happen when:

- cart quantity is not a number
- product ID does not exist
- inventory list index is invalid
- discount division uses zero
- JSON payload is invalid
- a required module is missing
- a file path is wrong

## Error vs Exception

In Python, most runtime problems are represented as **exceptions**. An exception is an object that Python raises when something goes wrong.

```python
quantity = int("two")
```

This raises `ValueError` because `"two"` cannot be converted to an integer.

## Common Built-in Errors

| Error | Common reason |
|-------|---------------|
| `TypeError` | operation uses wrong type |
| `ValueError` | correct type, invalid value |
| `NameError` | variable name does not exist |
| `KeyError` | dictionary key is missing |
| `IndexError` | sequence index is out of range |
| `AttributeError` | object does not have an attribute |
| `ImportError` | import fails |
| `ModuleNotFoundError` | module cannot be found |
| `FileNotFoundError` | file path does not exist |
| `ZeroDivisionError` | division by zero |
| `SyntaxError` | invalid Python syntax |
| `IndentationError` | invalid indentation |

## `TypeError`

`TypeError` happens when an operation is applied to the wrong type.

```python
price = "999"
tax = 50

total = price + tax
```

Fix:

```python
price = "999"
tax = 50

total = int(price) + tax
print(total)
```

## `ValueError`

`ValueError` happens when the type is correct but the value is invalid.

```python
quantity = int("two")
```

Fix:

```python
try:
    quantity = int("two")
except ValueError:
    quantity = 1
```

## `KeyError`

`KeyError` happens when a dictionary key is missing.

```python
product = {"name": "Laptop"}
print(product["price"])
```

Fix:

```python
product = {"name": "Laptop"}
print(product.get("price", 0))
```

## `IndexError`

`IndexError` happens when a list, tuple, or string index is out of range.

```python
cart = ["laptop"]
print(cart[3])
```

## `AttributeError`

`AttributeError` happens when an object does not have the requested attribute or method.

```python
product = {"name": "Laptop"}
product.append("Mouse")
```

`append()` belongs to lists, not dictionaries.

## `NameError`

`NameError` happens when Python cannot find a variable name.

```python
print(total_price)
```

If `total_price` was never defined, Python raises `NameError`.

## Compile-Time Style Errors

Some errors happen before the program runs.

```python
if True
    print("Laptop")
```

This raises `SyntaxError`.

## Practice Problems

1. Cause and fix a `TypeError`.
2. Cause and fix a `ValueError`.
3. Use `.get()` to avoid `KeyError`.
4. Check list length before indexing to avoid `IndexError`.
5. Explain `ModuleNotFoundError` vs `ImportError`.

## See also

- [Python error types reference](error-types-reference.md)
- [Python error types interview problems](interview-problems.md)
- [Python error types FAQ](frequently-asked-questions.md)
- [Python exception handling](../exception-handling/core-concepts.md)
