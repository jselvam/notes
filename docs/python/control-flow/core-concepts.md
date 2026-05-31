# Python Control Flow: Conditions, Loops, and `match`

Python **control flow** decides which code runs and how many times it runs. It includes conditional statements, loops, and pattern matching.

This section covers:

- `if`, `elif`, `else`
- `for` loops
- `while` loops
- `break`, `continue`, `pass`
- loop `else`
- `match` / `case`

Examples use an online computer shopping system: carts, stock, coupons, orders, product categories, and checkout validation.

## `if`, `elif`, `else`

Use conditions to choose between paths.

```python
stock_count = 5

if stock_count > 10:
    print("High stock")
elif stock_count > 0:
    print("In stock")
else:
    print("Out of stock")
```

## `for` Loop

Use `for` to iterate over a sequence or iterable.

```python
cart_items = ["laptop", "mouse", "keyboard"]

for item in cart_items:
    print(item)
```

Use `enumerate()` when you need index and value.

```python
for index, item in enumerate(cart_items):
    print(index, item)
```

## `range()`

Use `range()` when looping a fixed number of times.

```python
for order_number in range(1, 4):
    print(f"Processing order {order_number}")
```

## `while` Loop

Use `while` when the number of iterations depends on a condition.

```python
stock = 3

while stock > 0:
    print("Selling one item")
    stock -= 1
```

### Interview Point

Always make sure a `while` loop condition eventually becomes false.

## `break`

`break` exits the loop early.

```python
products = ["mouse", "keyboard", "laptop", "monitor"]

for product in products:
    if product == "laptop":
        print("Found laptop")
        break
```

## `continue`

`continue` skips to the next iteration.

```python
products = ["laptop", "out-of-stock", "mouse"]

for product in products:
    if product == "out-of-stock":
        continue
    print(product)
```

## `pass`

`pass` is a placeholder that does nothing.

```python
if True:
    pass
```

Use it when syntax requires a block but you are not ready to implement it.

## Loop `else`

A loop `else` runs if the loop finishes without `break`.

```python
products = ["mouse", "keyboard"]

for product in products:
    if product == "laptop":
        print("Found laptop")
        break
else:
    print("Laptop not found")
```

### Interview Point

Loop `else` is often misunderstood. It means “no break happened,” not “if loop condition was false.”

## `match` / `case`

`match` is Python's structural pattern matching. It is useful when choosing behavior based on shape or value.

```python
order_status = "paid"

match order_status:
    case "pending":
        print("Waiting for payment")
    case "paid":
        print("Prepare shipment")
    case "shipped":
        print("Track shipment")
    case _:
        print("Unknown status")
```

## Matching Dictionaries

```python
event = {"type": "order_paid", "order_id": 101}

match event:
    case {"type": "order_paid", "order_id": order_id}:
        print(f"Order paid: {order_id}")
    case {"type": "refund", "order_id": order_id}:
        print(f"Refund order: {order_id}")
    case _:
        print("Unknown event")
```

## Common Interview Points

### When should you use `for` vs `while`?

Use `for` when iterating over known items. Use `while` when repeating until a condition changes.

### What is the difference between `break` and `continue`?

`break` exits the loop. `continue` skips the current iteration.

### Is `match` a loop?

No. `match` is conditional pattern matching, not a loop.

## Practice Problems

1. Print every product in a cart using `for`.
2. Count down stock using `while`.
3. Find the first product above a target price using `break`.
4. Skip out-of-stock products using `continue`.
5. Use loop `else` to print “not found”.
6. Use `if` / `elif` / `else` to classify product price.
7. Use `match` to handle order status.
8. Use `match` to route event dictionaries.

## See also

- [Python control-flow reference](control-flow-reference.md)
- [Python control-flow interview problems](interview-problems.md)
- [Python control-flow FAQ](frequently-asked-questions.md)
- [Python boolean operations](../bool/operations-and-truthiness.md)
