# Advanced Python Interview Problems

## 1. Explain the GIL

### Problem

Explain why Python threads may not speed up a CPU-heavy report.

### Answer

In CPython, the GIL allows only one thread to execute Python bytecode at a time. For CPU-bound tasks like calculating a large sales report, multiple threads often do not run Python code in parallel.

Use multiprocessing for CPU-bound parallelism.

## 2. Choose Threading or Multiprocessing

### Problem

Choose a tool for each task.

| Task | Better choice |
|------|---------------|
| send order emails | threading |
| call payment API | threading or asyncio |
| resize product images | multiprocessing |
| calculate sales report | multiprocessing |

### Interview Point

Use threads for I/O-bound tasks and processes for CPU-bound tasks.

## 3. Show a CPU-Bound Task

```python
def calculate_report_total(numbers):
    total = 0
    for number in numbers:
        total += number * number
    return total
```

This is CPU-bound because most time is spent calculating.

## 4. Show an I/O-Bound Task

```python
import time


def fetch_stock_from_supplier(sku):
    time.sleep(1)
    return f"{sku}: available"
```

This is I/O-bound because it waits for an external response.

## 5. Explain Reference Counting

```python
product = {"name": "Laptop"}
same_product = product

del product
```

The object still exists because `same_product` still references it.

## 6. Explain a Circular Reference

```python
order = {}
customer = {}

order["customer"] = customer
customer["last_order"] = order
```

The objects refer to each other. If no outside references exist, Python's cyclic garbage collector can clean them.

## 7. Identify a Memory Leak Pattern

```python
order_cache = {}


def cache_order(order_id, order):
    order_cache[order_id] = order
```

If `order_cache` never removes old entries, memory usage can grow forever.

## 8. Fix an Unbounded Cache

```python
from functools import lru_cache


@lru_cache(maxsize=1000)
def get_product_details(product_id):
    return {"id": product_id, "name": "Laptop"}
```

Use a bounded cache instead of an unlimited dictionary.

## 9. Use a Generator to Save Memory

```python
def order_ids(orders):
    for order in orders:
        yield order["id"]
```

This avoids creating a full list of IDs.

## 10. Use Context Manager to Release Resources

```python
with open("orders.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

The file closes automatically when the block exits.

## 11. Use `gc` for Inspection

```python
import gc

print(gc.isenabled())
print(gc.get_count())
```

This is useful for learning and debugging, but application code rarely needs manual garbage collection.

## 12. Explain `sys.getsizeof()`

```python
import sys

cart = ["Laptop", "Mouse"]
print(sys.getsizeof(cart))
```

`sys.getsizeof()` shows shallow object size. It does not include the full size of referenced strings.

## Summary

In advanced Python interviews, connect internals to practical decisions: GIL affects CPU-bound threading, reference counting handles common cleanup, cyclic GC handles cycles, and memory growth usually means references are still alive.

## See also

- [Advanced Python: core concepts](core-concepts.md)
- [Advanced Python reference](advanced-python-reference.md)
- [Advanced Python FAQ](frequently-asked-questions.md)
