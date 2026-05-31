# Python RegEx Interview Problems

## 1. Validate SKU Format

### Problem

Validate product SKU like `SKU-1234`.

```python
import re


def is_valid_sku(sku):
    return re.fullmatch(r"SKU-\d{4}", sku) is not None


print(is_valid_sku("SKU-1024"))
print(is_valid_sku("SKU-10A4"))
```

**Complexity:** `O(n)` time, `O(1)` extra space.

## 2. Extract Order IDs

```python
import re


def extract_order_ids(log_text):
    return re.findall(r"ORD-\d{4}-\d+", log_text)


log = "created ORD-2026-501, shipped ORD-2026-502"
print(extract_order_ids(log))
```

## 3. Validate Coupon Code

```python
import re


def is_valid_coupon(code):
    return re.fullmatch(r"[A-Z]{4}\d{2}", code) is not None


print(is_valid_coupon("SAVE10"))
```

## 4. Extract Prices

```python
import re


def extract_prices(text):
    return [int(price) for price in re.findall(r"\$(\d+)", text)]


print(extract_prices("Laptop $999, Mouse $25"))
```

## 5. Mask Phone Number

```python
import re


def mask_phone(text):
    return re.sub(r"\b\d{10}\b", "**********", text)


print(mask_phone("Call 9876543210 for delivery"))
```

## 6. Find PDF Files

```python
import re


def pdf_files(files):
    return [file for file in files if re.search(r"\.pdf$", file, re.IGNORECASE)]


print(pdf_files(["invoice.pdf", "photo.png", "manual.PDF"]))
```

## 7. Split Imported Product Tags

```python
import re


def split_tags(text):
    return [tag for tag in re.split(r"[,;|]\s*", text) if tag]


print(split_tags("laptop,hardware;office|subscription"))
```

## 8. Extract Named Groups From Order ID

```python
import re


def parse_order_id(order_id):
    match = re.fullmatch(r"ORD-(?P<year>\d{4})-(?P<number>\d+)", order_id)
    if not match:
        return None
    return match.groupdict()


print(parse_order_id("ORD-2026-501"))
```

## 9. Normalize Extra Spaces

```python
import re


def normalize_spaces(text):
    return re.sub(r"\s+", " ", text).strip()


print(normalize_spaces("Laptop     with    warranty"))
```

## 10. Validate Simple Email Format

```python
import re


def is_simple_email(email):
    return re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email) is not None


print(is_simple_email("buyer@example.com"))
```

## Summary

| Problem pattern | RegEx idea |
|-----------------|------------|
| validate complete string | `re.fullmatch()` |
| find first occurrence | `re.search()` |
| extract many values | `re.findall()` |
| process large matches | `re.finditer()` |
| replace sensitive data | `re.sub()` |
| readable repeated pattern | `re.compile()` |

## See also

- [Python RegEx: core concepts](core-concepts.md)
- [Python RegEx reference](regex-reference.md)
- [Python RegEx FAQ](frequently-asked-questions.md)
