# Python Functions: Frequently Asked Interview Questions

This page collects frequently asked Python function interview questions from **basic** to **pro** level. Examples use online computer shopping system ideas like carts, products, discounts, inventory, and orders.

## Basic Level

### 1. What is a function in Python?

A function is a reusable block of code that performs a task.

```python
def greet():
    print("Welcome")
```

### 2. How do you define a function?

Use the `def` keyword.

```python
def show_product(name):
    print(name)
```

### 3. How do you call a function?

Use the function name followed by parentheses.

```python
show_product("laptop")
```

### 4. What is a parameter?

A parameter is a variable in the function definition.

```python
def show_product(name):
    print(name)
```

### 5. What is an argument?

An argument is the actual value passed to a function.

```python
show_product("mouse")
```

### 6. What is the difference between parameter and argument?

The parameter is in the function definition. The argument is passed during the function call.

### 7. What does `return` do?

It sends a value back to the caller.

```python
def total(price, quantity):
    return price * quantity
```

### 8. What does a function return if there is no `return`?

It returns `None`.

```python
def log_order(order_id):
    print(order_id)

print(log_order("ORD-1"))  # None
```

### 9. Can a function return multiple values?

Yes. Python returns them as a tuple.

```python
def price_range():
    return 25, 999
```

### 10. What is a default parameter?

A fallback value used when an argument is not provided.

```python
def discount(price, percent=10):
    return price - price * percent / 100
```

### 11. What is a positional argument?

An argument matched by position.

```python
def total(price, quantity):
    return price * quantity

total(999, 2)
```

### 12. What is a keyword argument?

An argument matched by name.

```python
total(quantity=2, price=999)
```

### 13. Can a function have both positional and keyword arguments?

Yes.

```python
total(999, quantity=2)
```

### 14. What is function scope?

Scope defines where a variable can be accessed.

```python
def f():
    x = 10

# print(x)  # NameError
```

### 15. What is a docstring?

A string that documents a function.

```python
def total(price, quantity):
    """Return total price."""
    return price * quantity
```

## Intermediate Level

### 16. What is `*args`?

`*args` collects extra positional arguments into a tuple.

```python
def total_prices(*prices):
    return sum(prices)
```

### 17. What is `**kwargs`?

`**kwargs` collects extra keyword arguments into a dictionary.

```python
def filters(**kwargs):
    return kwargs
```

### 18. What is the difference between `*args` and `**kwargs`?

`*args` is for positional arguments. `**kwargs` is for keyword arguments.

### 19. What is argument unpacking with `*`?

It unpacks a list/tuple into positional arguments.

```python
values = [999, 2]
total(*values)
```

### 20. What is argument unpacking with `**`?

It unpacks a dictionary into keyword arguments.

```python
data = {"price": 999, "quantity": 2}
total(**data)
```

### 21. What is a keyword-only argument?

An argument that must be passed by name.

```python
def checkout(price, *, tax=0):
    return price + price * tax / 100
```

### 22. What is a positional-only argument?

An argument that must be passed by position, marked before `/`.

```python
def apply_tax(price, /, tax):
    return price + price * tax / 100
```

### 23. What is the mutable default argument problem?

Mutable defaults are created once and shared between calls.

```python
def bad(item, cart=[]):
    cart.append(item)
    return cart
```

### 24. How do you fix mutable default arguments?

Use `None` and create the mutable object inside.

```python
def good(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart
```

### 25. What is a pure function?

A function that depends only on inputs and has no side effects.

```python
def discount(price, percent):
    return price - price * percent / 100
```

### 26. What is a side effect?

A side effect changes external state or performs I/O.

```python
def add_to_cart(cart, item):
    cart.append(item)
```

### 27. Are functions first-class objects in Python?

Yes. They can be assigned to variables, passed, and returned.

```python
def is_expensive(product):
    return product["price"] > 100

check = is_expensive
```

### 28. What is a lambda function?

A small anonymous function.

```python
is_expensive = lambda product: product["price"] > 100
```

### 29. When should you avoid lambda?

Avoid lambda when logic is complex or hurts readability.

### 30. What are type hints in functions?

Annotations that describe expected input and output types.

```python
def total(price: float, quantity: int) -> float:
    return price * quantity
```

## Advanced Level

### 31. What is a higher-order function?

A function that accepts or returns another function.

```python
def filter_items(items, condition):
    return [item for item in items if condition(item)]
```

### 32. What is a closure?

A closure is a function that remembers variables from an outer scope.

```python
def make_discount(percent):
    def apply(price):
        return price - price * percent / 100
    return apply

ten_percent = make_discount(10)
```

### 33. What is recursion?

A function calling itself.

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

### 34. What is a base case?

The condition that stops recursion.

### 35. What happens without a base case?

The function may recurse until `RecursionError`.

### 36. Does Python optimize tail recursion?

No. Python does not perform tail-call optimization.

### 37. What is `global`?

`global` lets a function assign to a module-level variable.

```python
count = 0

def increment():
    global count
    count += 1
```

### 38. What is `nonlocal`?

`nonlocal` lets an inner function assign to a variable in an enclosing function.

```python
def counter():
    count = 0

    def inc():
        nonlocal count
        count += 1
        return count

    return inc
```

### 39. What is LEGB scope?

Python name lookup order: Local, Enclosing, Global, Built-in.

### 40. What is function annotation?

Metadata stored in `__annotations__`.

```python
def total(price: float) -> float:
    return price

print(total.__annotations__)
```

### 41. What is a decorator?

A function that wraps another function to extend behavior.

```python
def log_call(func):
    def wrapper(*args, **kwargs):
        print("Calling function")
        return func(*args, **kwargs)
    return wrapper
```

### 42. What is `functools.wraps`?

It preserves metadata like function name and docstring in decorators.

```python
from functools import wraps
```

### 43. What is memoization?

Caching function results to avoid repeated work.

```python
cache = {}

def get_score(product_id):
    if product_id not in cache:
        cache[product_id] = product_id * 10
    return cache[product_id]
```

### 44. What is `lru_cache`?

A decorator that caches function results.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
```

### 45. What is a generator function?

A function that uses `yield` to produce values lazily.

```python
def product_ids():
    yield 101
    yield 102
```

## Pro Level

### 46. What is the difference between `return` and `yield`?

`return` ends a function and sends one result. `yield` pauses a generator and can produce multiple values lazily.

### 47. What is late binding in closures?

Inner functions capture variables by reference, not by value.

```python
funcs = []
for discount in [10, 20]:
    funcs.append(lambda price: price - price * discount / 100)
```

### 48. How do you fix late binding in lambdas?

Bind the value as a default argument.

```python
funcs = []
for discount in [10, 20]:
    funcs.append(lambda price, discount=discount: price - price * discount / 100)
```

### 49. What is dependency injection with functions?

Passing behavior or dependencies into a function instead of hardcoding them.

```python
def checkout(cart, tax_calculator):
    return tax_calculator(cart)
```

### 50. Why should functions be small?

Small functions are easier to test, reuse, debug, and explain in interviews.

### 51. What is idempotent function behavior?

Calling it multiple times with the same input produces the same final effect/result.

### 52. What is a predicate function?

A function that returns `True` or `False`.

```python
def is_in_stock(product):
    return product["stock"] > 0
```

### 53. What is a callback?

A function passed to another function to be called later.

### 54. What is function composition?

Combining functions so output of one becomes input to another.

```python
def add_tax(price):
    return price * 1.08

def apply_discount(price):
    return price * 0.9
```

### 55. What is an inner function?

A function defined inside another function.

### 56. Why use inner functions?

For helper logic, closures, decorators, or hiding implementation details.

### 57. Can functions be stored in dictionaries?

Yes. This is useful for dispatch tables.

```python
actions = {
    "discount": lambda price: price * 0.9,
    "tax": lambda price: price * 1.08,
}
```

### 58. What is a dispatch table?

A dictionary mapping keys to functions.

### 59. Why avoid too many arguments?

Too many arguments make functions hard to read and call correctly.

### 60. What should you say if asked “what makes a good function?”

A good function has a clear name, small scope, clear inputs/outputs, minimal side effects, and tests for edge cases.

## Final Interview Checklist

- Know parameter vs argument.
- Know `return`, default parameters, `*args`, and `**kwargs`.
- Explain mutable default argument pitfalls.
- Understand scope, LEGB, `global`, and `nonlocal`.
- Know pure functions vs side effects.
- Know higher-order functions, closures, decorators, recursion, and generators.
- Prefer clear names, small functions, and explicit return values.

## See also

- [Python functions: core concepts](core-concepts.md)
- [Python function parameters](parameters-and-arguments.md)
- [Python function interview problems](interview-problems.md)
- [Python dictionary FAQ](../dict/frequently-asked-questions.md)
