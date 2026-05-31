# Python String Formatting Interview Problems

## 1. Format Product Price

### Problem

Return a product label with price shown using two decimal places.

```python
def product_label(name, price):
    return f"{name}: ${price:.2f}"


print(product_label("Laptop", 999.9))
```

**Complexity:** `O(n)` time for output string length, `O(n)` space.

## 2. Format Cart Total

```python
def cart_summary(item_count, total):
    return f"Cart has {item_count} items. Total: ${total:.2f}"


print(cart_summary(3, 1024.987))
```

## 3. Add Leading Zeros to Order Number

```python
def format_order_number(number):
    return f"ORD-{number:0>6}"


print(format_order_number(501))
```

Output:

```text
ORD-000501
```

## 4. Align Product Report Columns

```python
def product_row(name, price, stock):
    return f"{name:<15} ${price:>8.2f} {stock:>5}"


print(product_row("Mouse", 25, 120))
print(product_row("Laptop", 999.99, 5))
```

## 5. Format Discount Percent

```python
def discount_message(rate):
    return f"Discount: {rate:.0%}"


print(discount_message(0.15))
```

## 6. Format Date in an Order Message

```python
from datetime import date


def order_date_message(order_id, ordered_on):
    return f"Order {order_id} placed on {ordered_on:%Y-%m-%d}"


print(order_date_message("ORD-501", date(2026, 5, 31)))
```

## 7. Use `str.format()` for a Reusable Template

```python
def render_template(template, product):
    return template.format(**product)


template = "{name} is available for ${price:.2f}"
product = {"name": "Keyboard", "price": 75}

print(render_template(template, product))
```

## 8. Convert `%` Formatting to f-String

Old:

```python
product = "Monitor"
price = 199.99

message = "Product: %s, Price: $%.2f" % (product, price)
```

Modern:

```python
product = "Monitor"
price = 199.99

message = f"Product: {product}, Price: ${price:.2f}"
print(message)
```

## 9. Debug Variable Values With f-String

```python
def debug_cart(quantity, price):
    return f"{quantity=}, {price=}, total={quantity * price:.2f}"


print(debug_cart(2, 25))
```

## 10. Format Large Revenue Number

```python
def revenue_message(revenue):
    return f"Monthly revenue: ${revenue:,.2f}"


print(revenue_message(1250000.5))
```

## Summary

| Problem pattern | Formatting idea |
|-----------------|-----------------|
| prices | `:.2f` |
| order numbers | `0>6` |
| columns | `<`, `>`, width |
| discounts | `:.0%` |
| dates | `%Y-%m-%d` inside f-string |
| large numbers | `:,` |
| legacy conversion | `%` to f-string |

## See also

- [Python string formatting: core concepts](core-concepts.md)
- [Python string formatting reference](string-formatting-reference.md)
- [Python string formatting FAQ](frequently-asked-questions.md)
