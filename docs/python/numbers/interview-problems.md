# Python Numeric Interview Problems

Numeric interview problems often test arithmetic, modulo, rounding, conversion, integer logic, and floating-point precision.

## Interview Pattern: When to Think About Numbers

Use numeric techniques when the problem needs:

- totals, tax, discount, averages
- even/odd checks
- modulo cycles
- digit extraction
- integer division
- rounding
- precision handling
- binary/bit concepts

## 1. Calculate Cart Total

### Problem

Given a price and quantity, calculate the total.

### Python Solution

```python
def cart_total(price, quantity):
    return price * quantity


print(cart_total(999, 2))
```

### Complexity

- Time: **O(1)**
- Space: **O(1)**

## 2. Apply Tax and Discount

### Problem

Apply discount first, then tax.

### Python Solution

```python
def final_price(price, discount_percent, tax_percent):
    discounted = price - (price * discount_percent / 100)
    taxed = discounted + (discounted * tax_percent / 100)
    return round(taxed, 2)


print(final_price(1000, 10, 8))
```

### Complexity

- Time: **O(1)**
- Space: **O(1)**

## 3. Check Even or Odd Order ID

### Problem

Check whether an order ID is even or odd.

### Python Solution

```python
def is_even(order_id):
    return order_id % 2 == 0


print(is_even(104))
print(is_even(105))
```

### Interview Point

Modulo `%` is the standard even/odd pattern.

## 4. Split Orders Into Batches

### Problem

Given number of orders and batch size, return full batches and remaining orders.

### Python Solution

```python
def batch_orders(order_count, batch_size):
    return divmod(order_count, batch_size)


full_batches, remaining = batch_orders(25, 10)
print(full_batches, remaining)
```

### Complexity

- Time: **O(1)**
- Space: **O(1)**

## 5. Sum Digits of Product ID

### Problem

Sum all digits in a product ID.

### Python Solution

```python
def sum_digits(product_id):
    product_id = abs(product_id)
    total = 0

    while product_id > 0:
        total += product_id % 10
        product_id //= 10

    return total


print(sum_digits(12345))
```

### Complexity

- Time: **O(d)** digits
- Space: **O(1)**

## 6. Reverse Integer Product Code

### Problem

Reverse the digits of an integer.

### Python Solution

```python
def reverse_integer(num):
    sign = -1 if num < 0 else 1
    num = abs(num)
    result = 0

    while num > 0:
        result = result * 10 + (num % 10)
        num //= 10

    return sign * result


print(reverse_integer(1234))
```

### Complexity

- Time: **O(d)**
- Space: **O(1)**

## 7. Check Numeric Palindrome

### Problem

Check whether an integer reads the same forward and backward.

### Python Solution

```python
def is_number_palindrome(num):
    if num < 0:
        return False

    original = num
    reversed_num = 0

    while num > 0:
        reversed_num = reversed_num * 10 + (num % 10)
        num //= 10

    return original == reversed_num


print(is_number_palindrome(1221))
```

### Complexity

- Time: **O(d)**
- Space: **O(1)**

## 8. Find Average Price

### Problem

Find average price from a list.

### Python Solution

```python
def average_price(prices):
    if not prices:
        return 0

    return sum(prices) / len(prices)


print(average_price([999, 25, 75]))
```

### Complexity

- Time: **O(n)**
- Space: **O(1)**

## 9. Avoid Float Precision for Money

### Problem

Calculate exact decimal tax for money values.

### Python Solution

```python
from decimal import Decimal


def exact_total(price, tax_rate):
    price = Decimal(price)
    tax_rate = Decimal(tax_rate)
    return price + (price * tax_rate)


print(exact_total("999.99", "0.08"))
```

### Interview Point

Pass strings to `Decimal` to avoid importing float imprecision.

## 10. Rotate Warehouse Index With Modulo

### Problem

Assign orders to warehouses in a repeating cycle.

### Python Solution

```python
def warehouse_for_order(order_index, warehouses):
    return warehouses[order_index % len(warehouses)]


warehouses = ["A", "B", "C"]

print(warehouse_for_order(0, warehouses))
print(warehouse_for_order(3, warehouses))
print(warehouse_for_order(4, warehouses))
```

### Complexity

- Time: **O(1)**
- Space: **O(1)**

## Summary: Numeric Patterns to Remember

| Pattern | Numeric idea | Example |
|---------|--------------|---------|
| Arithmetic | `+`, `-`, `*`, `/` | total price |
| Modulo | `%` | even/odd, cycles |
| Floor division | `//` | batches/pages |
| `divmod()` | quotient + remainder | batches + leftovers |
| Digit extraction | `% 10`, `// 10` | reverse integer |
| Rounding | `round()` | display price |
| Precision | `Decimal` | money |
| Complex parts | `.real`, `.imag` | math/signal |

## See also

- [Python numeric core concepts](core-concepts.md)
- [Python numeric operations](operations-and-methods.md)
- [Python numeric FAQ](frequently-asked-questions.md)
