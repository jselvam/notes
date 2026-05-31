# Python Concurrency Interview Problems

## 1. Run a Task in a Thread

### Problem

Send an order email without blocking the main flow.

```python
import threading


def send_email(order_id):
    print(f"Email sent for order {order_id}")


thread = threading.Thread(target=send_email, args=(1001,))
thread.start()
thread.join()
```

### Interview Point

Threading is useful for I/O-bound work.

## 2. Fetch Inventory With Thread Pool

```python
from concurrent.futures import ThreadPoolExecutor


def fetch_stock(sku):
    return f"{sku}: in stock"


skus = ["LAP-101", "MOU-201", "KEY-301"]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(fetch_stock, skus))

print(results)
```

### Complexity

Total time can improve when tasks wait on I/O.

## 3. Run CPU Work in a Process

```python
from multiprocessing import Process


def build_sales_report(month):
    print(f"Building report for {month}")


process = Process(target=build_sales_report, args=("May",))
process.start()
process.join()
```

### Interview Point

Processes can bypass the GIL for CPU-bound work.

## 4. Use Process Pool for CPU Tasks

```python
from concurrent.futures import ProcessPoolExecutor


def calculate_discounted_total(total):
    return total * 0.9


totals = [1000, 2500, 700]

with ProcessPoolExecutor() as executor:
    discounted = list(executor.map(calculate_discounted_total, totals))

print(discounted)
```

## 5. Fetch Shipping Rates With Asyncio

```python
import asyncio


async def fetch_rate(order_id):
    await asyncio.sleep(1)
    return f"Rate fetched for order {order_id}"


async def main():
    rates = await asyncio.gather(
        fetch_rate(1001),
        fetch_rate(1002),
        fetch_rate(1003),
    )
    print(rates)


asyncio.run(main())
```

## 6. Explain `await`

`await` pauses the current coroutine until a result is ready. During that waiting time, the event loop can run other coroutines.

## 7. Demonstrate a Race Condition

```python
stock = 1


def buy_product():
    global stock
    if stock > 0:
        stock -= 1
```

Two threads can both pass the `stock > 0` check before either updates the value.

## 8. Fix Race Condition With Lock

```python
import threading

stock = 1
lock = threading.Lock()


def buy_product():
    global stock
    with lock:
        if stock > 0:
            stock -= 1
            return "Purchased"
        return "Out of stock"
```

## 9. Choose Threading, Multiprocessing, or Asyncio

| Scenario | Best choice |
|----------|-------------|
| download product images | threading or asyncio |
| calculate large reports | multiprocessing |
| call many async APIs | asyncio |
| update shared stock | lock-protected threading or database transaction |

## 10. Explain the GIL

The GIL is a CPython mechanism that allows only one thread to execute Python bytecode at a time. It limits CPU-bound threading performance but does not prevent threads from helping I/O-bound tasks.

## 11. Avoid Shared State

```python
def calculate_total(items):
    return sum(item["price"] * item["quantity"] for item in items)
```

Pure functions avoid shared mutable state and are easier to run concurrently.

## 12. Use Queue for Thread Communication

```python
from queue import Queue

orders = Queue()
orders.put(1001)
orders.put(1002)

while not orders.empty():
    print(f"Processing order {orders.get()}")
```

Queues are safer than manually sharing lists between threads.

## Summary

Use threads for I/O, processes for CPU, asyncio for async I/O, and locks or queues to control shared state.

## See also

- [Concurrency: core concepts](core-concepts.md)
- [Concurrency reference](concurrency-reference.md)
- [Concurrency FAQ](frequently-asked-questions.md)
