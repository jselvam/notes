# Python Iterators: Core Concepts

An **iterator** is an object that returns values one at a time. Iterators are important in interviews because they explain how `for` loops, generators, lazy processing, and memory-efficient pipelines work.

In an online computer shopping system, iterators can help process:

- product catalog items one by one
- uploaded CSV rows
- order events from a queue
- paginated API results
- large report exports without loading everything into memory

## Iterable vs Iterator

An **iterable** can produce an iterator. Lists, tuples, dictionaries, sets, strings, and ranges are iterables.

An **iterator** remembers its current position and produces the next value using `next()`.

```python
products = ["laptop", "mouse", "keyboard"]

iterator = iter(products)

print(next(iterator))  # laptop
print(next(iterator))  # mouse
print(next(iterator))  # keyboard
```

When no values remain, `next()` raises `StopIteration`.

## How `for` Loops Work

A `for` loop internally calls `iter()` and then repeatedly calls `next()`.

```python
products = ["laptop", "mouse"]

for product in products:
    print(product)
```

Conceptually:

```python
iterator = iter(products)

while True:
    try:
        product = next(iterator)
    except StopIteration:
        break

    print(product)
```

## Custom Iterator

Create an iterator by implementing `__iter__()` and `__next__()`.

```python
class ProductIterator:
    def __init__(self, products):
        self.products = products
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.products):
            raise StopIteration

        product = self.products[self.index]
        self.index += 1
        return product


products = ProductIterator(["laptop", "mouse"])

for product in products:
    print(product)
```

## Generators

A generator is an easy way to create an iterator using `yield`.

```python
def product_stream():
    yield "laptop"
    yield "mouse"
    yield "keyboard"


for product in product_stream():
    print(product)
```

## Lazy Processing

Iterators are lazy: they produce values when asked.

```python
def order_ids():
    for order_id in range(1, 4):
        print(f"Generating {order_id}")
        yield order_id


ids = order_ids()
print(next(ids))
print(next(ids))
```

## Common Interview Points

### What is the difference between iterable and iterator?

An iterable can create an iterator. An iterator is the object that tracks state and returns the next value.

### What does `iter()` do?

`iter()` returns an iterator from an iterable.

### What does `next()` do?

`next()` returns the next value from an iterator.

### What is `StopIteration`?

The exception that signals an iterator has no more values.

## Practice Problems

1. Convert a list of products into an iterator and call `next()`.
2. Write a generator that yields product IDs from 101 to 105.
3. Write a custom iterator for cart items.
4. Explain why generators are memory efficient.
5. Show how a `for` loop uses `iter()` and `next()` internally.

## See also

- [Python iterator reference](iterator-reference.md)
- [Python iterator interview problems](interview-problems.md)
- [Python iterator FAQ](frequently-asked-questions.md)
- [Python control-flow reference](../control-flow/control-flow-reference.md)
