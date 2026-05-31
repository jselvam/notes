# Python Operator Interview Problems

Operator interview problems test arithmetic, comparisons, boolean logic, membership, identity, and bit manipulation.

## 1. Calculate Final Cart Total

### Problem

Use arithmetic operators to calculate total after discount and tax.

### Python Solution

```python
def final_total(price, quantity, discount_percent, tax_percent):
    subtotal = price * quantity
    discounted = subtotal - (subtotal * discount_percent / 100)
    taxed = discounted + (discounted * tax_percent / 100)
    return round(taxed, 2)


print(final_total(1000, 2, 10, 8))
```

### Complexity

- Time: **O(1)**
- Space: **O(1)**

## 2. Split Orders Into Full Batches

### Problem

Use `//` and `%` to find full batches and remaining orders.

### Python Solution

```python
def batch_summary(order_count, batch_size):
    full_batches = order_count // batch_size
    remaining = order_count % batch_size
    return full_batches, remaining


print(batch_summary(25, 10))
```

## 3. Check Price Range

### Problem

Check whether a price is within allowed range.

### Python Solution

```python
def is_valid_price(price):
    return 100 <= price <= 1000


print(is_valid_price(500))
```

### Interview Point

Python chained comparisons are readable and common.

## 4. Checkout Eligibility

### Problem

Checkout is allowed only when user is logged in, cart has items, and payment method exists.

### Python Solution

```python
def can_checkout(is_logged_in, cart_items, payment_method):
    return is_logged_in and bool(cart_items) and payment_method is not None


print(can_checkout(True, ["laptop"], "card"))
```

## 5. Safe First Cart Item Check

### Problem

Check if first cart item is `"laptop"` without failing on empty cart.

### Python Solution

```python
def starts_with_laptop(cart_items):
    return bool(cart_items) and cart_items[0] == "laptop"


print(starts_with_laptop([]))
print(starts_with_laptop(["laptop", "mouse"]))
```

### Interview Point

This uses logical short-circuiting.

## 6. Product Membership Check

### Problem

Check whether a product is in a cart.

### Python Solution

```python
def has_product(cart_items, product):
    return product in cart_items


print(has_product(["laptop", "mouse"], "mouse"))
```

### Follow-up

For many lookups, convert the cart to a set.

```python
cart_lookup = set(["laptop", "mouse"])
print("mouse" in cart_lookup)
```

## 7. Optional Discount Check

### Problem

Only apply default discount when discount is `None`, not when it is `0`.

### Python Solution

```python
def resolve_discount(discount, default_discount=10):
    if discount is None:
        return default_discount
    return discount


print(resolve_discount(0))
print(resolve_discount(None))
```

### Interview Point

Do not use `discount or default_discount` when `0` is valid.

## 8. Permission Flags With Bitwise Operators

### Problem

Use bitwise operators to store and check permissions.

### Python Solution

```python
VIEW = 1       # 001
BUY = 2        # 010
REFUND = 4     # 100

permission = VIEW | BUY

can_view = permission & VIEW != 0
can_refund = permission & REFUND != 0

print(can_view)
print(can_refund)
```

## 9. Toggle Feature Flag

### Problem

Use XOR to toggle a flag.

### Python Solution

```python
NEW_CHECKOUT = 1

flags = 0
flags ^= NEW_CHECKOUT
print(flags & NEW_CHECKOUT != 0)

flags ^= NEW_CHECKOUT
print(flags & NEW_CHECKOUT != 0)
```

## 10. Check Odd or Even

### Problem

Check whether a number is odd or even.

### Python Solution

```python
def is_even(num):
    return num % 2 == 0


print(is_even(104))
print(is_even(105))
```

### Bitwise Alternative

```python
def is_even_bitwise(num):
    return num & 1 == 0
```

## Summary: Operator Patterns to Remember

| Pattern | Operator idea | Example |
|---------|---------------|---------|
| Total calculation | `+`, `-`, `*`, `/` | cart total |
| Batching | `//`, `%` | order batches |
| Range check | chained comparison | `100 <= price <= 1000` |
| Validation | `and`, `or`, `not` | checkout |
| Safe access | short-circuit | `cart and cart[0]` |
| Optional value | `is None` | default discount |
| Lookup | `in` | product in cart |
| Flags | `&`, `|`, `^` | permissions |

## See also

- [Python operators: core concepts](core-concepts.md)
- [Python operator reference](operator-reference.md)
- [Python operator FAQ](frequently-asked-questions.md)
- [Python boolean interview problems](../bool/interview-problems.md)
