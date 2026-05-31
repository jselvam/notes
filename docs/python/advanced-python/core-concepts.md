# Advanced Python: Core Concepts

Advanced Python internals help you understand performance, memory usage, and concurrency behavior.

This page covers:

- GIL: Global Interpreter Lock
- memory management
- reference counting
- garbage collection
- common interview explanations

Examples use an online computer shopping system.

## Why Advanced Python Internals Matter

In interviews, these topics show that you understand how Python behaves beyond normal syntax.

They help answer questions like:

- Why do threads not always speed up Python code?
- When is multiprocessing better than threading?
- How does Python free unused objects?
- Why can circular references be tricky?
- How can memory leaks happen in Python?

## GIL

GIL stands for **Global Interpreter Lock**.

In CPython, the GIL is a lock that allows only one thread to execute Python bytecode at a time.

Important points:

- it protects CPython's internal memory structures
- it makes many object operations simpler and safer internally
- it limits CPU-bound threading performance
- it does not stop threads from helping I/O-bound tasks

## GIL Example

```python
import threading


def calculate_totals():
    total = 0
    for number in range(10_000_000):
        total += number
    return total


thread = threading.Thread(target=calculate_totals)
thread.start()
thread.join()
```

For CPU-heavy work like report calculation, threads may not improve speed much because of the GIL.

## When Threads Still Help

Threads are useful for I/O-bound work:

```python
import threading
import time


def send_order_email(order_id):
    time.sleep(1)
    print(f"Email sent for order {order_id}")


threads = [
    threading.Thread(target=send_order_email, args=(1001,)),
    threading.Thread(target=send_order_email, args=(1002,)),
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
```

While one thread waits for I/O, another can run.

## Memory Management

Python manages memory automatically. You usually create objects and let Python clean them up.

```python
cart = {
    "items": ["Laptop", "Mouse"],
    "total": 1025.49,
}
```

Python allocates memory for the dictionary, list, strings, and number objects.

## Private Heap

CPython stores objects in a private heap managed by Python's memory manager.

The programmer does not manually allocate and free memory like in C.

## Reference Counting

CPython primarily uses reference counting.

Each object keeps track of how many references point to it.

```python
product = {"name": "Laptop"}
same_product = product
```

The dictionary has two references: `product` and `same_product`.

When the reference count becomes zero, CPython can immediately destroy the object.

## Garbage Collection

Reference counting cannot clean all circular references by itself.

Example:

```python
cart = {}
cart["self"] = cart
```

The dictionary refers to itself. Its reference count may not become zero through normal reference counting.

Python's cyclic garbage collector finds and cleans unreachable reference cycles.

## Generational Garbage Collection

Python's cyclic garbage collector groups objects into generations.

Basic idea:

- new objects are checked more often
- long-lived objects are checked less often
- this improves performance because many objects die young

## Memory Leaks in Python

Python has automatic memory management, but memory leaks can still happen.

Common causes:

- global lists or caches that keep growing
- references kept longer than needed
- circular references involving finalizers
- open resources not closed
- large objects kept in closures

## Example: Accidental Growing Cache

```python
order_cache = {}


def remember_order(order_id, order):
    order_cache[order_id] = order
```

If this cache never removes old orders, memory usage can keep growing.

## Best Practices

- Use generators for large streams.
- Use context managers to close files and connections.
- Avoid unbounded global caches.
- Use weak references for non-owning references when needed.
- Use multiprocessing for CPU-bound parallelism.
- Use threading or asyncio for I/O-bound work.
- Measure memory before optimizing.

## See also

- [Advanced Python reference](advanced-python-reference.md)
- [Advanced Python interview problems](interview-problems.md)
- [Advanced Python FAQ](frequently-asked-questions.md)
- [Concurrency](../concurrency/core-concepts.md)
- [Advanced functions](../advanced-functions/core-concepts.md)
