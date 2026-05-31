# Python User Input: Frequently Asked Interview Questions

## Basic Level

### 1. Which function reads user input in Python?

`input()` reads user input from the terminal.

### 2. What does `input()` return?

It always returns a string.

### 3. How do you show a prompt to the user?

```python
name = input("Enter product name: ")
```

### 4. How do you convert input to an integer?

```python
quantity = int(input("Quantity: "))
```

### 5. How do you convert input to a float?

```python
price = float(input("Price: "))
```

### 6. What error happens for `int("two")`?

`ValueError`.

### 7. How do you remove extra spaces from input?

Use `.strip()`.

### 8. How do you make input lowercase?

Use `.lower()`.

### 9. How do you make input uppercase?

Use `.upper()`.

### 10. What happens if the user presses Enter?

`input()` returns an empty string `""`.

## Intermediate Level

### 11. How do you safely handle invalid numeric input?

Use `try` / `except ValueError`.

### 12. How do you keep asking until input is valid?

Use a loop with validation.

```python
while True:
    value = input("Quantity: ")
    if value.isdigit():
        break
```

### 13. Why is `.isdigit()` not always enough?

It does not handle negatives, decimals, or some real-world numeric formats well.

### 14. How do you validate menu choices?

Compare normalized input against a set of allowed values.

### 15. How do you read optional input?

Treat an empty string as `None` or a default value.

### 16. How do you read comma-separated values?

Use `.split(",")`.

### 17. How do you read yes/no input?

Normalize with `.strip().lower()` and compare with accepted words.

### 18. Should user input be trusted?

No. Always validate and sanitize it before use.

### 19. Why should input conversion be separated from validation?

It makes code easier to test and debug.

### 20. What is a common beginner mistake?

Forgetting that `input()` returns a string.

## Advanced Level

### 21. How do you write reusable input helpers?

Create functions such as `read_int()` or `read_positive_int()`.

### 22. Why should validation messages be clear?

Clear messages help users correct their input.

### 23. How can input cause `TypeError`?

Using input as a number without conversion can cause string-number operations.

### 24. How can input cause `ValueError`?

Invalid conversion such as `int("abc")` raises `ValueError`.

### 25. How should password input be handled?

Use `getpass.getpass()` instead of plain `input()` so text is not echoed.

### 26. Is `input()` used for web app form data?

No. Web frameworks read request data differently. `input()` is for terminal programs.

### 27. Can `input()` be tested?

Yes, by mocking input or separating parsing logic into pure functions.

### 28. What is the best way to handle prices from input?

For real money, parse carefully and consider `Decimal` instead of `float`.

### 29. What is a common interview trap?

Using `bool(input(...))` for yes/no. Any non-empty string becomes `True`, even `"no"`.

### 30. What should you remember?

`input()` returns `str`; normalize text; convert explicitly; handle `ValueError`; validate choices and ranges.

## Final Interview Checklist

- `input()` always returns string.
- Use `.strip()` to remove surrounding spaces.
- Use `int()` and `float()` for numeric conversion.
- Catch `ValueError` for bad numeric input.
- Use loops for repeated prompts.
- Validate fixed choices with a set.
- Do not use raw input directly in SQL, file paths, or business rules.

## See also

- [Python user input: core concepts](core-concepts.md)
- [Python user input reference](user-input-reference.md)
- [Python user input interview problems](interview-problems.md)
- [Python exception handling](../exception-handling/core-concepts.md)
