# Python Operators: Core Concepts

Python **operators** are symbols or keywords that perform operations on values. They are heavily asked in interviews because they connect to arithmetic, conditions, identity, membership, bit manipulation, and short-circuit logic.

This section covers:

- arithmetic operators
- assignment operators
- comparison operators
- logical operators
- identity operators
- membership operators
- bitwise operators

Examples use an online computer shopping system: product prices, stock counts, carts, coupons, subscriptions, and permission flags.

## Operator Categories

| Category | Examples | Used for |
|----------|----------|----------|
| Arithmetic | `+`, `-`, `*`, `/`, `//`, `%`, `**` | totals, discounts, batches |
| Assignment | `=`, `+=`, `-=`, `*=`, `/=` | updating counters/state |
| Comparison | `==`, `!=`, `>`, `<`, `>=`, `<=` | validation and filtering |
| Logical | `and`, `or`, `not` | combining conditions |
| Identity | `is`, `is not` | checking `None` / same object |
| Membership | `in`, `not in` | cart/category lookup |
| Bitwise | `&`, `|`, `^`, `~`, `<<`, `>>` | flags, masks, low-level logic |

## Arithmetic Operators

```python
price = 1000
quantity = 2

print(price + 100)       # addition
print(price - 100)       # subtraction
print(price * quantity)  # multiplication
print(price / 3)         # true division
print(price // 3)        # floor division
print(price % 3)         # remainder
print(2 ** 3)            # power
```

### Interview Point

Know the difference between `/`, `//`, and `%`.

```python
print(10 / 3)   # 3.333...
print(10 // 3)  # 3
print(10 % 3)   # 1
```

## Assignment Operators

Assignment operators update variables.

```python
stock = 10

stock += 5
stock -= 2
stock *= 2

print(stock)
```

### Interview Point

Augmented assignment can mutate mutable objects in place.

```python
cart = ["laptop"]
same_cart = cart

cart += ["mouse"]

print(same_cart)
# ["laptop", "mouse"]
```

## Comparison Operators

Comparisons return booleans.

```python
price = 999

print(price == 999)
print(price != 25)
print(price > 100)
print(price <= 1000)
```

Python supports chained comparisons:

```python
price = 500

print(100 <= price <= 1000)
```

## Logical Operators

Use `and`, `or`, and `not` to combine conditions.

```python
is_logged_in = True
cart_has_items = True

if is_logged_in and cart_has_items:
    print("Allow checkout")
```

### Short-Circuiting

Python stops when the result is known.

```python
cart = []

if cart and cart[0] == "laptop":
    print("First item is laptop")
```

This avoids `IndexError` because `cart[0]` is skipped when `cart` is empty.

## Identity Operators

Use `is` and `is not` to check whether two references point to the same object.

```python
discount = None

if discount is None:
    print("No discount configured")
```

### Interview Point

Use `is None`, not `== None`.

```python
if discount is not None:
    print("Discount available")
```

## Membership Operators

Use `in` and `not in`.

```python
cart = ["laptop", "mouse"]

print("mouse" in cart)
print("monitor" not in cart)
```

Membership performance depends on the container:

- list: **O(n)**
- set: **O(1)** average
- dict keys: **O(1)** average

## Bitwise Operators

Bitwise operators work on integer bits.

```python
READ = 1      # 001
WRITE = 2     # 010
EXECUTE = 4   # 100

permission = READ | WRITE

print(permission & READ != 0)     # True
print(permission & EXECUTE != 0)  # False
```

### Interview Point

Bitwise operators are useful for flags, masks, permissions, parity tricks, and low-level interview problems.

## Operator Precedence

Precedence decides what runs first.

```python
result = 10 + 2 * 3
print(result)  # 16
```

Use parentheses for clarity:

```python
result = (10 + 2) * 3
print(result)  # 36
```

## Practice Problems

1. Calculate total price using arithmetic operators.
2. Update stock count using assignment operators.
3. Check if price is in a valid range using comparison operators.
4. Check checkout eligibility using logical operators.
5. Check optional discount with `is None`.
6. Check whether a product exists in cart using `in`.
7. Use bitwise flags for product permissions.

## See also

- [Python operator reference](operator-reference.md)
- [Python operator interview problems](interview-problems.md)
- [Python operator FAQ](frequently-asked-questions.md)
- [Python boolean operations](../bool/operations-and-truthiness.md)
