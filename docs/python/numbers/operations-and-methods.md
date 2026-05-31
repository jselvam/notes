# Python Numeric Operations & Methods: Interview Notes

Python numbers are objects, but numeric interview questions usually focus on **operators**, **conversion**, **rounding**, **precision**, and built-in functions.

## Quick Table

| Operation / Function | What it does | Interview use case |
|----------------------|--------------|--------------------|
| `+`, `-`, `*` | Basic arithmetic | Cart total |
| `/` | True division | Average price |
| `//` | Floor division | Pages/batches |
| `%` | Remainder | Even/odd, cyclic logic |
| `**` | Power | Growth/math |
| `abs()` | Absolute value | Difference between prices |
| `round()` | Round number | Display price |
| `int()` | Convert/truncate | Quantity input |
| `float()` | Convert decimal | Price input |
| `complex()` | Create complex number | Math/signal questions |
| `divmod()` | Quotient and remainder | Pagination/batches |
| `pow()` | Power, optional modulo | Modular arithmetic |

## Addition, Subtraction, Multiplication

```python
price = 999
shipping = 25
quantity = 2

print(price + shipping)
print(price - 100)
print(price * quantity)
```

## True Division `/`

Always returns a float.

```python
total = 999
items = 2

print(total / items)
# 499.5
```

## Floor Division `//`

Returns the floor result.

```python
orders = 25
batch_size = 10

print(orders // batch_size)
# 2
```

### Interview Point

Floor division with negative numbers may surprise beginners.

```python
print(-7 // 2)
# -4
```

## Modulo `%`

Returns the remainder.

```python
order_id = 105

if order_id % 2 == 0:
    print("even")
else:
    print("odd")
```

### Interview Point

Modulo is useful for even/odd checks, circular arrays, and repeating cycles.

## Power `**`

```python
print(2 ** 3)
# 8
```

## `abs()`

Returns absolute value.

```python
old_price = 999
new_price = 899

print(abs(new_price - old_price))
# 100
```

## `round()`

Rounds a number.

```python
price = 999.987

print(round(price, 2))
# 999.99
```

### Interview Point

`round()` uses banker's rounding for `.5` ties.

```python
print(round(2.5))  # 2
print(round(3.5))  # 4
```

## `int()`

Converts to integer or truncates decimals toward zero.

```python
print(int("10"))
print(int(9.99))    # 9
print(int(-9.99))   # -9
```

## `float()`

Converts to float.

```python
print(float("999.99"))
print(float(10))
```

## `complex()`

Creates a complex number.

```python
signal = complex(3, 4)

print(signal)
print(signal.real)
print(signal.imag)
```

## `divmod()`

Returns quotient and remainder as a tuple.

```python
orders = 25
batch_size = 10

full_batches, remaining = divmod(orders, batch_size)

print(full_batches)  # 2
print(remaining)     # 5
```

## `pow()`

```python
print(pow(2, 3))
# 8
```

With modulo:

```python
print(pow(2, 3, 5))
# (2 ** 3) % 5 => 3
```

### Interview Point

`pow(base, exp, mod)` is useful in modular arithmetic problems.

## Numeric Methods

Numbers have some methods, but interviews usually ask fewer method-specific questions than with lists or dictionaries.

### `int.bit_length()`

Returns number of bits needed to represent the integer.

```python
print((10).bit_length())
# 4 because 10 is 1010 in binary
```

### `float.is_integer()`

Checks whether a float has no fractional part.

```python
print((10.0).is_integer())  # True
print((10.5).is_integer())  # False
```

### `complex.conjugate()`

Returns complex conjugate.

```python
z = 3 + 4j

print(z.conjugate())
# (3-4j)
```

## Decimal for Money

Use `Decimal` for exact decimal money calculations.

```python
from decimal import Decimal

price = Decimal("999.99")
tax_rate = Decimal("0.08")

total = price + (price * tax_rate)
print(total)
```

## Common Interview Questions

### What is the difference between `/` and `//`?

`/` returns true division as float. `//` returns floor division.

### What is the difference between `int()` and `round()`?

`int()` truncates toward zero. `round()` rounds to nearest based on Python's rules.

### Why is modulo useful?

Modulo helps with remainders, even/odd checks, wrapping indexes, and cyclic patterns.

### Why use `Decimal` for money?

`Decimal` avoids many binary floating-point precision surprises.

## Practice Problems

1. Calculate total price using quantity.
2. Use `divmod()` to split orders into batches.
3. Check if an order ID is even or odd.
4. Round a display price to two decimals.
5. Use `Decimal` to calculate tax.
6. Use modulo to rotate through warehouse IDs.
7. Check whether a float is mathematically an integer.
8. Extract real and imaginary parts from a complex value.

## See also

- [Python numeric core concepts](core-concepts.md)
- [Python numeric interview problems](interview-problems.md)
- [Python numeric FAQ](frequently-asked-questions.md)
