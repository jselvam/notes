# Python Control Flow: Frequently Asked Interview Questions

This page collects frequently asked Python control-flow interview questions from **basic** to **pro** level. It covers `if` / `elif` / `else`, `for`, `while`, loop control, loop `else`, and `match`.

## Basic Level

### 1. What is control flow?

Control flow decides which code runs and how many times it runs.

```python
if True:
    print("run")
```

### 2. What does `if` do?

`if` runs a block only when a condition is truthy.

```python
stock = 5
if stock > 0:
    print("in stock")
```

### 3. What does `else` do?

`else` runs when the `if` condition is false.

```python
stock = 0
if stock > 0:
    print("in stock")
else:
    print("out of stock")
```

### 4. What does `elif` do?

`elif` checks another condition after the previous condition fails.

```python
price = 500
if price >= 1000:
    print("premium")
elif price >= 100:
    print("standard")
else:
    print("budget")
```

### 5. Can an `if` have multiple `elif` blocks?

Yes.

```python
status = "paid"
if status == "pending":
    print("wait")
elif status == "paid":
    print("ship")
elif status == "cancelled":
    print("stop")
```

### 6. Is `else` required?

No. Use it only when you need a fallback branch.

### 7. What is a nested `if`?

An `if` inside another `if`.

```python
if True:
    if True:
        print("nested")
```

### 8. What is a `for` loop?

A loop that iterates over an iterable.

```python
for item in ["laptop", "mouse"]:
    print(item)
```

### 9. What is a `while` loop?

A loop that repeats while a condition is truthy.

```python
stock = 3
while stock > 0:
    stock -= 1
```

### 10. What is `range()` used for?

`range()` creates a sequence of numbers for looping.

```python
for i in range(3):
    print(i)
```

### 11. What is `break`?

`break` exits the nearest loop.

```python
for item in ["mouse", "laptop"]:
    if item == "laptop":
        break
```

### 12. What is `continue`?

`continue` skips the rest of the current iteration.

```python
for stock in [5, 0, 3]:
    if stock == 0:
        continue
    print(stock)
```

### 13. What is `pass`?

`pass` is a placeholder that does nothing.

```python
if True:
    pass
```

### 14. What is `enumerate()`?

`enumerate()` gives index and value while looping.

```python
for index, item in enumerate(["laptop", "mouse"]):
    print(index, item)
```

### 15. How do you loop over dictionary items?

Use `.items()`.

```python
prices = {"laptop": 999}
for product, price in prices.items():
    print(product, price)
```

## Intermediate Level

### 16. When should you use `for`?

Use `for` when iterating over known items or an iterable.

### 17. When should you use `while`?

Use `while` when repeating until a condition changes.

### 18. What is an infinite loop?

A loop whose condition never becomes false.

```python
# while True:
#     print("forever")
```

### 19. How do you avoid infinite `while` loops?

Update the condition variable or use `break` with a clear condition.

```python
attempts = 0
while attempts < 3:
    attempts += 1
```

### 20. What is loop `else`?

Loop `else` runs when a loop finishes without `break`.

```python
for item in ["mouse"]:
    if item == "laptop":
        break
else:
    print("not found")
```

### 21. Does loop `else` run after `break`?

No.

### 22. Does loop `else` mean the loop condition was false?

No. It means no `break` happened.

### 23. What is a common use of loop `else`?

Search problems where you want a “not found” block.

### 24. Can `break` be used outside a loop?

No. It causes a syntax error.

### 25. Can `continue` be used outside a loop?

No. It causes a syntax error.

### 26. What is the difference between `break` and `return` inside a loop?

`break` exits the loop. `return` exits the entire function.

### 27. What is the difference between `continue` and `pass`?

`continue` skips to the next iteration. `pass` does nothing and execution continues normally.

### 28. How do you skip out-of-stock products?

Use `continue`.

```python
for product in products:
    if product["stock"] == 0:
        continue
    print(product)
```

### 29. How do you stop after finding a product?

Use `break` or `return`.

```python
for item in cart:
    if item == "laptop":
        break
```

### 30. How do you loop with index without `range(len(...))`?

Use `enumerate()`.

```python
for index, item in enumerate(cart):
    print(index, item)
```

## Advanced Level

### 31. What is `match`?

`match` is Python structural pattern matching.

```python
match "paid":
    case "paid":
        print("ship")
```

### 32. Is `match` a loop?

No. It is conditional pattern matching.

### 33. What is `case _`?

It is the wildcard fallback case.

```python
match "unknown":
    case _:
        print("fallback")
```

### 34. What is a guard in `match`?

A guard is an `if` condition on a `case`.

```python
match {"price": 999}:
    case {"price": price} if price > 500:
        print("premium")
```

### 35. Can `match` destructure lists?

Yes.

```python
match ["add", "laptop"]:
    case ["add", product]:
        print(product)
```

### 36. Can `match` destructure dictionaries?

Yes.

```python
match {"type": "order_paid", "id": 101}:
    case {"type": "order_paid", "id": order_id}:
        print(order_id)
```

### 37. What Python version introduced `match`?

Python 3.10.

### 38. What is the difference between `match` and `if`?

`if` checks expressions. `match` checks value/structure patterns.

### 39. What is the danger of too much nesting?

Nested conditions and loops become hard to read and maintain.

### 40. How do you reduce nested `if` statements?

Use guard clauses, helper functions, or combine simple conditions.

```python
def can_checkout(user, cart):
    if not user:
        return False
    if not cart:
        return False
    return True
```

### 41. What is a guard clause?

A guard clause exits early when a condition is not met.

### 42. What is a nested loop?

A loop inside another loop.

```python
for row in grid:
    for value in row:
        print(value)
```

### 43. What is the time complexity of nested loops?

Often **O(n²)** when both loops scale with input size.

### 44. How can you optimize nested loops?

Use a set or dictionary for fast lookup when possible.

### 45. What is a common loop bug?

Modifying a list while iterating over it.

```python
# Prefer building a new list instead.
```

## Pro Level

### 46. What is an iterator?

An object that returns values one at a time using `__next__()`.

### 47. What is an iterable?

An object that can return an iterator, such as list, tuple, dict, set, or string.

### 48. What does `iter()` do?

It returns an iterator.

```python
iterator = iter(["laptop", "mouse"])
```

### 49. What does `next()` do?

It gets the next value from an iterator.

```python
iterator = iter(["laptop"])
print(next(iterator))
```

### 50. What happens when an iterator is exhausted?

`StopIteration` is raised internally.

### 51. How does a `for` loop work internally?

It calls `iter()` and repeatedly calls `next()` until `StopIteration`.

### 52. What is a generator?

A function using `yield` that produces values lazily.

```python
def ids():
    yield 101
    yield 102
```

### 53. Why are generators useful with loops?

They avoid building a full list in memory.

### 54. What is the walrus operator useful for in loops?

Assigning while checking a condition.

```python
while (line := "data"):
    break
```

### 55. What is a common readable alternative to clever loop logic?

Use named helper functions and simple conditions.

### 56. What is the difference between `for item in list` and `for i in range(len(list))`?

Loop directly over items unless you need indexes. Use `enumerate()` when you need both.

### 57. Why should you avoid `while True` without a clear break?

It can create infinite loops and hard-to-debug code.

### 58. How do `any()` and `all()` relate to loops?

They are concise loop-like helpers for boolean checks.

```python
any_stock = any(count > 0 for count in [0, 2, 0])
```

### 59. What is the best way to search and return first match?

Use a loop with early `return`.

```python
def first_match(items, target):
    for item in items:
        if item == target:
            return item
    return None
```

### 60. What makes good control-flow code?

Clear conditions, shallow nesting, meaningful names, safe loop exits, and readable branching.

## Final Interview Checklist

- Use `if` / `elif` / `else` for branching.
- Use `for` for known iterables.
- Use `while` for condition-based repetition.
- Avoid infinite loops.
- Know `break`, `continue`, and `pass`.
- Understand loop `else`: it runs only when no `break` happens.
- Use `enumerate()` instead of `range(len(...))` when possible.
- Use `match` for structural pattern matching in Python 3.10+.
- Avoid mutating lists while iterating.
- Know nested loop complexity.

## See also

- [Python control-flow core concepts](core-concepts.md)
- [Python control-flow reference](control-flow-reference.md)
- [Python control-flow interview problems](interview-problems.md)
- [Python operators FAQ](../operators/frequently-asked-questions.md)
