# Python User Input: Core Concepts

User input lets a Python program receive data while it is running. Python uses the built-in `input()` function for terminal input.

In an online computer shopping system, user input can be used for:

- entering product names
- selecting quantity
- applying coupon codes
- choosing payment method
- searching catalog items
- confirming checkout

## Basic `input()`

```python
product_name = input("Enter product name: ")
print(f"You searched for: {product_name}")
```

`input()` always returns a string.

## Convert Input to Number

```python
quantity_text = input("Enter quantity: ")
quantity = int(quantity_text)

print(f"Quantity: {quantity}")
```

If the user enters non-numeric text, `int()` raises `ValueError`.

## Safe Numeric Input

```python
quantity_text = input("Enter quantity: ")

try:
    quantity = int(quantity_text)
except ValueError:
    quantity = 1

print(f"Quantity: {quantity}")
```

## Float Input

```python
price_text = input("Enter product price: ")
price = float(price_text)

print(f"Price: ${price:.2f}")
```

## Boolean-Like Input

`input()` does not directly return `True` or `False`. Convert the text manually.

```python
answer = input("Do you want to checkout? yes/no: ").strip().lower()
checkout = answer == "yes"

print(checkout)
```

## Validate Choices

```python
payment_method = input("Payment method card/upi/cod: ").strip().lower()

if payment_method in {"card", "upi", "cod"}:
    print("Payment method accepted")
else:
    print("Invalid payment method")
```

## Repeat Until Valid

```python
while True:
    quantity_text = input("Enter quantity: ")

    try:
        quantity = int(quantity_text)
    except ValueError:
        print("Please enter a number")
        continue

    if quantity <= 0:
        print("Quantity must be positive")
        continue

    break

print(f"Accepted quantity: {quantity}")
```

## Common Gotchas

### `input()` returns string

```python
quantity = input("Quantity: ")
print(quantity + 1)
```

This raises `TypeError` because `quantity` is a string.

### Empty input is still a string

If the user presses Enter, `input()` returns `""`.

### Never trust raw user input

Always validate and convert user input before using it in calculations, file paths, SQL queries, or business rules.

## Practice Problems

1. Ask for product name and print a search message.
2. Ask for quantity and convert it to `int`.
3. Keep asking until the user enters a positive quantity.
4. Validate payment method from a fixed set.
5. Ask for coupon code and normalize it with `.strip().upper()`.

## See also

- [Python user input reference](user-input-reference.md)
- [Python user input interview problems](interview-problems.md)
- [Python user input FAQ](frequently-asked-questions.md)
- [Python exception handling](../exception-handling/core-concepts.md)
