# Python String Formatting: Frequently Asked Interview Questions

## Basic Level

### 1. What is string formatting?

String formatting inserts values into a string template.

### 2. What is an f-string?

An f-string is a formatted string literal that starts with `f`.

```python
name = "Laptop"
print(f"Product: {name}")
```

### 3. Which string formatting style is preferred in modern Python?

f-strings are usually preferred because they are readable and concise.

### 4. What Python version introduced f-strings?

Python 3.6.

### 5. How do you format two decimal places?

```python
price = 999.9
print(f"{price:.2f}")
```

### 6. Does formatting change the original value?

No. Formatting returns a string representation.

### 7. How do you use expressions inside f-strings?

```python
price = 100
quantity = 2
print(f"Total: {price * quantity}")
```

### 8. What is `str.format()`?

It is a method that inserts values into placeholders.

### 9. What is `%` formatting?

It is the older printf-style formatting syntax.

### 10. Can f-strings call functions?

Yes, but keep expressions simple for readability.

## Intermediate Level

### 11. How do you right-align text?

```python
print(f"{'999':>10}")
```

### 12. How do you left-align text?

```python
print(f"{'Laptop':<15}")
```

### 13. How do you center-align text?

```python
print(f"{'Invoice':^20}")
```

### 14. How do you add leading zeros?

```python
print(f"{501:0>6}")
```

### 15. How do you add comma separators?

```python
print(f"{1250000:,}")
```

### 16. How do you format a percentage?

```python
rate = 0.15
print(f"{rate:.0%}")
```

### 17. How do you format dates with f-strings?

```python
from datetime import date

print(f"{date.today():%Y-%m-%d}")
```

### 18. What is the debug f-string syntax?

```python
quantity = 3
print(f"{quantity=}")
```

### 19. What is the difference between `:.2f` and `round()`?

`:.2f` formats display as a string. `round()` returns a rounded number.

### 20. When is `str.format()` useful?

It is useful when the template is stored separately and filled later.

## Advanced Level

### 21. Why avoid very complex expressions in f-strings?

They make code harder to read and test.

### 22. Can f-strings be used for multi-line strings?

Yes.

```python
name = "Laptop"
price = 999.99

message = f"""
Product: {name}
Price: ${price:.2f}
"""
```

### 23. Can f-strings format custom objects?

Yes, if the object defines formatting behavior through methods such as `__format__`.

### 24. Is f-string formatting safe for SQL?

No. Use parameterized queries for SQL.

### 25. Which formatting style is common in logging?

Logging often uses lazy `%` style internally, such as `logger.info("Product %s", name)`.

### 26. Why is lazy logging useful?

It avoids building the message if that log level is disabled.

### 27. How do you escape braces in f-strings?

Use double braces.

```python
print(f"{{product}}")
```

### 28. What error happens if an f-string expression is invalid?

Usually `SyntaxError` or a runtime exception from the expression.

### 29. What is a common interview mistake?

Confusing formatting for display with numeric rounding or data conversion.

### 30. What should you remember?

Prefer f-strings, know `:.2f`, alignment, width, commas, percent formatting, date formatting, and legacy `%` syntax.

## Final Interview Checklist

- Prefer f-strings for modern Python.
- Use `:.2f` for money display.
- Use `<`, `>`, `^` for alignment.
- Use `:,` for thousands separators.
- Use `:.0%` or `:.2%` for percentages.
- Avoid formatting user input into SQL.

## See also

- [Python string formatting: core concepts](core-concepts.md)
- [Python string formatting reference](string-formatting-reference.md)
- [Python string formatting interview problems](interview-problems.md)
- [Python strings: core concepts](../strings/core-concepts.md)
