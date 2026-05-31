# Python Strings: Frequently Asked Interview Questions

This page collects frequently asked Python `str` interview questions from **basic** to **pro** level. Examples use online computer shopping system ideas like product names, coupon codes, SKUs, search queries, and file names.

## Basic Level

### 1. What is a string in Python?

A string is an immutable sequence of characters.

```python
name = "laptop"
```

### 2. How do you create a string?

Use single quotes, double quotes, or triple quotes.

```python
a = 'mouse'
b = "keyboard"
c = """monitor"""
```

### 3. Are strings mutable?

No. String operations return new strings.

```python
name = "Laptop"
print(name.lower())
print(name)
```

### 4. How do you get string length?

Use `len()`.

```python
print(len("laptop"))
```

### 5. How do you access the first character?

Use index `0`.

```python
print("laptop"[0])
```

### 6. How do you access the last character?

Use index `-1`.

```python
print("laptop"[-1])
```

### 7. What happens with an invalid index?

Python raises `IndexError`.

```python
# print("laptop"[99])  # IndexError
```

### 8. How do you slice a string?

Use `start:stop:step`.

```python
print("keyboard"[0:3])
```

### 9. How do you reverse a string?

Use slicing.

```python
print("laptop"[::-1])
```

### 10. How do you loop through a string?

Use a `for` loop.

```python
for ch in "mouse":
    print(ch)
```

### 11. How do you check if a substring exists?

Use `in`.

```python
print("lap" in "laptop")
```

### 12. How do you concatenate strings?

Use `+`.

```python
print("wireless" + " " + "mouse")
```

### 13. How do you repeat a string?

Use `*`.

```python
print("-" * 5)
```

### 14. What is an f-string?

A readable way to format values into strings.

```python
price = 999
print(f"Laptop costs {price}")
```

### 15. What is a multiline string?

A string written with triple quotes.

```python
description = """Line 1
Line 2"""
```

## Intermediate Level

### 16. What does `lower()` do?

It returns a lowercase copy.

```python
print("Laptop".lower())
```

### 17. What does `upper()` do?

It returns an uppercase copy.

```python
print("mouse".upper())
```

### 18. What does `strip()` do?

It removes whitespace from both ends.

```python
print("  laptop  ".strip())
```

### 19. What is the difference between `strip()`, `lstrip()`, and `rstrip()`?

`strip()` removes both sides, `lstrip()` left side, `rstrip()` right side.

### 20. What does `replace()` do?

It returns a new string with replacements.

```python
print("wireless mouse".replace(" ", "-"))
```

### 21. What does `split()` do?

It converts a string into a list.

```python
print("laptop,mouse".split(","))
```

### 22. What does `join()` do?

It joins strings from an iterable.

```python
print(", ".join(["laptop", "mouse"]))
```

### 23. Why prefer `join()` over `+` in loops?

`join()` avoids many intermediate strings.

### 24. What does `find()` do?

It returns the first index or `-1`.

```python
print("wireless mouse".find("mouse"))
```

### 25. What does `index()` do?

It returns the first index or raises `ValueError`.

```python
print("wireless mouse".index("mouse"))
```

### 26. What is the difference between `find()` and `index()`?

`find()` returns `-1` when missing. `index()` raises `ValueError`.

### 27. What does `count()` do?

It counts non-overlapping occurrences.

```python
print("banana".count("a"))
```

### 28. What does `startswith()` do?

It checks a prefix.

```python
print("ORD-1001".startswith("ORD-"))
```

### 29. What does `endswith()` do?

It checks a suffix.

```python
print("invoice.pdf".endswith(".pdf"))
```

### 30. What does `isdigit()` do?

It checks whether all characters are digits.

```python
print("12345".isdigit())
```

## Advanced Level

### 31. What is the time complexity of string indexing?

Indexing is **O(1)**.

```python
print("laptop"[2])
```

### 32. What is the time complexity of string slicing?

Slicing is **O(k)** where `k` is the slice length.

### 33. What is the time complexity of substring search?

It depends on the algorithm and input, but interview answers often treat simple substring checks as up to **O(n * m)** conceptually.

### 34. How do you check palindrome?

Compare string with its reverse.

```python
def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]
```

### 35. How do you check anagram?

Compare character counts.

```python
from collections import Counter

print(Counter("listen") == Counter("silent"))
```

### 36. How do you find the first non-repeating character?

Count characters, then scan original order.

```python
def first_unique(text):
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in text:
        if counts[ch] == 1:
            return ch
```

### 37. How do you remove duplicate characters preserving order?

Use a `seen` set and result list.

```python
def unique_chars(text):
    seen = set()
    result = []
    for ch in text:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    return "".join(result)
```

### 38. How do you count vowels?

Use a set for vowel lookup.

```python
def count_vowels(text):
    vowels = {"a", "e", "i", "o", "u"}
    return sum(1 for ch in text.lower() if ch in vowels)
```

### 39. How do you normalize text before comparison?

Use `strip()` and `lower()` or `casefold()`.

```python
query = "  Laptop  "
print(query.strip().lower())
```

### 40. How do you parse comma-separated tags?

Use `split()`.

```python
tags = "laptop,mouse,keyboard".split(",")
```

### 41. How do you build a string from characters efficiently?

Append to a list, then use `join()`.

```python
chars = ["l", "a", "p"]
print("".join(chars))
```

### 42. How do you validate alphanumeric coupon codes?

Use `isalnum()`.

```python
print("SAVE10".isalnum())
```

### 43. What is `casefold()`?

A stronger version of lowercase for case-insensitive comparisons.

```python
print("LAPTOP".casefold())
```

### 44. What is `partition()`?

It splits into `(before, separator, after)`.

```python
print("SKU-101".partition("-"))
```

### 45. What is `zfill()`?

It pads a string with zeros on the left.

```python
print("42".zfill(5))
```

## Pro Level

### 46. Why are strings immutable?

Immutability makes strings safer to share and usable as dictionary keys.

### 47. Can strings be dictionary keys?

Yes. Strings are hashable.

```python
prices = {"laptop": 999}
```

### 48. What is string interning?

Python may reuse some string objects internally for optimization.

```python
a = "laptop"
b = "laptop"
print(a == b)
```

Use `==` for value comparison, not `is`.

### 49. What is the difference between `==` and `is` for strings?

`==` compares value. `is` compares identity.

### 50. What is Unicode?

Unicode is a standard for representing text characters from many languages and symbol sets.

### 51. What is encoding?

Encoding converts text into bytes, such as UTF-8.

```python
data = "laptop".encode("utf-8")
```

### 52. What is decoding?

Decoding converts bytes back to text.

```python
text = b"laptop".decode("utf-8")
```

### 53. What is the difference between `str` and `bytes`?

`str` is text. `bytes` is binary data.

### 54. Why can repeated string concatenation be slow?

Strings are immutable, so each concatenation may create a new string.

### 55. How do you compare strings lexicographically?

Python compares character by character.

```python
print("keyboard" < "mouse")
```

### 56. What is a raw string?

A raw string treats backslashes mostly as literal characters.

```python
path = r"C:\temp\file.txt"
```

### 57. What are escape characters?

Special sequences like `\n`, `\t`, and `\\`.

```python
print("Line 1\nLine 2")
```

### 58. Why should passwords/secrets not be casually logged as strings?

Strings can appear in logs, memory dumps, or error messages. Treat sensitive values carefully.

### 59. When should you use regular expressions instead of string methods?

Use regex for complex patterns. Use string methods for simple checks because they are clearer.

### 60. What should you say if asked “string or list of chars?”

Use string for immutable text. Use list of characters when building or modifying many characters efficiently, then `join()`.

## Final Interview Checklist

- Strings are immutable sequences.
- Indexing is **O(1)**; slicing creates a new string.
- Use `lower()` / `casefold()` for case-insensitive checks.
- Use `join()` for efficient string building.
- Use dictionaries or `Counter` for frequency problems.
- Use sets for membership checks like vowels or seen characters.
- Use `==`, not `is`, for string value comparison.
- Know `find()` vs `index()`, `split()` vs `join()`, and `strip()` variants.

## See also

- [Python strings: core concepts](core-concepts.md)
- [Python string methods](methods.md)
- [Python string interview problems](interview-problems.md)
- [Python strings practice](practice-tasks.md)
