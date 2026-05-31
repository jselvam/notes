# Advanced Python Reference

## Quick Reference

| Topic | Meaning | Interview point |
|-------|---------|-----------------|
| GIL | Global Interpreter Lock | one Python thread executes bytecode at a time in CPython |
| CPU-bound work | calculation-heavy work | use multiprocessing for parallel speedup |
| I/O-bound work | waits for network, disk, database | threading or asyncio can help |
| memory management | automatic object allocation and cleanup | Python manages memory for you |
| reference counting | count references to each object | object can be freed when count becomes zero |
| garbage collection | cleanup unreachable objects | handles cycles reference counting misses |
| memory leak | memory retained unintentionally | often caused by lingering references |

## GIL Reference

The GIL exists in CPython, the most common Python implementation.

Key facts:

- only one thread executes Python bytecode at once
- threads can still overlap while waiting for I/O
- C extensions may release the GIL for heavy native work
- multiprocessing uses separate processes and can use multiple cores

## Threading vs Multiprocessing

| Work type | Better tool |
|-----------|-------------|
| send emails | threading |
| API calls | threading or asyncio |
| image resizing | multiprocessing |
| report calculation | multiprocessing |
| many async HTTP calls | asyncio |

## Memory Management Reference

Python memory management includes:

- object allocation
- reference counting
- cyclic garbage collection
- memory pools and arenas internally

Most application code should focus on object lifetime and references rather than manual memory allocation.

## Reference Counting

```python
product = {"sku": "LAP-101"}
cart_item = product
```

Both names refer to the same dictionary object.

When references are removed:

```python
del product
del cart_item
```

If no references remain, the object can be destroyed.

## Cyclic References

```python
order = {}
customer = {}

order["customer"] = customer
customer["last_order"] = order
```

These objects refer to each other. Python's cyclic garbage collector can clean them if they become unreachable.

## `gc` Module

The `gc` module exposes garbage collector controls and inspection helpers.

```python
import gc

print(gc.isenabled())
print(gc.get_count())
```

Manual collection:

```python
import gc

unreachable = gc.collect()
print(unreachable)
```

Most programs should not call `gc.collect()` routinely.

## `sys.getsizeof()`

```python
import sys

products = ["Laptop", "Mouse", "Keyboard"]
print(sys.getsizeof(products))
```

`sys.getsizeof()` returns the shallow size of an object, not the full deep size of all referenced objects.

## Memory Leak Patterns

| Pattern | Why it leaks |
|---------|--------------|
| growing global list | old objects are still referenced |
| unbounded dictionary cache | cache never evicts entries |
| closures retaining large objects | hidden reference remains |
| open files/connections | external resources not released |
| event listeners not removed | observer keeps object alive |

## Memory-Friendly Patterns

```python
def stream_order_ids(orders):
    for order in orders:
        yield order["id"]
```

Use generators to avoid building large intermediate lists.

```python
with open("orders.txt", "r", encoding="utf-8") as file:
    for line in file:
        process_order_line = line.strip()
```

Use context managers to release resources.

## Common Comparisons

| Comparison | Difference |
|------------|------------|
| GIL vs lock | GIL protects interpreter internals; lock protects your shared data |
| reference counting vs garbage collection | immediate cleanup vs cycle cleanup |
| shallow size vs deep size | object itself vs object plus referenced objects |
| memory leak in C vs Python | lost pointer vs retained references |
| threading vs multiprocessing | shared process vs separate processes |

## Best Practices

- Choose concurrency tools based on I/O-bound vs CPU-bound work.
- Do not assume threads speed up CPU-heavy Python.
- Avoid unbounded caches.
- Close files and connections with context managers.
- Use generators for large data streams.
- Use profiling tools before optimizing memory.
- Understand references when debugging memory growth.

## See also

- [Advanced Python: core concepts](core-concepts.md)
- [Advanced Python interview problems](interview-problems.md)
- [Advanced Python FAQ](frequently-asked-questions.md)
- [Concurrency](../concurrency/core-concepts.md)
- [Advanced functions](../advanced-functions/core-concepts.md)
