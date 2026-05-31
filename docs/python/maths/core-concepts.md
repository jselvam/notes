# Python Maths: Core Concepts

Python provides built-in math operations plus modules such as `math`, `statistics`, `random`, `decimal`, and `fractions`.

In an online computer shopping system, maths is used for:

- cart totals
- discounts and tax
- average order value
- minimum/maximum price
- rounding display values
- random coupon codes
- analytics and reports

## Built-in Numeric Helpers

```python
prices = [999, 25, 75, 199]

print(sum(prices))
print(min(prices))
print(max(prices))
print(round(999.987, 2))
```

## `math` Module

```python
import math

print(math.ceil(10.2))
print(math.floor(10.8))
print(math.sqrt(16))
print(math.gcd(12, 18))
```

## `statistics` Module

```python
import statistics

prices = [999, 25, 75, 199]

print(statistics.mean(prices))
print(statistics.median(prices))
```

## `random` Module

```python
import random

coupon = random.choice(["SAVE10", "OFFICE20", "SHIPFREE"])
print(coupon)
```

## `Decimal` for Money

```python
from decimal import Decimal

price = Decimal("999.99")
tax = Decimal("0.08")

print(price + price * tax)
```

## `Fraction` for Exact Rational Values

```python
from fractions import Fraction

print(Fraction(1, 3) + Fraction(1, 3))
```

## Common Interview Points

### Why not use float for exact money?

Floats are approximate. Use integer cents or `Decimal`.

### What is the difference between `floor`, `ceil`, and `round`?

`floor` goes down, `ceil` goes up, and `round` rounds to nearest.

### What is modulo useful for?

Even/odd checks, cycles, wrapping indexes, and divisibility.

## Practice Problems

1. Calculate cart total.
2. Find average product price.
3. Find min and max product price.
4. Round final price to two decimals.
5. Calculate exact tax using `Decimal`.
6. Use `math.gcd()` for a math problem.
7. Pick a random coupon code.

## See also

- [Python maths reference](maths-reference.md)
- [Python maths interview problems](interview-problems.md)
- [Python maths FAQ](frequently-asked-questions.md)
- [Python numeric types](../numbers/core-concepts.md)
