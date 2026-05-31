# Python RegEx Reference

## Quick Function Table

| Function | Meaning | Best use |
|----------|---------|----------|
| `re.search()` | first match anywhere | find text |
| `re.match()` | match from start | prefix checks |
| `re.fullmatch()` | match whole string | validation |
| `re.findall()` | all matches as list | extraction |
| `re.finditer()` | all matches as iterator | large text processing |
| `re.sub()` | replace matches | cleaning text |
| `re.split()` | split by pattern | flexible splitting |
| `re.compile()` | reusable pattern object | repeated matching |

## `re.search()`

```python
import re

text = "Payment ID PAY-8831 completed"
match = re.search(r"PAY-\d+", text)

print(match.group() if match else None)
```

## `re.match()`

```python
import re

text = "SKU-1024 Laptop"
print(re.match(r"SKU-\d+", text) is not None)
```

## `re.fullmatch()`

```python
import re

sku = "SKU-1024"
print(re.fullmatch(r"SKU-\d{4}", sku) is not None)
```

## `re.findall()`

```python
import re

text = "ORD-100, ORD-101, ORD-102"
print(re.findall(r"ORD-\d+", text))
```

## `re.finditer()`

```python
import re

text = "Mouse $25, Keyboard $75"

for match in re.finditer(r"\$(\d+)", text):
    print(match.group(1))
```

## Groups

```python
import re

text = "SKU-1024: Laptop"
match = re.search(r"(SKU-\d+):\s(.+)", text)

if match:
    print(match.group(1))
    print(match.group(2))
```

## Named Groups

```python
import re

text = "ORD-2026-501"
match = re.fullmatch(r"ORD-(?P<year>\d{4})-(?P<number>\d+)", text)

if match:
    print(match.group("year"))
```

## `re.sub()`

```python
import re

text = "coupon SAVE10 expires soon"
print(re.sub(r"SAVE\d+", "HIDDEN", text))
```

## `re.compile()`

```python
import re

sku_pattern = re.compile(r"SKU-\d{4}")

print(sku_pattern.fullmatch("SKU-1024") is not None)
```

## Common Flags

| Flag | Meaning |
|------|---------|
| `re.IGNORECASE` | case-insensitive matching |
| `re.MULTILINE` | `^` and `$` work per line |
| `re.DOTALL` | `.` also matches newline |
| `re.VERBOSE` | allow readable multi-line regex |

## See also

- [Python RegEx: core concepts](core-concepts.md)
- [Python RegEx interview problems](interview-problems.md)
- [Python RegEx FAQ](frequently-asked-questions.md)
