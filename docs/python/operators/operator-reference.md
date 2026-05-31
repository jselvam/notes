# Python Operator Reference: Interview Notes

This page is a quick reference for Python operator categories with examples and interview points.

## Arithmetic Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `+` | Addition | `price + tax` |
| `-` | Subtraction | `price - discount` |
| `*` | Multiplication | `price * quantity` |
| `/` | True division | `total / count` |
| `//` | Floor division | `orders // batch_size` |
| `%` | Modulo / remainder | `order_id % 2` |
| `**` | Power | `2 ** 3` |

```python
price = 999
quantity = 2

print(price * quantity)
print(price % 2)
```

## Assignment Operators

| Operator | Meaning |
|----------|---------|
| `=` | Assign |
| `+=` | Add and assign |
| `-=` | Subtract and assign |
| `*=` | Multiply and assign |
| `/=` | Divide and assign |
| `//=` | Floor divide and assign |
| `%=` | Modulo and assign |
| `**=` | Power and assign |
| `&=`, `|=`, `^=` | Bitwise update |
| `<<=`, `>>=` | Shift update |

```python
stock = 10
stock += 5
stock -= 2
print(stock)
```

## Comparison Operators

| Operator | Meaning |
|----------|---------|
| `==` | Equal |
| `!=` | Not equal |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |

```python
price = 500

print(price == 500)
print(100 <= price <= 1000)
```

## Logical Operators

| Operator | Meaning |
|----------|---------|
| `and` | Both conditions |
| `or` | At least one condition |
| `not` | Negation |

```python
is_logged_in = True
has_cart = True

print(is_logged_in and has_cart)
```

### Important Return Behavior

`and` and `or` return operands, not always booleans.

```python
print("laptop" and "mouse")  # mouse
print("" or "default")       # default
```

## Identity Operators

| Operator | Meaning |
|----------|---------|
| `is` | Same object |
| `is not` | Different object |

```python
discount = None

print(discount is None)
```

### Interview Point

Use `is None` for `None` checks. Use `==` for value equality.

## Membership Operators

| Operator | Meaning |
|----------|---------|
| `in` | Exists in container |
| `not in` | Does not exist in container |

```python
cart = ["laptop", "mouse"]

print("mouse" in cart)
```

For dictionaries, `in` checks keys.

```python
prices = {"laptop": 999}

print("laptop" in prices)
print(999 in prices)  # False
```

## Bitwise Operators

| Operator | Meaning |
|----------|---------|
| `&` | Bitwise AND |
| `|` | Bitwise OR |
| `^` | Bitwise XOR |
| `~` | Bitwise NOT |
| `<<` | Left shift |
| `>>` | Right shift |

```python
READ = 1
WRITE = 2
EXECUTE = 4

permission = READ | WRITE

print(permission & READ != 0)
print(permission & EXECUTE != 0)
```

## Common Precedence Tips

1. Parentheses run first.
2. `**` has high precedence.
3. `*`, `/`, `//`, `%` happen before `+`, `-`.
4. Comparisons happen before logical `and` / `or`.
5. `not` happens before `and`, and `and` before `or`.

```python
print(True or False and False)
# True because and happens before or
```

Use parentheses when in doubt.

## Common Interview Questions

### What is the difference between `/` and `//`?

`/` returns true division as a float. `//` returns floor division.

### What is the difference between `==` and `is`?

`==` compares values. `is` compares object identity.

### What does `in` check in a dictionary?

It checks keys, not values.

### What is bitwise AND used for?

It is commonly used to test flags or check if a bit is set.

## See also

- [Python operators: core concepts](core-concepts.md)
- [Python operator interview problems](interview-problems.md)
- [Python operator FAQ](frequently-asked-questions.md)
