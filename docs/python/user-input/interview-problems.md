# Python User Input Interview Problems

## 1. Read Product Search Text

### Problem

Ask the user for a product search term and normalize extra spaces.

```python
def read_search_term():
    search = input("Search product: ").strip()
    return search
```

**Complexity:** `O(n)` time and space for input length.

## 2. Read Quantity as Integer

```python
def read_quantity():
    quantity_text = input("Quantity: ")
    return int(quantity_text)
```

This is simple, but it raises `ValueError` for invalid input.

## 3. Read Quantity Safely

```python
def read_quantity_safe():
    quantity_text = input("Quantity: ")

    try:
        return int(quantity_text)
    except ValueError:
        return 1
```

## 4. Keep Asking Until Quantity Is Valid

```python
def read_positive_quantity():
    while True:
        quantity_text = input("Quantity: ")

        try:
            quantity = int(quantity_text)
        except ValueError:
            print("Enter a valid number")
            continue

        if quantity <= 0:
            print("Quantity must be positive")
            continue

        return quantity
```

## 5. Validate Payment Method

```python
def read_payment_method():
    allowed = {"card", "upi", "cod"}

    while True:
        method = input("Payment method card/upi/cod: ").strip().lower()

        if method in allowed:
            return method

        print("Invalid payment method")
```

## 6. Normalize Coupon Code

```python
def read_coupon_code():
    coupon = input("Coupon code optional: ").strip().upper()

    if coupon == "":
        return None

    return coupon
```

## 7. Read Multiple Product IDs

```python
def read_product_ids():
    raw = input("Product IDs comma separated: ")
    parts = raw.split(",")
    return [int(part.strip()) for part in parts if part.strip()]
```

Example input:

```text
101, 102, 103
```

## 8. Handle Invalid Product IDs

```python
def read_product_ids_safe():
    raw = input("Product IDs comma separated: ")
    ids = []

    for part in raw.split(","):
        part = part.strip()
        if not part:
            continue

        try:
            ids.append(int(part))
        except ValueError:
            print(f"Skipping invalid ID: {part}")

    return ids
```

## 9. Confirm Checkout

```python
def confirm_checkout():
    answer = input("Confirm checkout yes/no: ").strip().lower()
    return answer in {"yes", "y"}
```

## 10. Read Price With Validation

```python
def read_price():
    while True:
        value = input("Price: ")

        try:
            price = float(value)
        except ValueError:
            print("Enter a valid price")
            continue

        if price < 0:
            print("Price cannot be negative")
            continue

        return price
```

## Summary

| Problem pattern | Input idea |
|-----------------|------------|
| text search | `.strip()` |
| numeric input | `int()` or `float()` |
| invalid conversion | `try` / `except ValueError` |
| repeated prompt | `while True` |
| menu validation | membership in set |
| optional input | empty string to `None` |
| multiple values | `split()` and conversion |

## See also

- [Python user input: core concepts](core-concepts.md)
- [Python user input reference](user-input-reference.md)
- [Python user input FAQ](frequently-asked-questions.md)
