# Python RegEx: Core Concepts

RegEx means **regular expression**. It is a pattern language used to search, match, validate, extract, and replace text.

In an online computer shopping system, RegEx can help with:

- validating product codes
- checking coupon formats
- extracting order IDs from logs
- validating email-like customer input
- cleaning imported CSV text
- finding prices or version numbers in descriptions

## Import the `re` Module

Python provides regular expressions through the built-in `re` module.

```python
import re
```

## Basic Search

```python
import re

text = "Order ID: ORD-2026-501"
match = re.search(r"ORD-\d{4}-\d+", text)

if match:
    print(match.group())
```

## Common Pattern Symbols

| Pattern | Meaning | Example |
|---------|---------|---------|
| `.` | any character except newline | `a.c` |
| `\d` | digit | `\d+` |
| `\w` | word character | `\w+` |
| `\s` | whitespace | `\s+` |
| `+` | one or more | `\d+` |
| `*` | zero or more | `\w*` |
| `?` | zero or one | `colou?r` |
| `{n}` | exactly n times | `\d{4}` |
| `^` | start of string | `^SKU` |
| `$` | end of string | `\.pdf$` |

## Raw Strings

Use raw strings for regex patterns.

```python
pattern = r"\d{4}"
```

Without `r`, backslashes can be interpreted by Python string rules before RegEx sees them.

## Validate Product Code

```python
import re


def is_valid_sku(sku):
    return re.fullmatch(r"SKU-\d{4}", sku) is not None


print(is_valid_sku("SKU-1024"))
print(is_valid_sku("SKU-ABC"))
```

## Extract All Prices

```python
import re

description = "Laptop $999, Mouse $25, Keyboard $75"
prices = re.findall(r"\$(\d+)", description)

print(prices)
```

## Replace Text

```python
import re

text = "Customer phone: 9876543210"
masked = re.sub(r"\d{10}", "**********", text)

print(masked)
```

## Common Gotchas

### `match()` checks from the start

`re.match()` checks only at the beginning of a string.

### `search()` checks anywhere

`re.search()` finds the first match anywhere in the string.

### `fullmatch()` checks the whole string

Use `fullmatch()` for validation.

## Practice Problems

1. Validate SKU format like `SKU-1234`.
2. Extract order IDs from a log line.
3. Replace all phone numbers with masked text.
4. Find all `.pdf` files in a list.
5. Explain `search()` vs `match()` vs `fullmatch()`.

## See also

- [Python RegEx reference](regex-reference.md)
- [Python RegEx interview problems](interview-problems.md)
- [Python RegEx FAQ](frequently-asked-questions.md)
- [Python strings: core concepts](../strings/core-concepts.md)
