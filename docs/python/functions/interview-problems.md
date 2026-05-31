# Python Function Interview Problems

Function interview problems test whether you can break logic into reusable pieces, handle edge cases, return values clearly, and avoid common bugs like mutable default arguments.

## Interview Pattern: When to Think About Functions

Use functions to:

- reduce repeated code
- isolate business logic
- return testable results
- split a big problem into smaller parts
- pass behavior into other functions
- solve recursion or closure questions

## 1. Calculate Cart Total

### Problem

Write a function that takes product prices and returns the total.

### Python Solution

```python
def cart_total(prices):
    total = 0

    for price in prices:
        total += price

    return total


print(cart_total([999, 25, 75]))
# 1099
```

### Complexity

- Time: **O(n)**
- Space: **O(1)**

## 2. Apply Discount

### Problem

Write a function that applies a percentage discount to a price.

### Python Solution

```python
def apply_discount(price, discount_percent=10):
    return price - (price * discount_percent / 100)


print(apply_discount(1000))
print(apply_discount(1000, 20))
```

### Complexity

- Time: **O(1)**
- Space: **O(1)**

## 3. Check Product Availability

### Problem

Write a function that checks whether a product has stock greater than zero.

### Python Solution

```python
def is_available(inventory, product_id):
    return inventory.get(product_id, 0) > 0


inventory = {101: 5, 102: 0}

print(is_available(inventory, 101))  # True
print(is_available(inventory, 102))  # False
```

### Complexity

- Time: **O(1)** average dictionary lookup
- Space: **O(1)**

## 4. Return Min and Max Price

### Problem

Return both the lowest and highest prices.

### Python Solution

```python
def min_max_price(prices):
    if not prices:
        return None

    minimum = prices[0]
    maximum = prices[0]

    for price in prices[1:]:
        if price < minimum:
            minimum = price
        if price > maximum:
            maximum = price

    return minimum, maximum


print(min_max_price([999, 25, 75, 199]))
```

### Complexity

- Time: **O(n)**
- Space: **O(1)**

## 5. Count Products by Category

### Problem

Write a function that counts how many products belong to each category.

### Python Solution

```python
def count_by_category(products):
    counts = {}

    for product in products:
        category = product["category"]
        counts[category] = counts.get(category, 0) + 1

    return counts


products = [
    {"name": "laptop", "category": "hardware"},
    {"name": "mouse", "category": "hardware"},
    {"name": "office-suite", "category": "software"},
]

print(count_by_category(products))
```

### Complexity

- Time: **O(n)**
- Space: **O(k)** categories

## 6. Fix Mutable Default Cart

### Problem

Fix a function that accidentally shares the same default cart list across calls.

### Bad Code

```python
def add_to_cart_bad(item, cart=[]):
    cart.append(item)
    return cart
```

### Correct Solution

```python
def add_to_cart(item, cart=None):
    if cart is None:
        cart = []

    cart.append(item)
    return cart


print(add_to_cart("laptop"))
print(add_to_cart("mouse"))
```

### Interview Point

Default values are created once when the function is defined.

## 7. Build a Function That Accepts Any Number of Prices

### Problem

Use `*args` to calculate total for any number of prices.

### Python Solution

```python
def total_prices(*prices):
    return sum(prices)


print(total_prices(999, 25, 75))
```

### Complexity

- Time: **O(n)**
- Space: **O(1)** extra

## 8. Filter Products With `**kwargs`

### Problem

Write a function that filters products by optional keyword filters.

### Python Solution

```python
def matches_filters(product, **filters):
    for key, expected_value in filters.items():
        if product.get(key) != expected_value:
            return False
    return True


product = {"name": "laptop", "category": "hardware", "in_stock": True}

print(matches_filters(product, category="hardware", in_stock=True))
```

### Complexity

- Time: **O(k)** filters
- Space: **O(1)**

## 9. Higher-Order Function for Product Filtering

### Problem

Write a function that accepts another function as a condition.

### Python Solution

```python
def filter_products(products, condition):
    result = []

    for product in products:
        if condition(product):
            result.append(product)

    return result


products = [
    {"name": "laptop", "price": 999},
    {"name": "mouse", "price": 25},
]

expensive = filter_products(products, lambda product: product["price"] >= 100)
print(expensive)
```

### Interview Point

Functions are first-class objects in Python.

## 10. Recursive Factorial

### Problem

Write factorial using recursion.

### Python Solution

```python
def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))
```

### Complexity

- Time: **O(n)**
- Space: **O(n)** call stack

## Summary: Function Patterns to Remember

| Pattern | Function idea | Example |
|---------|---------------|---------|
| Pure function | returns only from inputs | discount calculation |
| Multiple return | returns tuple | min and max price |
| Default parameter | optional value | default discount |
| `*args` | variable positional values | total of many prices |
| `**kwargs` | flexible named filters | product filters |
| Higher-order function | function as argument | filtering |
| Recursion | function calls itself | factorial |

## See also

- [Python functions: core concepts](core-concepts.md)
- [Python function parameters](parameters-and-arguments.md)
- [Python function FAQ](frequently-asked-questions.md)
- [Python dictionary interview problems](../dict/interview-problems.md)
