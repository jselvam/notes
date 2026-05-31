# Python Functions: Core Concepts & Shopping Examples

A Python **function** is a reusable block of code that performs a specific task. Functions help make code readable, testable, and reusable.

In an online computer shopping management system, functions can handle:

- calculating cart total
- applying discounts
- checking product availability
- validating coupon codes
- formatting product names
- grouping products by category
- returning order summaries

## Basic Function Syntax

Use `def` to define a function.

```python
def greet_customer():
    print("Welcome to the computer store")


greet_customer()
```

## Function With Parameters

Parameters receive input values.

```python
def show_product(name):
    print(f"Product: {name}")


show_product("laptop")
```

## Function With Return Value

Use `return` to send a result back to the caller.

```python
def calculate_total(price, quantity):
    return price * quantity


total = calculate_total(999, 2)
print(total)
```

## Function Without Return

If a function does not return anything, Python returns `None`.

```python
def log_order(order_id):
    print(f"Order received: {order_id}")


result = log_order("ORD-1001")
print(result)  # None
```

## Default Parameters

Default values are used when an argument is not provided.

```python
def apply_discount(price, discount_percent=10):
    return price - (price * discount_percent / 100)


print(apply_discount(1000))      # 900.0
print(apply_discount(1000, 20))  # 800.0
```

## Keyword Arguments

Keyword arguments make calls more readable.

```python
def create_product(name, price, category):
    return {
        "name": name,
        "price": price,
        "category": category,
    }


product = create_product(name="laptop", price=999, category="hardware")
print(product)
```

## Multiple Return Values

Python can return multiple values as a tuple.

```python
def min_max_price(prices):
    return min(prices), max(prices)


lowest, highest = min_max_price([25, 75, 999])

print(lowest)
print(highest)
```

## Scope

Variables created inside a function are local to that function.

```python
def calculate_tax(price):
    tax_rate = 0.08
    return price * tax_rate


print(calculate_tax(1000))
# print(tax_rate)  # NameError
```

## Pure Functions

A pure function returns a result based only on input and does not modify outside state.

```python
def discounted_price(price, discount_percent):
    return price - (price * discount_percent / 100)
```

Pure functions are easier to test and explain in interviews.

## Side Effects

A side effect changes something outside the function, such as a list, dictionary, file, database, or printed output.

```python
def add_to_cart(cart, item):
    cart.append(item)


cart = []
add_to_cart(cart, "laptop")
print(cart)
```

Side effects are not always bad, but mention them clearly in interviews.

## Type Hints

Type hints improve readability.

```python
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity
```

Type hints do not enforce types at runtime by default.

## Docstrings

A docstring explains what a function does.

```python
def calculate_total(price, quantity):
    """Return total price for a product quantity."""
    return price * quantity
```

## Common Interview Points

### What is the difference between parameter and argument?

A **parameter** is the variable in the function definition. An **argument** is the value passed during the function call.

```python
def show_product(name):  # name is parameter
    print(name)


show_product("laptop")  # "laptop" is argument
```

### What does a function return by default?

If there is no `return`, the function returns `None`.

### Why are functions useful?

Functions reduce duplication, improve readability, and make code easier to test.

## Practice Problems

1. Write a function to calculate cart total.
2. Write a function to apply discount.
3. Write a function to check whether a product is in stock.
4. Write a function that returns minimum and maximum price.
5. Write a function to count products by category.
6. Write a pure function and a function with side effects.
7. Add type hints to a cart-total function.

## See also

- [Python function parameters](parameters-and-arguments.md)
- [Python function interview problems](interview-problems.md)
- [Python function FAQ](frequently-asked-questions.md)
- [Python dictionaries: core concepts](../dict/core-concepts.md)
