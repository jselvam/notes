# Python Maths Reference: Interview Notes

## Quick Table

| Tool | Use |
|------|-----|
| `sum()` | Total |
| `min()` / `max()` | Smallest/largest |
| `round()` | Round display values |
| `abs()` | Absolute difference |
| `pow()` | Exponentiation |
| `math.ceil()` | Round up |
| `math.floor()` | Round down |
| `math.sqrt()` | Square root |
| `math.gcd()` | Greatest common divisor |
| `math.lcm()` | Least common multiple |
| `statistics.mean()` | Average |
| `statistics.median()` | Middle value |
| `random.choice()` | Pick random item |

## Built-ins

```python
prices = [999, 25, 75]

print(sum(prices))
print(min(prices))
print(max(prices))
print(abs(25 - 999))
```

## `math`

```python
import math

print(math.ceil(10.1))
print(math.floor(10.9))
print(math.sqrt(81))
print(math.gcd(24, 36))
print(math.lcm(4, 6))
```

## `statistics`

```python
import statistics

prices = [25, 75, 199, 999]

print(statistics.mean(prices))
print(statistics.median(prices))
```

## `random`

```python
import random

codes = ["SAVE10", "OFFICE20", "SHIPFREE"]

print(random.choice(codes))
print(random.randint(1000, 9999))
```

## `Decimal`

```python
from decimal import Decimal

total = Decimal("99.99") + Decimal("0.01")
print(total)
```

## Common Interview Questions

### What is `math.ceil()`?

Rounds up to the nearest integer.

### What is `math.floor()`?

Rounds down to the nearest integer.

### What is `statistics.mean()`?

Arithmetic average.

### What is `random.choice()`?

Selects one random item from a sequence.

## See also

- [Python maths core concepts](core-concepts.md)
- [Python maths interview problems](interview-problems.md)
- [Python maths FAQ](frequently-asked-questions.md)
