# Python String Formatting: Core Concepts

String formatting means building readable strings by inserting values into a template. It is common in logs, invoices, reports, email messages, API responses, and user-facing messages.

In an online computer shopping system, string formatting helps create:

- product labels
- order summaries
- payment messages
- invoice lines
- stock alerts
- formatted prices
- aligned reports

## Main Formatting Styles

Python has three common string formatting styles:

| Style | Example | Recommendation |
|-------|---------|----------------|
| f-string | `f"Price: {price}"` | prefer for modern Python |
| `str.format()` | `"Price: {}".format(price)` | useful for reusable templates |
| `%` formatting | `"Price: %s" % price` | older style, still seen in legacy code |

## f-Strings

f-strings are the most readable modern option.

```python
product = "Laptop"
price = 999.99

message = f"{product} costs ${price}"
print(message)
```

## Expressions Inside f-Strings

```python
price = 1000
discount = 10

message = f"Final price: ${price - (price * discount / 100)}"
print(message)
```

## Format Decimal Places

Use `:.2f` to show two digits after the decimal point.

```python
price = 999.9

print(f"Price: ${price:.2f}")
```

Output:

```text
Price: $999.90
```

## Align Text

```python
product = "Mouse"
price = 25

print(f"{product:<15} ${price:>8.2f}")
```

`<` left-aligns and `>` right-aligns.

## `str.format()`

```python
template = "Order {order_id} total is ${total:.2f}"
message = template.format(order_id="ORD-501", total=1024.99)

print(message)
```

## `%` Formatting

```python
product = "Keyboard"
price = 75

print("Product: %s, Price: $%.2f" % (product, price))
```

This style is older, but interviewers may ask about it because legacy code still uses it.

## Common Gotchas

### f-strings need Python 3.6+

Older Python versions do not support f-strings.

### Formatting does not change the original value

```python
price = 999.9
formatted = f"{price:.2f}"

print(type(price))
print(type(formatted))
```

`formatted` is a string. `price` remains a number.

### Do not build SQL with string formatting

Use parameterized queries instead of formatting user input into SQL strings.

## Practice Problems

1. Format product name and price using an f-string.
2. Show a price with two decimal places.
3. Align product report columns.
4. Format an order ID and total using `str.format()`.
5. Convert an old `%` formatted string to an f-string.

## See also

- [Python string formatting reference](string-formatting-reference.md)
- [Python string formatting interview problems](interview-problems.md)
- [Python string formatting FAQ](frequently-asked-questions.md)
- [Python strings: core concepts](../strings/core-concepts.md)
