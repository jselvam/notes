# Python User Input Reference

## Quick Table

| Task | Example |
|------|---------|
| Read text | `name = input("Name: ")` |
| Convert to integer | `quantity = int(text)` |
| Convert to float | `price = float(text)` |
| Remove spaces | `text.strip()` |
| Normalize lowercase | `text.lower()` |
| Normalize uppercase | `text.upper()` |
| Validate choice | `value in allowed_values` |
| Handle bad input | `try` / `except ValueError` |
| Repeat input | `while True` |

## `input()` Syntax

```python
value = input("Prompt message: ")
```

The prompt is optional, but it helps the user understand what to enter.

## String Input

```python
search = input("Search products: ").strip()

print(f"Searching for {search}")
```

## Integer Input

```python
quantity_text = input("Quantity: ")
quantity = int(quantity_text)
```

## Float Input

```python
price_text = input("Price: ")
price = float(price_text)
```

## Safe Integer Helper

```python
def read_int(prompt):
    while True:
        value = input(prompt)

        try:
            return int(value)
        except ValueError:
            print("Please enter a valid integer")


quantity = read_int("Quantity: ")
print(quantity)
```

## Validate Positive Number

```python
def read_positive_int(prompt):
    while True:
        value = input(prompt)

        try:
            number = int(value)
        except ValueError:
            print("Please enter a valid integer")
            continue

        if number <= 0:
            print("Number must be positive")
            continue

        return number
```

## Validate Menu Choice

```python
def read_payment_method():
    allowed = {"card", "upi", "cod"}

    while True:
        method = input("Payment method card/upi/cod: ").strip().lower()

        if method in allowed:
            return method

        print("Invalid payment method")
```

## Normalize Coupon Code

```python
coupon = input("Coupon code: ").strip().upper()

if coupon:
    print(f"Applying coupon {coupon}")
else:
    print("No coupon entered")
```

## Common Input Conversions

| User enters | Code | Result |
|-------------|------|--------|
| `"10"` | `int(value)` | `10` |
| `"999.99"` | `float(value)` | `999.99` |
| `" yes "` | `value.strip().lower()` | `"yes"` |
| `"save10"` | `value.upper()` | `"SAVE10"` |
| `"laptop,mouse"` | `value.split(",")` | `["laptop", "mouse"]` |

## See also

- [Python user input: core concepts](core-concepts.md)
- [Python user input interview problems](interview-problems.md)
- [Python user input FAQ](frequently-asked-questions.md)
