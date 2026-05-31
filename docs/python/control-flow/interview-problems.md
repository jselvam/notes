# Python Control Flow Interview Problems

Control-flow problems test whether you can use conditions, loops, `break`, `continue`, loop `else`, and `match` clearly.

## 1. Classify Product Price

### Problem

Classify product price as `budget`, `standard`, or `premium`.

### Python Solution

```python
def classify_price(price):
    if price >= 1000:
        return "premium"
    elif price >= 100:
        return "standard"
    else:
        return "budget"


print(classify_price(999))
```

### Complexity

- Time: **O(1)**
- Space: **O(1)**

## 2. Print Cart Items

### Problem

Print every item in a cart.

### Python Solution

```python
def print_cart(cart_items):
    for item in cart_items:
        print(item)


print_cart(["laptop", "mouse"])
```

### Complexity

- Time: **O(n)**
- Space: **O(1)**

## 3. Find First Expensive Product

### Problem

Return the first product whose price is at least target price.

### Python Solution

```python
def first_expensive_product(products, target_price):
    for product in products:
        if product["price"] >= target_price:
            return product

    return None


products = [
    {"name": "mouse", "price": 25},
    {"name": "laptop", "price": 999},
]

print(first_expensive_product(products, 500))
```

### Complexity

- Time: **O(n)**
- Space: **O(1)**

## 4. Skip Out-of-Stock Products

### Problem

Return only products with stock greater than zero.

### Python Solution

```python
def available_products(products):
    result = []

    for product in products:
        if product["stock"] == 0:
            continue
        result.append(product)

    return result
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

## 5. Search With Loop `else`

### Problem

Search for a product and return a message when not found.

### Python Solution

```python
def find_product(products, target):
    for product in products:
        if product == target:
            result = "found"
            break
    else:
        result = "not found"

    return result


print(find_product(["mouse", "keyboard"], "laptop"))
```

### Interview Point

The `else` block runs only when no `break` happens. In real interview code, an early `return` is often simpler:

```python
def find_product_simple(products, target):
    for product in products:
        if product == target:
            return "found"
    return "not found"
```

## 6. Count Down Stock With `while`

### Problem

Sell products until stock reaches zero.

### Python Solution

```python
def sell_until_empty(stock):
    sold = 0

    while stock > 0:
        sold += 1
        stock -= 1

    return sold


print(sell_until_empty(3))
```

### Complexity

- Time: **O(n)** where `n` is initial stock
- Space: **O(1)**

## 7. Retry Payment With `while`

### Problem

Retry payment up to max attempts.

### Python Solution

```python
def retry_payment(results, max_attempts):
    attempts = 0

    while attempts < max_attempts:
        if results[attempts]:
            return "paid"
        attempts += 1

    return "failed"


print(retry_payment([False, False, True], 3))
```

### Interview Point

Guard against indexes going out of range in real code if input length can be shorter than max attempts.

## 8. Handle Order Status With `match`

### Problem

Return action based on order status.

### Python Solution

```python
def order_action(status):
    match status:
        case "pending":
            return "wait for payment"
        case "paid":
            return "prepare shipment"
        case "shipped":
            return "track shipment"
        case "cancelled":
            return "stop processing"
        case _:
            return "manual review"


print(order_action("paid"))
```

### Complexity

- Time: **O(1)** for this small fixed set
- Space: **O(1)**

## 9. Match Event Dictionary

### Problem

Route event dictionaries based on type.

### Python Solution

```python
def handle_event(event):
    match event:
        case {"type": "order_paid", "order_id": order_id}:
            return f"ship order {order_id}"
        case {"type": "refund", "order_id": order_id}:
            return f"refund order {order_id}"
        case {"type": "inventory_low", "product_id": product_id}:
            return f"restock product {product_id}"
        case _:
            return "unknown event"


print(handle_event({"type": "order_paid", "order_id": 101}))
```

## 10. Nested Loop: Find Pair With Target

### Problem

Find whether two prices add to target using nested loops.

### Python Solution

```python
def has_pair_brute_force(prices, target):
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] + prices[j] == target:
                return True

    return False


print(has_pair_brute_force([499, 129, 99], 628))
```

### Complexity

- Time: **O(n^2)**
- Space: **O(1)**

### Follow-up

Use a set or dictionary to optimize to **O(n)**.

## Summary: Control-Flow Patterns to Remember

| Pattern | Construct | Example |
|---------|-----------|---------|
| Branching | `if` / `elif` / `else` | price category |
| Iterate known items | `for` | cart items |
| Repeat until condition | `while` | retry payment |
| Stop early | `break` / `return` | first match |
| Skip item | `continue` | out-of-stock |
| Not found | loop `else` | search result |
| Route by shape/value | `match` | event handling |

## See also

- [Python control-flow core concepts](core-concepts.md)
- [Python control-flow reference](control-flow-reference.md)
- [Python control-flow FAQ](frequently-asked-questions.md)
- [Python set interview problems](../set/interview-problems.md)
