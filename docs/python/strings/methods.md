# Python String Methods: Interview Notes

Python string methods are frequently asked because string problems appear in almost every interview: reverse string, palindrome, anagram, substring search, formatting, validation, and parsing.

Strings are **immutable**. Most methods return a **new string** and do not change the original.

## Quick Method Table

| Method | What it does | Interview use case |
|--------|--------------|--------------------|
| `lower()` / `upper()` | Change case | Case-insensitive compare |
| `casefold()` | Stronger lowercase | Robust text compare |
| `strip()` | Remove outer whitespace | Clean user input |
| `replace()` | Replace substring | Normalize text |
| `split()` | String to list | Parse CSV/search terms |
| `join()` | List to string | Build result efficiently |
| `find()` | Find index or `-1` | Safe substring search |
| `index()` | Find index or error | Required substring |
| `count()` | Count occurrences | Frequency checks |
| `startswith()` | Prefix check | SKU/order prefix |
| `endswith()` | Suffix check | File extension check |
| `isdigit()` | Digit validation | Product ID input |
| `isalpha()` | Alphabet validation | Name validation |
| `isalnum()` | Letters/numbers | Coupon validation |
| `format()` / f-string | Format values | Messages/output |

## `lower()` and `upper()`

```python
category = "Hardware"

print(category.lower())  # hardware
print(category.upper())  # HARDWARE
```

### Interview point

Use lowercasing before comparison when case should not matter.

```python
def same_product_name(a, b):
    return a.lower() == b.lower()
```

## `casefold()`

`casefold()` is stronger than `lower()` for case-insensitive matching.

```python
name = "LAPTOP"

print(name.casefold())  # laptop
```

### Interview point

For most basic interview examples, `lower()` is enough. Mention `casefold()` for more robust text normalization.

## `strip()`, `lstrip()`, `rstrip()`

Remove whitespace or selected characters from ends.

```python
raw_search = "  laptop  "

print(raw_search.strip())   # laptop
print(raw_search.lstrip())  # laptop  
print(raw_search.rstrip())  #   laptop
```

### Interview point

Use `strip()` before validation.

```python
def normalize_query(query):
    return query.strip().lower()
```

## `replace()`

Returns a new string with replacements.

```python
sku = "LAP TOP 13"
normalized = sku.replace(" ", "-")

print(normalized)
# LAP-TOP-13
```

### Interview point

Useful for normalization before palindrome/anagram checks.

## `split()`

Converts a string into a list.

```python
tags = "laptop,mouse,keyboard"

print(tags.split(","))
# ["laptop", "mouse", "keyboard"]
```

### Interview point

Use `split()` for parsing input.

```python
query = "laptop mouse monitor"
words = query.split()
```

## `join()`

Combines strings from an iterable.

```python
parts = ["laptop", "mouse", "keyboard"]

print(", ".join(parts))
# laptop, mouse, keyboard
```

### Interview point

Use `join()` instead of repeated `+` in loops.

```python
def remove_spaces(text):
    return "".join(ch for ch in text if ch != " ")
```

## `find()` and `index()`

Both search for a substring.

```python
text = "wireless mouse"

print(text.find("mouse"))   # 9
print(text.find("laptop"))  # -1
```

`index()` raises `ValueError` if missing.

```python
text = "wireless mouse"
print(text.index("mouse"))
```

### Interview point

Use `find()` when missing is normal. Use `index()` when missing should be treated as an error.

## `count()`

Counts non-overlapping occurrences.

```python
code = "AABBA"

print(code.count("A"))  # 3
```

### Interview point

For many character counts, use a dictionary or `Counter`.

```python
from collections import Counter

print(Counter("mouse"))
```

## `startswith()` and `endswith()`

```python
order_id = "ORD-1001"
file_name = "invoice.pdf"

print(order_id.startswith("ORD-"))  # True
print(file_name.endswith(".pdf"))   # True
```

### Interview point

Useful for prefix/suffix validation.

## Validation Methods

```python
print("12345".isdigit())       # True
print("Laptop".isalpha())      # True
print("SAVE10".isalnum())      # True
print("   ".isspace())         # True
```

### Interview point

These are useful for validating user input, coupon codes, and product IDs.

## `zfill()`

Pads a string with zeros on the left.

```python
order_number = "42"

print(order_number.zfill(5))
# 00042
```

## `partition()`

Splits into three parts: before separator, separator, after separator.

```python
sku = "LAPTOP-101"

prefix, separator, product_id = sku.partition("-")

print(prefix, product_id)
```

## f-strings

```python
name = "laptop"
price = 999

message = f"{name} costs ${price}"
print(message)
```

### Interview point

Prefer f-strings for readable formatting.

## Common Interview Questions

### Are string methods mutable?

No. They return new strings.

```python
name = "Laptop"
name.lower()
print(name)  # Laptop
```

### What is the difference between `split()` and `join()`?

`split()` converts string to list. `join()` converts list/iterable of strings to string.

### Why prefer `join()` over `+` in a loop?

`join()` avoids creating many intermediate strings.

### What is the difference between `find()` and `index()`?

`find()` returns `-1`; `index()` raises `ValueError`.

## Practice Problems

1. Normalize a search query using `strip()` and `lower()`.
2. Check if an invoice file ends with `.pdf`.
3. Split comma-separated product tags.
4. Join product names into a display string.
5. Count how many times a character appears.
6. Validate whether a coupon code is alphanumeric.
7. Replace spaces in SKU with hyphens.
8. Format product price using an f-string.

## See also

- [Python strings: core concepts](core-concepts.md)
- [Python string interview problems](interview-problems.md)
- [Python string FAQ](frequently-asked-questions.md)
