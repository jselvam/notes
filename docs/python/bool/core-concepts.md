# Python Boolean: Core Concepts & Shopping Examples

Python **boolean** values represent truth: `True` or `False`. Booleans are used in conditions, validations, filters, loops, and interview problems.

In an online computer shopping management system, booleans can represent:

- product is in stock
- coupon is valid
- user is logged in
- subscription is active
- order is paid
- cart is empty
- product is eligible for discount

## Boolean Values

Python has two boolean constants:

```python
is_in_stock = True
is_discontinued = False

print(type(is_in_stock))
# <class 'bool'>
```

Use capital `True` and `False`. Lowercase `true` and `false` are not Python booleans.

## Boolean From Comparisons

Comparisons return booleans.

```python
stock_count = 5
requested_quantity = 2

can_add_to_cart = requested_quantity <= stock_count

print(can_add_to_cart)
# True
```

## Boolean in `if` Statements

```python
is_logged_in = True

if is_logged_in:
    print("Show checkout button")
else:
    print("Ask user to sign in")
```

## Truthy and Falsey Values

Python does not require an expression to be exactly `True` or `False`. Many values have truthiness.

Falsey values include:

- `False`
- `None`
- `0`, `0.0`, `0j`
- `""`
- `[]`, `{}`, `set()`, `()`

```python
cart_items = []

if not cart_items:
    print("Cart is empty")
```

Truthy values include most non-empty or non-zero values.

```python
cart_items = ["laptop"]

if cart_items:
    print("Cart has items")
```

## `bool()` Conversion

Use `bool()` to check truthiness.

```python
print(bool(""))          # False
print(bool("laptop"))    # True
print(bool([]))          # False
print(bool([101]))       # True
print(bool(0))           # False
print(bool(1))           # True
```

## Boolean Operators

### `and`

Returns true only when both conditions are true.

```python
is_logged_in = True
cart_has_items = True

if is_logged_in and cart_has_items:
    print("Allow checkout")
```

### `or`

Returns true if at least one condition is true.

```python
has_coupon = False
has_member_discount = True

if has_coupon or has_member_discount:
    print("Apply discount logic")
```

### `not`

Negates truthiness.

```python
is_out_of_stock = False

if not is_out_of_stock:
    print("Product can be purchased")
```

## Booleans Are Integers

In Python, `bool` is a subclass of `int`.

```python
print(True == 1)   # True
print(False == 0)  # True
print(True + True) # 2
```

This is sometimes asked in interviews, but avoid relying on it in business logic unless it improves clarity.

## Common Interview Points

### What is the difference between `==` and `is` for booleans?

Use `is` only for singleton checks like `x is None`. For boolean expressions, prefer direct truth checks.

```python
is_active = True

if is_active:
    print("Active")
```

Avoid unnecessary comparisons:

```python
# Less Pythonic
if is_active == True:
    print("Active")
```

### What is short-circuit evaluation?

Python stops evaluating as soon as the result is known.

```python
cart = []

if cart and cart[0] == "laptop":
    print("First item is laptop")
```

Here `cart[0]` is not evaluated when `cart` is empty.

## Practice Problems

1. Check whether a product can be added to cart.
2. Check whether checkout is allowed.
3. Validate whether a coupon can be applied.
4. Filter products that are in stock.
5. Count how many products are active using booleans.
6. Explain why `bool([])` is `False`.
7. Explain why `True + True == 2`.

## See also

- [Python boolean operations](operations-and-truthiness.md)
- [Python boolean interview problems](interview-problems.md)
- [Python boolean FAQ](frequently-asked-questions.md)
- [Python numeric types](../numbers/core-concepts.md)
