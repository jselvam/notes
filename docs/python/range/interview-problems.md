# Python `range` Interview Problems

## 1. Print Page Numbers

### Problem

Print product page numbers from 1 to `n`.

```python
def print_pages(n):
    for page in range(1, n + 1):
        print(page)


print_pages(5)
```

### Complexity

- Time: **O(n)**
- Space: **O(1)**

## 2. Generate Even Product IDs

```python
def even_product_ids(start, stop):
    return list(range(start, stop + 1, 2))


print(even_product_ids(100, 110))
```

## 3. Countdown Retry Attempts

```python
def retry_countdown(max_attempts):
    for attempt in range(max_attempts, 0, -1):
        print(f"{attempt} attempts left")


retry_countdown(3)
```

## 4. Process Products in Batches

```python
def product_batches(products, batch_size):
    batches = []

    for start in range(0, len(products), batch_size):
        batches.append(products[start:start + batch_size])

    return batches


print(product_batches(["laptop", "mouse", "keyboard", "monitor"], 2))
```

## 5. Reverse a List With Indexes

```python
def reverse_with_range(items):
    result = []

    for index in range(len(items) - 1, -1, -1):
        result.append(items[index])

    return result


print(reverse_with_range(["laptop", "mouse", "keyboard"]))
```

## 6. Find Index of Product

```python
def find_product_index(products, target):
    for index in range(len(products)):
        if products[index] == target:
            return index
    return -1


print(find_product_index(["mouse", "laptop"], "laptop"))
```

## 7. Multiplication Table for Price

```python
def price_table(price, max_quantity):
    result = []

    for quantity in range(1, max_quantity + 1):
        result.append(price * quantity)

    return result


print(price_table(25, 5))
```

## 8. Validate Quantity Range

```python
def is_valid_quantity(quantity):
    return quantity in range(1, 11)


print(is_valid_quantity(5))
print(is_valid_quantity(11))
```

## 9. Sum Numbers From 1 to n

```python
def sum_range(n):
    total = 0

    for number in range(1, n + 1):
        total += number

    return total


print(sum_range(5))
```

## 10. FizzBuzz

```python
def fizz_buzz(n):
    result = []

    for number in range(1, n + 1):
        if number % 15 == 0:
            result.append("FizzBuzz")
        elif number % 3 == 0:
            result.append("Fizz")
        elif number % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(number))

    return result
```

## Summary

| Pattern | `range` use |
|---------|-------------|
| Repeat fixed times | `range(n)` |
| Human page numbers | `range(1, n + 1)` |
| Batches | `range(0, len(items), batch_size)` |
| Reverse indexes | `range(len(items) - 1, -1, -1)` |
| Validation | `value in range(...)` |

## See also

- [Python range core concepts](core-concepts.md)
- [Python range reference](range-reference.md)
- [Python range FAQ](frequently-asked-questions.md)
