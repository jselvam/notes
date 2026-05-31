# Python Numeric Types: `int`, `float`, and `complex`

Python has three main built-in numeric types:

- **`int`** — whole numbers
- **`float`** — decimal numbers
- **`complex`** — numbers with real and imaginary parts

In an online computer shopping management system, numeric types are used for:

- product quantity: `int`
- product IDs / order IDs: `int`
- price, tax, discount: `float` or `Decimal`
- ratings and percentages: `float`
- analytics or signal/math problems: `complex`

## `int`

`int` stores whole numbers with unlimited precision, limited only by memory.

```python
product_id = 101
quantity = 3
stock_count = 25

print(type(quantity))  # <class 'int'>
```

### Common `int` use cases

```python
cart_quantity = 2
available_stock = 10

can_add_to_cart = cart_quantity <= available_stock
print(can_add_to_cart)
```

## `float`

`float` stores decimal values using binary floating-point representation.

```python
price = 999.99
tax_rate = 0.08
discount_percent = 10.5

print(type(price))  # <class 'float'>
```

### Common `float` use cases

```python
price = 999.99
tax = price * 0.08
total = price + tax

print(total)
```

## Important Float Warning

Floats can have precision issues.

```python
print(0.1 + 0.2)
# 0.30000000000000004
```

For money calculations, prefer `decimal.Decimal`.

```python
from decimal import Decimal

price = Decimal("999.99")
tax = Decimal("0.08")

print(price + (price * tax))
```

## `complex`

`complex` stores numbers with a real and imaginary part.

```python
signal = 3 + 4j

print(signal.real)  # 3.0
print(signal.imag)  # 4.0
```

Complex numbers are less common in business apps but can appear in math, engineering, data science, signal processing, or advanced interview questions.

## Creating Numbers

```python
quantity = int("5")
price = float("999.99")
signal = complex(3, 4)

print(quantity)
print(price)
print(signal)
```

## Type Conversion

```python
print(int(9.99))       # 9
print(float(10))       # 10.0
print(complex(10))     # (10+0j)
```

`int()` truncates toward zero; it does not round.

```python
print(int(9.99))   # 9
print(int(-9.99))  # -9
```

## Arithmetic Operators

```python
price = 100
quantity = 3

print(price + 20)       # addition
print(price - 20)       # subtraction
print(price * quantity) # multiplication
print(price / 3)        # true division
print(price // 3)       # floor division
print(price % 3)        # modulo
print(2 ** 3)           # exponent
```

## Division Results

`/` always returns a float.

```python
print(10 / 2)   # 5.0
print(10 // 2)  # 5
```

`//` is floor division, not simple truncation.

```python
print(7 // 2)    # 3
print(-7 // 2)   # -4
```

## Rounding

```python
price = 999.987

print(round(price, 2))  # 999.99
```

Be careful: `round()` follows banker's rounding in tie cases.

```python
print(round(2.5))  # 2
print(round(3.5))  # 4
```

## Truthiness

Zero values are falsey. Non-zero values are truthy.

```python
print(bool(0))       # False
print(bool(0.0))     # False
print(bool(0j))      # False
print(bool(10))      # True
```

## Common Interview Points

### What is the difference between `int` and `float`?

`int` stores whole numbers. `float` stores decimal approximations.

### Why should floats be avoided for exact money calculations?

Binary floating-point cannot exactly represent many decimal fractions.

### What is `complex` used for?

Complex numbers are used in mathematical domains like signal processing, electrical engineering, and scientific computing.

## Practice Problems

1. Calculate cart total from price and quantity.
2. Apply tax and discount to a price.
3. Check whether stock count is enough for an order quantity.
4. Convert string inputs to numbers safely.
5. Round a final price to two decimals.
6. Explain why `0.1 + 0.2` is not exactly `0.3`.
7. Extract real and imaginary parts from a complex number.

## See also

- [Python numeric operations](operations-and-methods.md)
- [Python numeric interview problems](interview-problems.md)
- [Python numeric FAQ](frequently-asked-questions.md)
- [Python functions: core concepts](../functions/core-concepts.md)
