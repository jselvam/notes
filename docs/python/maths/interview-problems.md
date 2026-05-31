# Python Maths Interview Problems

## 1. Cart Total

```python
def cart_total(prices):
    return sum(prices)


print(cart_total([999, 25, 75]))
```

## 2. Average Product Price

```python
def average_price(prices):
    if not prices:
        return 0
    return sum(prices) / len(prices)


print(average_price([999, 25, 75]))
```

## 3. Min and Max Price

```python
def min_max_price(prices):
    if not prices:
        return None
    return min(prices), max(prices)
```

## 4. Round Final Price

```python
def display_price(price):
    return round(price, 2)


print(display_price(999.987))
```

## 5. Exact Money With Decimal

```python
from decimal import Decimal


def exact_tax(price, tax_rate):
    price = Decimal(price)
    tax_rate = Decimal(tax_rate)
    return price + price * tax_rate


print(exact_tax("999.99", "0.08"))
```

## 6. GCD of Package Sizes

```python
import math


def common_pack_size(a, b):
    return math.gcd(a, b)


print(common_pack_size(24, 36))
```

## 7. LCM for Delivery Cycle

```python
import math


def common_delivery_cycle(a, b):
    return math.lcm(a, b)


print(common_delivery_cycle(4, 6))
```

## 8. Prime Check

```python
def is_prime(num):
    if num < 2:
        return False

    factor = 2
    while factor * factor <= num:
        if num % factor == 0:
            return False
        factor += 1

    return True


print(is_prime(29))
```

## 9. Random Coupon

```python
import random


def random_coupon(coupons):
    return random.choice(coupons)


print(random_coupon(["SAVE10", "OFFICE20"]))
```

## 10. Clamp Discount

```python
def clamp_discount(discount):
    return max(0, min(discount, 100))


print(clamp_discount(120))
```

## Summary

| Pattern | Maths idea |
|---------|------------|
| Total | `sum()` |
| Average | `sum() / len()` |
| Bounds | `min()` / `max()` |
| Rounding | `round()` |
| Exact money | `Decimal` |
| Factors | `gcd`, `lcm` |
| Random pick | `random.choice()` |

## See also

- [Python maths core concepts](core-concepts.md)
- [Python maths reference](maths-reference.md)
- [Python maths FAQ](frequently-asked-questions.md)
