# Python Numeric Types: Frequently Asked Interview Questions

This page collects frequently asked Python numeric interview questions for `int`, `float`, and `complex` from **basic** to **pro** level.

## Basic Level

### 1. What are Python's main numeric types?

Python has `int`, `float`, and `complex`.

```python
quantity = 10
price = 99.99
signal = 3 + 4j
```

### 2. What is `int`?

`int` stores whole numbers.

```python
stock = 25
```

### 3. What is `float`?

`float` stores decimal numbers using binary floating-point representation.

```python
price = 999.99
```

### 4. What is `complex`?

`complex` stores real and imaginary parts.

```python
z = 3 + 4j
```

### 5. How do you check a numeric type?

Use `type()`.

```python
print(type(10))
print(type(10.5))
print(type(3 + 4j))
```

### 6. How do you convert string to int?

Use `int()`.

```python
quantity = int("5")
```

### 7. How do you convert string to float?

Use `float()`.

```python
price = float("999.99")
```

### 8. How do you create a complex number?

Use `a + bj` or `complex(a, b)`.

```python
z = complex(3, 4)
```

### 9. What does `/` return?

`/` returns true division as a float.

```python
print(10 / 2)  # 5.0
```

### 10. What does `//` return?

`//` returns floor division.

```python
print(10 // 3)  # 3
```

### 11. What does `%` return?

Modulo returns the remainder.

```python
print(10 % 3)  # 1
```

### 12. What does `**` do?

It performs exponentiation.

```python
print(2 ** 3)  # 8
```

### 13. How do you round a number?

Use `round()`.

```python
print(round(999.987, 2))
```

### 14. How do you get absolute value?

Use `abs()`.

```python
print(abs(-100))
```

### 15. What numeric values are falsey?

Zero values are falsey.

```python
print(bool(0), bool(0.0), bool(0j))
```

## Intermediate Level

### 16. What is the difference between `int()` and `round()`?

`int()` truncates toward zero. `round()` rounds to nearest according to Python's rounding rules.

```python
print(int(9.99))
print(round(9.99))
```

### 17. What is surprising about floor division with negative numbers?

It floors toward negative infinity.

```python
print(-7 // 2)  # -4
```

### 18. How do you check even or odd?

Use modulo.

```python
print(105 % 2 == 0)
```

### 19. How do you get quotient and remainder together?

Use `divmod()`.

```python
print(divmod(25, 10))
```

### 20. What is `pow()`?

`pow(a, b)` calculates `a ** b`.

```python
print(pow(2, 3))
```

### 21. What is three-argument `pow()`?

`pow(a, b, mod)` calculates `(a ** b) % mod` efficiently.

```python
print(pow(2, 3, 5))
```

### 22. How do you get real and imaginary parts?

Use `.real` and `.imag`.

```python
z = 3 + 4j
print(z.real, z.imag)
```

### 23. What is complex conjugate?

It changes the sign of the imaginary part.

```python
z = 3 + 4j
print(z.conjugate())
```

### 24. What is `float.is_integer()`?

It checks if a float has no fractional part.

```python
print((10.0).is_integer())
```

### 25. What is `int.bit_length()`?

It returns how many bits are needed to represent an integer.

```python
print((10).bit_length())
```

### 26. What happens when you mix `int` and `float`?

The result is usually a float.

```python
print(10 + 2.5)
```

### 27. What happens when you mix real and complex numbers?

The result becomes complex.

```python
print(10 + (3 + 4j))
```

### 28. Can Python integers overflow?

Python `int` has arbitrary precision, limited by memory.

```python
print(10 ** 100)
```

### 29. Can floats overflow?

Very large float operations can overflow.

```python
# Very large float calculations can raise OverflowError or become inf.
```

### 30. What is `math.isclose()`?

It compares floats with tolerance.

```python
import math

print(math.isclose(0.1 + 0.2, 0.3))
```

## Advanced Level

### 31. Why is `0.1 + 0.2 != 0.3` exactly?

Many decimals cannot be represented exactly in binary floating-point.

```python
print(0.1 + 0.2)
```

### 32. How should you compare floats?

Use a tolerance, often with `math.isclose()`.

```python
import math

print(math.isclose(0.1 + 0.2, 0.3))
```

### 33. Why use `Decimal` for money?

`Decimal` gives exact decimal arithmetic when constructed from strings.

```python
from decimal import Decimal

print(Decimal("0.1") + Decimal("0.2"))
```

### 34. Why should you avoid `Decimal(0.1)`?

It imports the existing float approximation.

```python
from decimal import Decimal

print(Decimal(0.1))
print(Decimal("0.1"))
```

### 35. What is banker's rounding?

Python `round()` rounds `.5` ties to the nearest even number.

```python
print(round(2.5))
print(round(3.5))
```

### 36. How do you sum digits of an integer?

Use `% 10` and `// 10`.

```python
def sum_digits(num):
    total = 0
    while num:
        total += num % 10
        num //= 10
    return total
```

### 37. How do you reverse an integer?

Build result using modulo and floor division.

```python
def reverse_int(num):
    result = 0
    while num:
        result = result * 10 + num % 10
        num //= 10
    return result
```

### 38. How do you check numeric palindrome?

Reverse the number and compare with original.

```python
def is_palindrome(num):
    original = num
    reversed_num = 0
    while num:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    return original == reversed_num
```

### 39. How do you use modulo for cyclic indexing?

Use `index % length`.

```python
warehouses = ["A", "B", "C"]
print(warehouses[4 % len(warehouses)])
```

### 40. What is integer division useful for?

Batching, pagination, digit extraction, and quotient calculation.

### 41. What is modulo useful for?

Remainders, even/odd checks, cycles, wrapping arrays, and divisibility.

### 42. How do you check divisibility?

Use modulo equals zero.

```python
print(100 % 5 == 0)
```

### 43. How do you format money to two decimals?

Use format specifiers for display.

```python
price = 999.9
print(f"{price:.2f}")
```

### 44. What is the difference between display formatting and exact value?

Formatting changes display, not the underlying number.

### 45. What is `math.floor()` vs `int()`?

`math.floor()` floors toward negative infinity. `int()` truncates toward zero.

```python
import math

print(math.floor(-9.5))
print(int(-9.5))
```

## Pro Level

### 46. How are Python floats represented?

They use IEEE 754 binary floating-point.

### 47. What is `float("inf")`?

It represents positive infinity.

```python
print(float("inf"))
```

### 48. What is `float("nan")`?

NaN means “not a number”.

```python
value = float("nan")
print(value != value)
```

### 49. How do you check for NaN?

Use `math.isnan()`.

```python
import math

print(math.isnan(float("nan")))
```

### 50. How do you check for infinity?

Use `math.isinf()`.

```python
import math

print(math.isinf(float("inf")))
```

### 51. Are booleans numeric in Python?

Yes. `bool` is a subclass of `int`.

```python
print(True + True)
```

### 52. Why is `True == 1`?

Because `bool` behaves like `0` and `1`.

```python
print(True == 1)
```

### 53. Can complex numbers be ordered?

No. Comparisons like `<` are not supported.

```python
# print((3 + 4j) < (5 + 6j))  # TypeError
```

### 54. How do you get magnitude of complex number?

Use `abs()`.

```python
print(abs(3 + 4j))
```

### 55. Can complex numbers be dictionary keys?

Yes, complex numbers are hashable.

```python
data = {3 + 4j: "signal"}
```

### 56. What is type promotion?

Operations between numeric types may produce a broader type, such as `int + float -> float`.

### 57. What is arbitrary precision?

Python integers can grow beyond fixed 32-bit or 64-bit limits.

### 58. When should you use `Fraction`?

Use `fractions.Fraction` for exact rational arithmetic.

```python
from fractions import Fraction

print(Fraction(1, 3) + Fraction(1, 3))
```

### 59. When should you use `Decimal` vs `float`?

Use `Decimal` for exact decimal/business money calculations. Use `float` for approximate scientific/analytics calculations.

### 60. What should you say if asked “int, float, or Decimal for price?”

Use integer cents or `Decimal` for money. Avoid `float` for exact financial calculations.

## Final Interview Checklist

- `int` is arbitrary precision.
- `float` is approximate binary floating-point.
- `complex` has `.real`, `.imag`, and `.conjugate()`.
- `/` returns float; `//` floors.
- `%` is essential for even/odd, divisibility, and cycles.
- `int()` truncates; `round()` rounds.
- Use `math.isclose()` for float comparisons.
- Use `Decimal` or integer cents for money.
- Complex numbers cannot be ordered with `<` / `>`.

## See also

- [Python numeric core concepts](core-concepts.md)
- [Python numeric operations](operations-and-methods.md)
- [Python numeric interview problems](interview-problems.md)
- [Python functions FAQ](../functions/frequently-asked-questions.md)
