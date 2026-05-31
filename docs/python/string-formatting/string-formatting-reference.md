# Python String Formatting Reference

## Quick Table

| Format | Syntax | Use case |
|--------|--------|----------|
| f-string | `f"{name}"` | modern readable formatting |
| expression | `f"{price * qty}"` | inline calculations |
| decimal places | `f"{price:.2f}"` | prices and totals |
| width | `f"{name:20}"` | aligned reports |
| left align | `f"{name:<20}"` | text columns |
| right align | `f"{price:>10}"` | number columns |
| center align | `f"{title:^20}"` | headings |
| comma separator | `f"{amount:,}"` | large numbers |
| percent | `f"{rate:.2%}"` | rates and discounts |
| `format()` | `"{}".format(value)` | reusable templates |
| `%` | `"%s" % value` | legacy code |

## f-String Basics

```python
product = "Laptop"
price = 999.99

print(f"{product}: ${price}")
```

## Decimal Places

```python
total = 1024.987

print(f"${total:.2f}")
```

## Thousands Separator

```python
revenue = 1250000

print(f"${revenue:,}")
```

## Percent Formatting

```python
discount_rate = 0.15

print(f"Discount: {discount_rate:.0%}")
```

## Width and Alignment

```python
product = "Mouse"
price = 25

print(f"{product:<15} {price:>8.2f}")
```

## Fill Characters

```python
order_number = 501

print(f"{order_number:0>6}")
```

Output:

```text
000501
```

## Date Formatting

```python
from datetime import date

ordered_on = date(2026, 5, 31)

print(f"Ordered on: {ordered_on:%Y-%m-%d}")
```

## Debug f-Strings

```python
quantity = 3

print(f"{quantity=}")
```

Output:

```text
quantity=3
```

## `str.format()`

```python
message = "Product: {name}, Price: ${price:.2f}".format(
    name="Keyboard",
    price=75,
)

print(message)
```

## Positional `format()`

```python
print("{} x {} = ${:.2f}".format("Mouse", 2, 50))
```

## Legacy `%` Formatting

```python
product = "Monitor"
price = 199.99

print("Product: %s, Price: $%.2f" % (product, price))
```

## Common Comparisons

| Pair | Difference |
|------|------------|
| f-string vs `format()` | f-string is concise; `format()` works well for reusable templates |
| f-string vs `%` | f-string is modern; `%` is older legacy syntax |
| `:.2f` vs `round()` | `:.2f` formats display; `round()` returns a rounded number |
| formatting vs conversion | formatting returns a string; original value is unchanged |

## See also

- [Python string formatting: core concepts](core-concepts.md)
- [Python string formatting interview problems](interview-problems.md)
- [Python string formatting FAQ](frequently-asked-questions.md)
