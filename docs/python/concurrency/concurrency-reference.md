# Python Concurrency Reference

## Quick Reference

| Topic | Tool | Best for |
|-------|------|----------|
| Threading | `threading.Thread` | I/O-bound tasks |
| Thread pool | `ThreadPoolExecutor` | many small I/O jobs |
| Multiprocessing | `multiprocessing.Process` | CPU-bound tasks |
| Process pool | `ProcessPoolExecutor` | parallel CPU work |
| Asyncio | `async`, `await`, `asyncio.gather` | many async I/O tasks |
| Race condition fix | `Lock` | protecting shared state |

## Threading

```python
import threading


def send_notification(order_id):
    print(f"Notify customer for order {order_id}")


thread = threading.Thread(target=send_notification, args=(1001,))
thread.start()
thread.join()
```

## ThreadPoolExecutor

```python
from concurrent.futures import ThreadPoolExecutor


def fetch_inventory(sku):
    return f"{sku}: available"


skus = ["LAP-101", "MOU-201", "KEY-301"]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(fetch_inventory, skus))

print(results)
```

## Multiprocessing

```python
from multiprocessing import Process


def resize_product_images(category):
    print(f"Resizing images for {category}")


process = Process(target=resize_product_images, args=("laptops",))
process.start()
process.join()
```

## ProcessPoolExecutor

```python
from concurrent.futures import ProcessPoolExecutor


def calculate_tax(total):
    return total * 0.18


totals = [1000, 2500, 999]

with ProcessPoolExecutor() as executor:
    taxes = list(executor.map(calculate_tax, totals))

print(taxes)
```

## Asyncio

```python
import asyncio


async def fetch_shipping_rate(order_id):
    await asyncio.sleep(1)
    return f"Rate for order {order_id}"


async def main():
    rates = await asyncio.gather(
        fetch_shipping_rate(1001),
        fetch_shipping_rate(1002),
    )
    print(rates)


asyncio.run(main())
```

## Race Condition Example

```python
stock = 1


def unsafe_buy():
    global stock
    if stock > 0:
        stock -= 1
```

This check-update sequence is not safe when multiple threads run it.

## Lock

```python
import threading

lock = threading.Lock()
stock = 1


def safe_buy():
    global stock
    with lock:
        if stock > 0:
            stock -= 1
```

## Common Methods

| API | Purpose |
|-----|---------|
| `Thread(target=...)` | create thread |
| `thread.start()` | start thread |
| `thread.join()` | wait for thread |
| `Process(target=...)` | create process |
| `process.start()` | start process |
| `async def` | define coroutine |
| `await` | wait without blocking event loop |
| `asyncio.gather()` | run coroutines concurrently |
| `asyncio.run()` | start event loop |
| `Lock()` | create lock |

## Common Comparisons

| Comparison | Difference |
|------------|------------|
| threading vs multiprocessing | threads share memory; processes have separate memory |
| threading vs asyncio | threads are OS-managed; asyncio uses cooperative coroutines |
| multiprocessing vs asyncio | multiprocessing is for CPU parallelism; asyncio is for async I/O |
| concurrency vs parallelism | concurrency manages tasks; parallelism runs tasks simultaneously |
| lock vs semaphore | lock allows one worker; semaphore allows limited workers |

## Best Practices

- Use threads for blocking I/O.
- Use processes for CPU-heavy work.
- Use asyncio with async-compatible libraries.
- Avoid shared mutable state when possible.
- Protect shared state with locks.
- Keep lock-protected code small.
- Prefer executors for simple pools of work.

## See also

- [Concurrency: core concepts](core-concepts.md)
- [Concurrency interview problems](interview-problems.md)
- [Concurrency FAQ](frequently-asked-questions.md)
