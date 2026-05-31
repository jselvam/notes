# Python Boolean: Frequently Asked Interview Questions

This page collects frequently asked Python `bool` interview questions from **basic** to **pro** level. Examples use online computer shopping system ideas like carts, coupons, stock, checkout, and feature flags.

## Basic Level

### 1. What is a boolean in Python?

A boolean represents truth: `True` or `False`.

```python
is_in_stock = True
```

### 2. What are the two boolean values?

`True` and `False`.

```python
print(True)
print(False)
```

### 3. Are `true` and `false` valid Python booleans?

No. Python uses capitalized `True` and `False`.

```python
# true  # NameError
```

### 4. What is the type of `True`?

`bool`.

```python
print(type(True))
```

### 5. How do you create a boolean from comparison?

Use comparison operators.

```python
print(5 > 2)
```

### 6. What does `bool()` do?

It converts a value to its truthiness.

```python
print(bool("laptop"))
```

### 7. What is a truthy value?

A value treated as true in conditions.

```python
print(bool(["laptop"]))  # True
```

### 8. What is a falsey value?

A value treated as false in conditions.

```python
print(bool([]))  # False
```

### 9. Is an empty string truthy or falsey?

Falsey.

```python
print(bool(""))
```

### 10. Is a non-empty string truthy?

Yes.

```python
print(bool("mouse"))
```

### 11. Is zero truthy or falsey?

Zero is falsey.

```python
print(bool(0))
```

### 12. Is a non-zero number truthy?

Yes.

```python
print(bool(-1))
```

### 13. Is an empty list falsey?

Yes.

```python
print(bool([]))
```

### 14. How do you check if a cart is empty?

Use `if not cart`.

```python
cart = []
if not cart:
    print("empty")
```

### 15. How do you check if a cart has items?

Use `if cart`.

```python
cart = ["laptop"]
if cart:
    print("has items")
```

## Intermediate Level

### 16. What does `and` do?

It returns the first falsey value, or the last value if all are truthy.

```python
print(True and "checkout")
```

### 17. What does `or` do?

It returns the first truthy value, or the last value if all are falsey.

```python
print("" or "WELCOME10")
```

### 18. What does `not` do?

It negates truthiness and returns a real boolean.

```python
print(not [])
```

### 19. Does `and` always return `True` or `False`?

No. It returns one of the original operands.

```python
print("laptop" and "mouse")
```

### 20. Does `or` always return `True` or `False`?

No. It returns one of the original operands.

```python
print("" or "default")
```

### 21. What is short-circuit evaluation?

Python stops evaluating once the final result is known.

```python
cart = []
print(cart and cart[0])
```

### 22. Why is short-circuiting useful?

It avoids unnecessary work and can prevent errors.

```python
cart = []
if cart and cart[0] == "laptop":
    print("first")
```

### 23. What is `any()`?

It returns `True` if any item is truthy.

```python
print(any([False, False, True]))
```

### 24. What is `all()`?

It returns `True` if all items are truthy.

```python
print(all([True, True, False]))
```

### 25. What does `any([])` return?

`False`.

```python
print(any([]))
```

### 26. What does `all([])` return?

`True`.

```python
print(all([]))
```

### 27. How do you check a price range?

Use chained comparison.

```python
price = 500
print(100 <= price <= 1000)
```

### 28. What is the difference between `==` and `is`?

`==` compares values. `is` compares identity.

### 29. Should you write `if is_active == True`?

Usually no. Prefer `if is_active`.

```python
if True:
    print("active")
```

### 30. How should you check for `None`?

Use `is None`.

```python
discount = None
print(discount is None)
```

## Advanced Level

### 31. Is `bool` a subclass of `int`?

Yes.

```python
print(isinstance(True, int))
```

### 32. What is `True + True`?

`2`.

```python
print(True + True)
```

### 33. Why is `True == 1`?

Because `bool` behaves like integers `1` and `0`.

```python
print(True == 1)
```

### 34. Why can `True` and `1` collide as dictionary keys?

They are equal and have the same hash.

```python
data = {True: "yes", 1: "one"}
print(data)
```

### 35. How do you count true values?

Use `sum()` on booleans.

```python
print(sum([True, False, True]))
```

### 36. What is the danger of `x or default`?

It replaces valid falsey values like `0`, `False`, or `""`.

```python
discount = 0
print(discount or 10)
```

### 37. How do you safely default only when value is `None`?

Use `is None`.

```python
def default_discount(discount):
    return 10 if discount is None else discount
```

### 38. What is De Morgan's law?

`not (A and B)` is same as `(not A) or (not B)`.

```python
is_logged_in = True
has_cart = False
print(not (is_logged_in and has_cart))
```

### 39. How can booleans simplify filtering?

Use boolean fields directly in conditions.

```python
products = [{"active": True}, {"active": False}]
print([p for p in products if p["active"]])
```

### 40. How do comparison operators chain?

Python evaluates chained comparisons naturally.

```python
print(1 < 5 < 10)
```

### 41. Does chained comparison evaluate the middle expression once?

Yes. `a < b < c` evaluates `b` once.

### 42. What is operator precedence for `not`, `and`, `or`?

`not` has higher precedence than `and`, and `and` has higher precedence than `or`.

```python
print(True or False and False)
```

### 43. How do you make boolean expressions readable?

Use meaningful variable names and helper functions.

```python
can_checkout = is_logged_in and bool(cart_items) and payment_method is not None
```

### 44. When should a function return boolean?

When it answers a yes/no question.

```python
def is_in_stock(stock_count):
    return stock_count > 0
```

### 45. What is a predicate function?

A function that returns `True` or `False`.

## Pro Level

### 46. Why does `all([])` return `True`?

It is vacuously true: no element violates the condition.

### 47. Why does `any([])` return `False`?

There is no truthy element.

### 48. How do `any()` and `all()` short-circuit?

`any()` stops at first truthy value. `all()` stops at first falsey value.

```python
print(any([False, True, True]))
print(all([True, False, True]))
```

### 49. How can booleans improve guard clauses?

Return early when conditions fail.

```python
def can_checkout(user, cart):
    if not user:
        return False
    if not cart:
        return False
    return True
```

### 50. Why avoid overly clever boolean expressions?

They become hard to read and easy to break.

### 51. How do you name boolean variables?

Use prefixes like `is_`, `has_`, `can_`, `should_`.

```python
is_active = True
has_stock = True
can_checkout = False
```

### 52. What is the difference between boolean flag and enum/status?

A boolean has two states. Use enum/status when there are more than two meaningful states.

```python
status = "pending"  # better than multiple booleans for order state
```

### 53. When can multiple booleans become a problem?

When combinations create invalid states.

```python
is_paid = True
is_refunded = True  # possible, but needs domain rules
```

### 54. How do booleans relate to feature flags?

Feature flags often use booleans to enable/disable behavior.

```python
enable_new_checkout = True
```

### 55. How should booleans be stored in JSON?

JSON uses lowercase `true` and `false`, but Python uses `True` and `False`.

### 56. What is a common API bug with booleans?

Treating string `"false"` as false. Non-empty strings are truthy in Python.

```python
print(bool("false"))  # True
```

### 57. How do you parse boolean strings safely?

Compare normalized text to allowed values.

```python
def parse_bool(value):
    return value.strip().lower() in {"true", "1", "yes"}
```

### 58. Why should boolean expressions avoid side effects?

Short-circuiting may skip side-effect function calls, causing surprising behavior.

### 59. What should you say if asked “bool or int flag?”

Use `bool` for true/false meaning. Use `int` only when numeric operations or counts are intended.

### 60. What makes good boolean code?

Clear names, direct conditions, simple expressions, and explicit handling of `None` when needed.

## Final Interview Checklist

- Python booleans are `True` and `False`.
- Empty containers, zero, `None`, and empty strings are falsey.
- `and` / `or` return operands, not always booleans.
- `not` returns a real boolean.
- Use `if value`, `if not value`, and `is None` idiomatically.
- `any()` and `all()` short-circuit.
- `bool` is a subclass of `int`.
- Be careful with `x or default` when `0` or `False` is valid.
- Avoid over-complicated boolean expressions.

## See also

- [Python boolean core concepts](core-concepts.md)
- [Python boolean operations](operations-and-truthiness.md)
- [Python boolean interview problems](interview-problems.md)
- [Python numeric FAQ](../numbers/frequently-asked-questions.md)
