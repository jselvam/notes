# Python NoneType: Frequently Asked Interview Questions

This page collects frequently asked Python `None` / `NoneType` interview questions from **basic** to **pro** level.

## Basic Level

### 1. What is `None` in Python?

`None` represents no value or missing value.

```python
discount = None
```

### 2. What is the type of `None`?

The type is `NoneType`.

```python
print(type(None))
```

### 3. Is `None` a keyword?

Yes. `None` is a Python keyword-like singleton constant.

### 4. Can you assign a new value to `None`?

No.

```python
# None = 10  # SyntaxError
```

### 5. How many `None` objects exist?

Only one. `None` is a singleton.

```python
print(None is None)
```

### 6. How do you check for `None`?

Use `is None`.

```python
value = None
print(value is None)
```

### 7. How do you check not None?

Use `is not None`.

```python
value = 0
print(value is not None)
```

### 8. Should you use `== None`?

No. Prefer `is None`.

### 9. Is `None` falsey?

Yes.

```python
print(bool(None))
```

### 10. Is `None` equal to `False`?

No.

```python
print(None == False)
```

### 11. Is `None` equal to `0`?

No.

```python
print(None == 0)
```

### 12. Is `None` equal to an empty string?

No.

```python
print(None == "")
```

### 13. What does a function return without `return`?

It returns `None`.

```python
def log():
    print("log")

print(log())
```

### 14. What does a bare `return` return?

It returns `None`.

```python
def stop():
    return

print(stop())
```

### 15. Can a function explicitly return `None`?

Yes.

```python
def not_found():
    return None
```

## Intermediate Level

### 16. When should a function return `None`?

When no meaningful value is found or available.

```python
def find_product(products, target):
    return None
```

### 17. What is an optional return?

A function that may return a value or `None`.

```python
def find_price(product_id) -> float | None:
    return None
```

### 18. What is `Optional[int]`?

It means `int` or `None`.

```python
from typing import Optional

def find_id() -> Optional[int]:
    return None
```

### 19. What does `int | None` mean?

It is modern syntax meaning `int` or `None`.

```python
def find_id() -> int | None:
    return None
```

### 20. Why is `None` useful as a default parameter?

It avoids mutable default argument bugs.

```python
def add_item(item, cart=None):
    if cart is None:
        cart = []
```

### 21. Why is `cart=[]` dangerous as a default?

The same list is reused across calls.

### 22. How do you fix mutable default arguments?

Use `None`, then create the object inside.

### 23. What is the difference between missing and empty?

Missing can be `None`; empty can be `""`, `[]`, `{}`, or `0`, depending on context.

### 24. Why is `discount or 10` risky?

It treats valid falsey values like `0` as missing.

```python
discount = 0
print(discount or 10)
```

### 25. How do you default only when value is `None`?

Use `is None`.

```python
if discount is None:
    discount = 10
```

### 26. What does `dict.get()` return by default?

It returns `None` if the key is missing.

```python
prices = {}
print(prices.get("laptop"))
```

### 27. Why can `dict.get()` be ambiguous?

The key may exist with value `None`, or the key may be missing.

```python
config = {"discount": None}
print(config.get("discount"))
print(config.get("tax"))
```

### 28. How do you distinguish missing key from value `None`?

Use a sentinel object.

```python
MISSING = object()
value = config.get("tax", MISSING)
```

### 29. Can `None` be a dictionary key?

Yes.

```python
data = {None: "missing"}
```

### 30. Can `None` be in a set?

Yes.

```python
values = {None, 1, 2}
```

## Advanced Level

### 31. Why use `is None` instead of `== None`?

`None` is a singleton. `is` checks identity and avoids custom equality surprises.

### 32. Can custom `__eq__` make `== None` behave strangely?

Yes, which is another reason to use `is None`.

```python
class Weird:
    def __eq__(self, other):
        return True

print(Weird() == None)
```

### 33. What is a sentinel object?

A unique object used to represent “not provided” or “missing”.

```python
MISSING = object()
```

### 34. Why use a sentinel instead of `None`?

Because `None` may be a valid value.

### 35. What is a common use of `None` in linked lists?

`None` marks the end of the list.

```python
node.next = None
```

### 36. What is a common use of `None` in trees?

`None` marks a missing child.

```python
root.left = None
```

### 37. Is `None` hashable?

Yes.

```python
print(hash(None))
```

### 38. Can `None` be serialized to JSON?

Yes. Python `None` becomes JSON `null`.

```python
import json

print(json.dumps({"discount": None}))
```

### 39. What does JSON `null` become in Python?

It becomes `None`.

```python
import json

print(json.loads('{"discount": null}'))
```

### 40. What is the difference between `None` and `NotImplemented`?

`None` means no value. `NotImplemented` is used by special methods to signal unsupported operations.

### 41. What is the difference between `None` and `Ellipsis`?

`None` means no value. `Ellipsis` (`...`) is a separate singleton often used as placeholder or in slicing libraries.

### 42. What is a common bug with API data and `None`?

Assuming a field exists or is not `None` before accessing methods on it.

```python
name = None
# name.lower()  # AttributeError
```

### 43. How do you safely call a method on a maybe-None value?

Check first.

```python
if name is not None:
    name = name.lower()
```

### 44. How do you use `None` with `match`?

Match it directly.

```python
match None:
    case None:
        print("missing")
```

### 45. How does `None` differ from empty list in return values?

`None` can mean no result; empty list can mean result exists but has no items.

## Pro Level

### 46. Is `None` garbage collected?

`None` is a process-wide singleton and always exists while Python runs.

### 47. Can `None` have attributes?

No useful custom attributes can be assigned to `None`.

### 48. Why is `None` often used for default arguments?

It is immutable, singleton, and clearly means “not provided” in many APIs.

### 49. When should you avoid returning `None`?

Avoid it when exceptions, empty collections, or result objects communicate failure more clearly.

### 50. When should you raise an exception instead of returning `None`?

When absence is unexpected or should stop the flow.

### 51. When should you return an empty list instead of `None`?

When the function logically returns a collection and there are simply no results.

```python
def find_products():
    return []
```

### 52. When should you return `None` instead of empty list?

When there is no meaningful collection or the requested object does not exist.

### 53. How do type checkers help with `None`?

They can warn when you use a maybe-None value without checking.

### 54. What is `None` in optional chaining?

Python does not have JavaScript-style optional chaining; check explicitly or use helper logic.

### 55. Why can `if value:` be wrong for optional values?

It treats all falsey values as missing.

### 56. What is better than multiple None checks?

Refactor with guard clauses, helper functions, or clear data models.

### 57. How do guard clauses work with `None`?

Return early when required value is missing.

```python
def checkout(payment_method):
    if payment_method is None:
        return "missing payment"
    return "ok"
```

### 58. What is a good boolean function name for None checks?

Use names like `has_payment_method`, `is_missing`, or `is_configured`.

### 59. What is the biggest NoneType interview trap?

Confusing `None` with other falsey values like `0`, `False`, `""`, or `[]`.

### 60. What should you say if asked “How do you handle None safely?”

Use `is None`, distinguish missing from falsey, type hint optional values, and choose between `None`, empty result, sentinel, or exception based on meaning.

## Final Interview Checklist

- `None` means no value / missing value.
- `type(None)` is `NoneType`.
- Use `is None` and `is not None`.
- A function without `return` returns `None`.
- Use `None` for safe mutable defaults.
- Do not confuse `None` with `0`, `False`, `""`, or `[]`.
- Use `T | None` or `Optional[T]` for optional return values.
- Use a sentinel object when `None` is a valid value.
- JSON `null` maps to Python `None`.

## See also

- [Python NoneType core concepts](core-concepts.md)
- [Python NoneType operations](operations-and-patterns.md)
- [Python NoneType interview problems](interview-problems.md)
- [Python boolean FAQ](../bool/frequently-asked-questions.md)
