# Python Boolean Interview Problems

Boolean problems test whether you can express conditions clearly, handle truthy/falsey values, and avoid common mistakes with `and`, `or`, `not`, `any()`, and `all()`.

## Interview Pattern: When to Think About Booleans

Use boolean logic when the problem needs:

- validation
- filtering
- feature flags
- access control
- eligibility checks
- empty input checks
- all/any condition checks
- safe short-circuit access

## 1. Can Add Product to Cart

### Problem

A product can be added when requested quantity is positive and stock is enough.

### Python Solution

```python
def can_add_to_cart(requested_quantity, stock_count):
    return requested_quantity > 0 and requested_quantity <= stock_count


print(can_add_to_cart(2, 5))  # True
print(can_add_to_cart(6, 5))  # False
```

### Complexity

- Time: **O(1)**
- Space: **O(1)**

## 2. Is Checkout Allowed

### Problem

Checkout is allowed only if user is logged in, cart has items, and payment method exists.

### Python Solution

```python
def can_checkout(is_logged_in, cart_items, payment_method):
    return is_logged_in and bool(cart_items) and payment_method is not None


print(can_checkout(True, ["laptop"], "card"))  # True
print(can_checkout(True, [], "card"))          # False
```

### Interview Point

Use `bool(cart_items)` or simply `if cart_items` for non-empty checks.

## 3. Validate Coupon

### Problem

A coupon is valid if it is active, not expired, and order total reaches minimum amount.

### Python Solution

```python
def is_coupon_valid(is_active, is_expired, order_total, minimum_total):
    return is_active and not is_expired and order_total >= minimum_total


print(is_coupon_valid(True, False, 1200, 1000))
```

### Complexity

- Time: **O(1)**
- Space: **O(1)**

## 4. Any Warehouse Has Stock

### Problem

Return `True` if any warehouse has stock.

### Python Solution

```python
def any_warehouse_has_stock(stock_counts):
    return any(count > 0 for count in stock_counts)


print(any_warehouse_has_stock([0, 0, 5]))  # True
```

### Complexity

- Time: **O(n)**
- Space: **O(1)**

### Interview Point

`any()` short-circuits after the first true value.

## 5. All Checkout Rules Pass

### Problem

Return `True` if all validation checks pass.

### Python Solution

```python
def all_rules_pass(checks):
    return all(checks)


checks = [True, True, False]
print(all_rules_pass(checks))  # False
```

### Interview Point

`all()` short-circuits after the first false value.

## 6. Safe First Item Check

### Problem

Check if the first cart item is `"laptop"` without failing on an empty cart.

### Python Solution

```python
def starts_with_laptop(cart_items):
    return bool(cart_items) and cart_items[0] == "laptop"


print(starts_with_laptop(["laptop", "mouse"]))  # True
print(starts_with_laptop([]))                   # False
```

### Interview Point

Short-circuiting prevents `IndexError`.

## 7. Price Range Check

### Problem

Check whether price is between minimum and maximum.

### Python Solution

```python
def is_price_in_range(price, minimum, maximum):
    return minimum <= price <= maximum


print(is_price_in_range(500, 100, 1000))  # True
```

### Interview Point

Python supports chained comparisons.

## 8. Filter Active Products

### Problem

Return only active products.

### Python Solution

```python
def active_products(products):
    return [product for product in products if product.get("is_active")]


products = [
    {"name": "laptop", "is_active": True},
    {"name": "old-monitor", "is_active": False},
]

print(active_products(products))
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

## 9. Avoid Bad Default With `or`

### Problem

Use default discount only when discount is `None`, not when discount is `0`.

### Python Solution

```python
def final_discount(discount, default_discount=10):
    if discount is None:
        return default_discount
    return discount


print(final_discount(0))     # 0
print(final_discount(None))  # 10
```

### Interview Point

`discount or default_discount` would incorrectly replace `0`.

## 10. Count True Values

### Problem

Count how many product flags are true.

### Python Solution

```python
def count_true_flags(flags):
    return sum(flags)


print(count_true_flags([True, False, True, True]))
# 3
```

### Interview Point

Booleans behave like integers: `True == 1`, `False == 0`.

## Summary: Boolean Patterns to Remember

| Pattern | Boolean idea | Example |
|---------|--------------|---------|
| Validation | `and`, `not` | coupon rules |
| Alternative | `or` | default value |
| Empty check | truthiness | empty cart |
| Safe access | short-circuit | `cart and cart[0]` |
| At least one | `any()` | warehouse stock |
| All required | `all()` | checkout checks |
| Range | chained comparison | price range |
| Count flags | `sum(bool_list)` | true flags |

## See also

- [Python boolean core concepts](core-concepts.md)
- [Python boolean operations](operations-and-truthiness.md)
- [Python boolean FAQ](frequently-asked-questions.md)
- [Python numeric interview problems](../numbers/interview-problems.md)
