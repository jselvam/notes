# Python Maths: Frequently Asked Interview Questions

## Basic Level

### 1. Which module provides advanced math functions?

The `math` module.

### 2. How do you calculate total?

Use `sum()`.

### 3. How do you find minimum?

Use `min()`.

### 4. How do you find maximum?

Use `max()`.

### 5. How do you get absolute value?

Use `abs()`.

### 6. How do you round a number?

Use `round()`.

### 7. What does `pow()` do?

Calculates exponentiation.

### 8. What does `%` help with?

Remainders, divisibility, even/odd checks.

### 9. How do you calculate average?

Use `sum(values) / len(values)`.

### 10. What should you do for empty average input?

Handle it before dividing.

## Intermediate Level

### 11. What is `math.ceil()`?

Rounds up.

### 12. What is `math.floor()`?

Rounds down.

### 13. What is `math.sqrt()`?

Square root.

### 14. What is `math.gcd()`?

Greatest common divisor.

### 15. What is `math.lcm()`?

Least common multiple.

### 16. What is `statistics.mean()`?

Average.

### 17. What is `statistics.median()`?

Middle value after sorting.

### 18. What is `random.choice()`?

Selects one random item.

### 19. What is `random.randint(a, b)`?

Random integer including both endpoints.

### 20. Why avoid float for money?

Floats are approximate.

## Advanced Level

### 21. Why use `Decimal`?

For exact decimal arithmetic.

### 22. Why pass strings to `Decimal`?

To avoid importing float approximation.

### 23. What is `Fraction`?

Exact rational number.

### 24. What is banker's rounding?

Python `round()` ties to nearest even.

### 25. How do you compare floats?

Use `math.isclose()`.

### 26. How do you test prime efficiently?

Check factors up to square root.

### 27. How do you clamp a value?

Use `max(min_value, min(value, max_value))`.

### 28. How do you avoid division by zero?

Check denominator before division.

### 29. What is modulo useful for in cycles?

Wrapping indexes.

### 30. What should you remember?

Use built-ins first, `math` for advanced functions, `Decimal` for money, and handle edge cases like empty lists and division by zero.

## See also

- [Python maths core concepts](core-concepts.md)
- [Python maths reference](maths-reference.md)
- [Python maths interview problems](interview-problems.md)
