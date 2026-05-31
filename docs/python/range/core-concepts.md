# Python `range`: Core Concepts

`range` represents an immutable sequence of integers. It is most often used with `for` loops when you need indexes, counters, pagination, batching, or repeated work.

In an online computer shopping system, `range` can help with:

- page numbers in product listing
- batch processing orders
- retry attempts
- generating product IDs for tests
- looping over list indexes

## Basic Syntax

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

`stop` is exclusive.

```python
for number in range(5):
    print(number)
# 0, 1, 2, 3, 4
```

## Start and Stop

```python
for page in range(1, 6):
    print(f"Load page {page}")
# 1, 2, 3, 4, 5
```

## Step

```python
for product_id in range(100, 111, 2):
    print(product_id)
# 100, 102, 104, 106, 108, 110
```

## Reverse Range

Use a negative step.

```python
for countdown in range(5, 0, -1):
    print(countdown)
```

## `range` Is Lazy

`range` does not build a full list immediately.

```python
numbers = range(1_000_000)
print(numbers)
```

This is memory efficient for large sequences.

## Convert Range to List

```python
pages = list(range(1, 6))
print(pages)
# [1, 2, 3, 4, 5]
```

## Membership Check

`range` supports membership checks.

```python
valid_quantity = 5 in range(1, 11)
print(valid_quantity)  # True
```

## Common Interview Points

### Why does `range(5)` stop at `4`?

Because the stop value is exclusive.

### Is `range` a list?

No. It is a lazy range object.

### When should you use `enumerate()` instead of `range(len(...))`?

Use `enumerate()` when you need both index and value.

```python
cart = ["laptop", "mouse"]

for index, item in enumerate(cart):
    print(index, item)
```

## Practice Problems

1. Print product page numbers from 1 to 10.
2. Print even product IDs from 100 to 120.
3. Count down retry attempts from 3 to 1.
4. Process cart items by index using `range(len(cart))`.
5. Replace `range(len(items))` with `enumerate()`.

## See also

- [Python range reference](range-reference.md)
- [Python range interview problems](interview-problems.md)
- [Python range FAQ](frequently-asked-questions.md)
- [Python control-flow reference](../control-flow/control-flow-reference.md)
