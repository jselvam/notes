# Python NoneType Interview Problems

NoneType interview problems usually test whether you can distinguish missing values from falsey values, write safe defaults, and handle optional returns correctly.

## 1. Find Product or Return `None`

### Problem

Return a product dictionary if found; otherwise return `None`.

### Python Solution

```python
def find_product(products, product_id):
    for product in products:
        if product["id"] == product_id:
            return product

    return None


products = [{"id": 101, "name": "laptop"}]
result = find_product(products, 999)

if result is None:
    print("Product not found")
```

### Complexity

- Time: **O(n)**
- Space: **O(1)**

## 2. Apply Default Discount Correctly

### Problem

Use default discount only when discount is `None`. A discount of `0` is valid.

### Python Solution

```python
def resolve_discount(discount, default_discount=10):
    if discount is None:
        return default_discount
    return discount


print(resolve_discount(0))     # 0
print(resolve_discount(None))  # 10
```

### Interview Point

Avoid `discount or default_discount` because `0` is falsey.

## 3. Fix Mutable Default Cart

### Problem

Fix a function that shares the same default cart list across calls.

### Bad Code

```python
def add_to_cart_bad(item, cart=[]):
    cart.append(item)
    return cart
```

### Python Solution

```python
def add_to_cart(item, cart=None):
    if cart is None:
        cart = []

    cart.append(item)
    return cart


print(add_to_cart("laptop"))
print(add_to_cart("mouse"))
```

## 4. Validate Optional Payment Method

### Problem

Checkout is allowed only when payment method is selected.

### Python Solution

```python
def has_payment_method(payment_method):
    return payment_method is not None


print(has_payment_method("card"))  # True
print(has_payment_method(None))    # False
```

## 5. Distinguish Missing Price From Free Product

### Problem

`None` means price is missing. `0` means free product.

### Python Solution

```python
def price_label(price):
    if price is None:
        return "price missing"
    if price == 0:
        return "free"
    return f"${price}"


print(price_label(None))
print(price_label(0))
print(price_label(25))
```

## 6. Safe Dictionary Lookup With Sentinel

### Problem

Dictionary values may be `None`, so `.get()` default `None` is ambiguous.

### Python Solution

```python
MISSING = object()


def get_config_value(config, key):
    value = config.get(key, MISSING)

    if value is MISSING:
        return "missing key"
    if value is None:
        return "configured as None"
    return value


config = {"discount": None}
print(get_config_value(config, "discount"))
print(get_config_value(config, "tax"))
```

## 7. Optional Return Type Hint

### Problem

Add a type hint for a function that may return a product ID or `None`.

### Python Solution

```python
def find_product_id(name: str) -> int | None:
    products = {"laptop": 101}
    return products.get(name)


print(find_product_id("mouse"))
```

## 8. Function Without Return Bug

### Problem

Find why a function prints a value but the caller receives `None`.

### Example

```python
def calculate_total(price, quantity):
    print(price * quantity)


result = calculate_total(100, 2)
print(result)  # None
```

### Fix

```python
def calculate_total(price, quantity):
    return price * quantity
```

## 9. Filter Products With Optional Category

### Problem

If category is `None`, return all products. Otherwise filter by category.

### Python Solution

```python
def filter_by_category(products, category=None):
    if category is None:
        return products

    return [product for product in products if product["category"] == category]
```

## 10. Use `None` as Linked List End

### Problem

In many data-structure questions, `None` marks the end of a linked list.

### Python Solution

```python
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


head = Node("laptop", Node("mouse"))

current = head
while current is not None:
    print(current.value)
    current = current.next
```

## Summary: NoneType Patterns to Remember

| Pattern | None idea | Example |
|---------|-----------|---------|
| Not found | return `None` | product search |
| Optional value | `is None` | discount missing |
| Safe default | `param=None` | cart list |
| Ambiguous `.get()` | sentinel | key exists with `None` |
| Optional typing | `T | None` | product ID lookup |
| End marker | `next is None` | linked list |

## See also

- [Python NoneType core concepts](core-concepts.md)
- [Python NoneType operations](operations-and-patterns.md)
- [Python NoneType FAQ](frequently-asked-questions.md)
- [Python function interview problems](../functions/interview-problems.md)
