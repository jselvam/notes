# Python Function Parameters & Arguments: Interview Notes

Function parameter questions are common in interviews because they reveal whether you understand how values are passed, defaults work, and flexible signatures like `*args` and `**kwargs`.

## Quick Table

| Topic | Meaning | Interview use case |
|-------|---------|--------------------|
| Positional arguments | Matched by position | Simple function calls |
| Keyword arguments | Matched by name | Readable calls |
| Default parameters | Fallback values | Optional discount/tax |
| `*args` | Extra positional args | Variable number of prices |
| `**kwargs` | Extra keyword args | Flexible product filters |
| Keyword-only args | Must be passed by name | Avoid unclear calls |
| Positional-only args | Must be passed by position | Built-in style APIs |

## Positional Arguments

Arguments are matched by order.

```python
def calculate_total(price, quantity):
    return price * quantity


print(calculate_total(999, 2))
```

## Keyword Arguments

Arguments are matched by name.

```python
def calculate_total(price, quantity):
    return price * quantity


print(calculate_total(quantity=2, price=999))
```

### Interview Point

Keyword arguments improve readability when many values are passed.

## Default Arguments

Default values are used when arguments are not provided.

```python
def apply_discount(price, discount_percent=10):
    return price - (price * discount_percent / 100)


print(apply_discount(1000))
print(apply_discount(1000, 20))
```

## Mutable Default Argument Pitfall

Do not use mutable defaults like `[]` or `{}` unless you really want shared state.

```python
def add_item_bad(item, cart=[]):
    cart.append(item)
    return cart


print(add_item_bad("laptop"))
print(add_item_bad("mouse"))
# Same list is reused
```

Use `None` instead.

```python
def add_item(item, cart=None):
    if cart is None:
        cart = []

    cart.append(item)
    return cart
```

## `*args`

`*args` collects extra positional arguments into a tuple.

```python
def total_prices(*prices):
    return sum(prices)


print(total_prices(999, 25, 75))
```

### Interview Point

Use `*args` when the number of inputs can vary.

## `**kwargs`

`**kwargs` collects extra keyword arguments into a dictionary.

```python
def filter_products(**filters):
    return filters


print(filter_products(category="hardware", in_stock=True, max_price=1000))
```

### Interview Point

Use `**kwargs` for flexible named options, but avoid hiding required data.

## Combining Parameters

Common order:

```python
def create_order(customer_id, *items, discount=0, **metadata):
    return {
        "customer_id": customer_id,
        "items": items,
        "discount": discount,
        "metadata": metadata,
    }


order = create_order(
    501,
    "laptop",
    "mouse",
    discount=10,
    source="web",
)
```

Order:

1. positional / normal parameters
2. `*args`
3. keyword-only parameters
4. `**kwargs`

## Keyword-Only Arguments

Arguments after `*` must be passed by name.

```python
def checkout_total(price, quantity, *, tax_percent=0, discount_percent=0):
    subtotal = price * quantity
    subtotal -= subtotal * discount_percent / 100
    subtotal += subtotal * tax_percent / 100
    return subtotal


print(checkout_total(1000, 2, tax_percent=8, discount_percent=10))
```

### Interview Point

Keyword-only arguments prevent unclear calls like `checkout_total(1000, 2, 8, 10)`.

## Positional-Only Arguments

Arguments before `/` must be passed by position.

```python
def apply_tax(price, /, tax_percent):
    return price + (price * tax_percent / 100)


print(apply_tax(1000, tax_percent=8))
```

This is more common in built-in functions than everyday code.

## Argument Unpacking

Use `*` to unpack a list or tuple into positional arguments.

```python
values = [999, 2]

def calculate_total(price, quantity):
    return price * quantity


print(calculate_total(*values))
```

Use `**` to unpack a dictionary into keyword arguments.

```python
data = {"price": 999, "quantity": 2}

print(calculate_total(**data))
```

## Common Interview Questions

### What is the difference between `*args` and `**kwargs`?

`*args` collects positional arguments into a tuple. `**kwargs` collects keyword arguments into a dictionary.

### Why is mutable default argument dangerous?

Default values are created once when the function is defined, not every time the function is called.

### What is the difference between positional and keyword arguments?

Positional arguments are matched by order. Keyword arguments are matched by name.

### Why use keyword-only arguments?

They make function calls clearer and reduce mistakes when many optional values exist.

## Practice Problems

1. Write a function with default discount.
2. Write a function that accepts any number of product prices using `*args`.
3. Write a function that accepts product filters using `**kwargs`.
4. Fix a mutable default argument bug.
5. Use `*` unpacking to call a function from a list.
6. Use `**` unpacking to call a function from a dictionary.

## See also

- [Python functions: core concepts](core-concepts.md)
- [Python function interview problems](interview-problems.md)
- [Python function FAQ](frequently-asked-questions.md)
