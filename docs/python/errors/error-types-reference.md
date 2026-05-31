# Python Error Types Reference

## Quick Reference Table

| Error type | Meaning | Example cause | Common fix |
|------------|---------|---------------|------------|
| `TypeError` | wrong type | `"999" + 50` | convert or validate type |
| `ValueError` | invalid value | `int("two")` | validate value |
| `NameError` | name not defined | `print(total)` before assignment | define variable |
| `UnboundLocalError` | local variable used before assignment | assign inside branch only | initialize first |
| `KeyError` | missing dictionary key | `product["price"]` | use `.get()` or check key |
| `IndexError` | invalid sequence index | `cart[10]` | check length |
| `AttributeError` | missing attribute/method | `dict.append()` | use correct object/method |
| `ImportError` | import failed | bad imported name | check package/module |
| `ModuleNotFoundError` | module missing | `import fake_module` | install or fix import |
| `FileNotFoundError` | file missing | `open("x.txt")` | check path |
| `PermissionError` | insufficient permission | write protected file | change permissions/path |
| `ZeroDivisionError` | divide by zero | `price / 0` | guard denominator |
| `OverflowError` | numeric result too large | huge numeric operation | limit range |
| `RecursionError` | recursion too deep | missing base case | add base case |
| `StopIteration` | iterator exhausted | `next(empty_iterator)` | use default or handle |
| `AssertionError` | assertion failed | `assert total > 0` | fix condition/data |
| `SyntaxError` | invalid syntax | missing colon | fix code syntax |
| `IndentationError` | bad indentation | uneven block indent | fix indentation |
| `TabError` | mixed tabs/spaces | inconsistent indentation | use spaces consistently |

## `TypeError`

```python
price = "999"
tax = 50

try:
    print(price + tax)
except TypeError as error:
    print(error)
```

## `ValueError`

```python
try:
    quantity = int("two")
except ValueError:
    quantity = 1
```

## `KeyError`

```python
product = {"name": "Laptop"}

try:
    print(product["price"])
except KeyError:
    print("Price missing")
```

## `IndexError`

```python
cart = ["laptop"]

if len(cart) > 2:
    print(cart[2])
else:
    print("Cart does not have item at index 2")
```

## `AttributeError`

```python
product = {"name": "Laptop"}

try:
    product.append("Mouse")
except AttributeError:
    print("Dictionaries do not support append")
```

## `FileNotFoundError`

```python
try:
    with open("products.csv", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("Products file not found")
```

## `ModuleNotFoundError`

```python
try:
    import fake_payment_sdk
except ModuleNotFoundError:
    print("Install the package or fix the module name")
```

## `ZeroDivisionError`

```python
orders = 0
revenue = 1000

if orders != 0:
    average = revenue / orders
else:
    average = 0
```

## `RecursionError`

```python
def count_down(n):
    if n == 0:
        return
    return count_down(n - 1)
```

Always include a base case in recursive functions.

## Common Interview Comparisons

| Pair | Difference |
|------|------------|
| `TypeError` vs `ValueError` | wrong type vs invalid value |
| `KeyError` vs `IndexError` | missing dict key vs invalid sequence index |
| `ImportError` vs `ModuleNotFoundError` | import problem vs module not found |
| `SyntaxError` vs runtime error | code cannot parse vs code fails while running |
| `NameError` vs `AttributeError` | missing variable name vs missing object attribute |

## See also

- [Python error types: core concepts](core-concepts.md)
- [Python error types interview problems](interview-problems.md)
- [Python error types FAQ](frequently-asked-questions.md)
