# Python Operators: Frequently Asked Interview Questions

This page collects frequently asked Python operator interview questions from **basic** to **pro** level.

## Basic Level

### 1. What are operators in Python?

Operators perform operations on values.

```python
print(10 + 5)
```

### 2. What are arithmetic operators?

They perform math operations like addition, subtraction, multiplication, and division.

```python
print(1000 * 2)
```

### 3. What does `+` do?

It adds numbers or concatenates compatible sequences.

```python
print(10 + 5)
print("lap" + "top")
```

### 4. What does `-` do?

It subtracts numbers.

```python
print(100 - 25)
```

### 5. What does `*` do?

It multiplies numbers or repeats sequences.

```python
print(25 * 3)
print("ha" * 3)
```

### 6. What does `/` do?

It performs true division and returns a float.

```python
print(10 / 2)
```

### 7. What does `//` do?

It performs floor division.

```python
print(10 // 3)
```

### 8. What does `%` do?

It returns the remainder.

```python
print(10 % 3)
```

### 9. What does `**` do?

It performs exponentiation.

```python
print(2 ** 3)
```

### 10. What is an assignment operator?

It assigns or updates a variable.

```python
stock = 10
stock += 5
```

### 11. What does `+=` do?

It adds and assigns.

```python
stock = 10
stock += 2
```

### 12. What are comparison operators?

They compare values and return booleans.

```python
print(999 > 100)
```

### 13. What does `==` do?

It checks value equality.

```python
print("laptop" == "laptop")
```

### 14. What does `!=` do?

It checks value inequality.

```python
print("mouse" != "keyboard")
```

### 15. What are logical operators?

`and`, `or`, and `not`.

```python
print(True and False)
```

## Intermediate Level

### 16. What does `and` return?

It returns the first falsey value, or the last value if all are truthy.

```python
print("laptop" and "mouse")
```

### 17. What does `or` return?

It returns the first truthy value, or the last value if all are falsey.

```python
print("" or "default")
```

### 18. What does `not` return?

It returns a boolean negation.

```python
print(not [])
```

### 19. What is short-circuit evaluation?

Python stops evaluating as soon as the result is known.

```python
cart = []
print(cart and cart[0])
```

### 20. What are identity operators?

`is` and `is not` check object identity.

```python
discount = None
print(discount is None)
```

### 21. What is the difference between `==` and `is`?

`==` compares values. `is` compares whether two references point to the same object.

### 22. When should you use `is None`?

Use it when checking for the singleton `None`.

```python
discount = None
print(discount is None)
```

### 23. What are membership operators?

`in` and `not in`.

```python
cart = ["laptop", "mouse"]
print("mouse" in cart)
```

### 24. What does `in` check in a dictionary?

It checks keys.

```python
prices = {"laptop": 999}
print("laptop" in prices)
```

### 25. What is the time complexity of `in` for a list?

**O(n)** because it may scan the list.

### 26. What is the time complexity of `in` for a set?

Average **O(1)** due to hashing.

### 27. What is chained comparison?

Python lets you write comparisons like math notation.

```python
price = 500
print(100 <= price <= 1000)
```

### 28. What is operator precedence?

Rules that decide which operator runs first.

```python
print(10 + 2 * 3)
```

### 29. How do you override precedence?

Use parentheses.

```python
print((10 + 2) * 3)
```

### 30. What is the precedence of `and` vs `or`?

`and` has higher precedence than `or`.

```python
print(True or False and False)
```

## Advanced Level

### 31. What are bitwise operators?

Operators that work on integer bits: `&`, `|`, `^`, `~`, `<<`, `>>`.

### 32. What does bitwise AND `&` do?

It keeps bits set in both numbers.

```python
print(6 & 3)
```

### 33. What does bitwise OR `|` do?

It keeps bits set in either number.

```python
print(4 | 2)
```

### 34. What does bitwise XOR `^` do?

It keeps bits set in exactly one number.

```python
print(5 ^ 3)
```

### 35. What does bitwise NOT `~` do?

It flips bits using Python's signed integer representation rules.

```python
print(~5)
```

### 36. What does left shift `<<` do?

It shifts bits left, often equivalent to multiplying by powers of two.

```python
print(3 << 1)
```

### 37. What does right shift `>>` do?

It shifts bits right, often equivalent to floor division by powers of two for non-negative integers.

```python
print(8 >> 1)
```

### 38. How do you check if a number is odd using bitwise operators?

Check the last bit.

```python
print(105 & 1 == 1)
```

### 39. How do you set a permission flag?

Use bitwise OR.

```python
READ = 1
WRITE = 2
permission = READ | WRITE
```

### 40. How do you check a permission flag?

Use bitwise AND.

```python
print(permission & READ != 0)
```

### 41. How do you toggle a flag?

Use XOR.

```python
FLAG = 1
state = 0
state ^= FLAG
```

### 42. What is the walrus operator `:=`?

It assigns and returns a value inside an expression.

```python
cart = ["laptop"]
if (count := len(cart)) > 0:
    print(count)
```

### 43. What is the ternary conditional operator?

Python uses `a if condition else b`.

```python
status = "in-stock" if 5 > 0 else "out-of-stock"
```

### 44. What is augmented assignment with mutable objects?

It can mutate the object in place.

```python
cart = ["laptop"]
alias = cart
cart += ["mouse"]
print(alias)
```

### 45. What is the difference between `a = a + b` and `a += b`?

For immutable values they often behave similarly. For mutable objects, `+=` may mutate in place.

## Pro Level

### 46. Can operators be overloaded in Python?

Yes. Classes can define special methods like `__add__`, `__eq__`, and `__contains__`.

### 47. Which method powers `+`?

`__add__`.

```python
print((10).__add__(5))
```

### 48. Which method powers `in`?

Usually `__contains__`, with iteration fallback.

### 49. Which method powers `==`?

`__eq__`.

### 50. Why can `True == 1`?

`bool` is a subclass of `int`.

```python
print(True == 1)
```

### 51. Why should you avoid `is` for string comparison?

`is` checks identity, not value. Use `==`.

### 52. Why can `x or default` be dangerous?

It replaces valid falsey values like `0`, `False`, or `""`.

```python
discount = 0
print(discount or 10)
```

### 53. What is the safest way to default only missing values?

Check `is None`.

```python
discount = None
if discount is None:
    discount = 10
```

### 54. What is De Morgan's law?

`not (A and B)` equals `(not A) or (not B)`.

### 55. What is the difference between logical `and` and bitwise `&`?

`and` checks truthiness and short-circuits. `&` works on bits or overloaded objects and does not short-circuit.

### 56. What is the difference between logical `or` and bitwise `|`?

`or` checks truthiness and short-circuits. `|` combines bits or overloaded objects.

### 57. Why can `&` work with sets?

Sets overload `&` for intersection.

```python
print({"laptop", "mouse"} & {"mouse"})
```

### 58. Why can `|` work with sets and dicts?

Sets use `|` for union. Modern dictionaries use `|` for merge.

```python
print({"a"} | {"b"})
print({"a": 1} | {"b": 2})
```

### 59. How should you explain operator precedence in interviews?

Know common cases but prefer parentheses for readability.

### 60. What makes operator-heavy code good?

Correctness first, then readability. Avoid clever expressions that hide intent.

## Final Interview Checklist

- Know `/` vs `//` vs `%`.
- Know `==` vs `is`.
- Use `is None` for `None`.
- Know `and` / `or` return operands and short-circuit.
- Know `in` performance depends on container.
- Know bitwise operators for flags and masks.
- Know chained comparisons.
- Use parentheses for clarity.
- Avoid `x or default` when falsey values are valid.

## See also

- [Python operators: core concepts](core-concepts.md)
- [Python operator reference](operator-reference.md)
- [Python operator interview problems](interview-problems.md)
- [Python boolean FAQ](../bool/frequently-asked-questions.md)
