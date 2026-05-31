# Python Control Flow Reference: Interview Notes

This page is a quick reference for Python conditions, loops, and pattern matching.

## Quick Table

| Construct | Purpose | Example use |
|-----------|---------|-------------|
| `if` | Run block when condition is true | Valid checkout |
| `elif` | Additional condition | Price category |
| `else` | Fallback block | Out of stock |
| `for` | Iterate over iterable | Cart items |
| `while` | Repeat while condition is true | Retry / countdown |
| `break` | Exit loop | Stop when found |
| `continue` | Skip iteration | Skip out-of-stock |
| `pass` | Placeholder | TODO block |
| loop `else` | Runs if no `break` | Not found |
| `match` | Pattern matching | Order event routing |

## `if` / `elif` / `else`

```python
price = 999

if price >= 1000:
    label = "premium"
elif price >= 100:
    label = "standard"
else:
    label = "budget"
```

## Nested `if`

```python
is_logged_in = True
cart_items = ["laptop"]

if is_logged_in:
    if cart_items:
        print("Checkout allowed")
```

Prefer combining conditions when it improves readability.

```python
if is_logged_in and cart_items:
    print("Checkout allowed")
```

## `for` Loop

```python
for item in ["laptop", "mouse"]:
    print(item)
```

## `for` With `range()`

```python
for number in range(1, 4):
    print(number)
```

## `for` With `enumerate()`

```python
cart = ["laptop", "mouse"]

for index, item in enumerate(cart):
    print(index, item)
```

## `for` With Dictionary

```python
prices = {"laptop": 999, "mouse": 25}

for product, price in prices.items():
    print(product, price)
```

## `while` Loop

```python
stock = 3

while stock > 0:
    print("sell")
    stock -= 1
```

## `break`

```python
for product in ["mouse", "laptop", "monitor"]:
    if product == "laptop":
        break
```

## `continue`

```python
for stock in [5, 0, 3]:
    if stock == 0:
        continue
    print(stock)
```

## `pass`

```python
def todo():
    pass
```

## Loop `else`

```python
products = ["mouse", "keyboard"]

for product in products:
    if product == "laptop":
        print("found")
        break
else:
    print("not found")
```

## `match` / `case`

```python
status = "paid"

match status:
    case "pending":
        action = "wait"
    case "paid":
        action = "ship"
    case _:
        action = "manual-review"
```

## Pattern Matching With Lists

```python
command = ["add", "laptop"]

match command:
    case ["add", product]:
        print(f"Add {product}")
    case ["remove", product]:
        print(f"Remove {product}")
    case _:
        print("Unknown command")
```

## Pattern Matching With Guards

```python
product = {"name": "laptop", "price": 999}

match product:
    case {"name": name, "price": price} if price >= 500:
        print(f"Premium product: {name}")
    case _:
        print("Other product")
```

## Common Interview Questions

### Does loop `else` run after `break`?

No. It runs only if the loop completes without `break`.

### What is `_` in `match`?

`_` is the wildcard fallback pattern.

### What is a guard in `match`?

A guard is an `if` condition attached to a `case`.

## See also

- [Python control-flow core concepts](core-concepts.md)
- [Python control-flow interview problems](interview-problems.md)
- [Python control-flow FAQ](frequently-asked-questions.md)
