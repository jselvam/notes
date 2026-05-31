# Python Concurrency: Core Concepts

Concurrency means handling multiple tasks during the same time period. In Python, common concurrency tools are:

- `threading`
- `multiprocessing`
- `asyncio`
- locks for race conditions

Examples use an online computer shopping system.

## Concurrency vs Parallelism

| Term | Meaning |
|------|---------|
| Concurrency | managing many tasks at once |
| Parallelism | running many tasks at the exact same time |

Concurrency is useful when tasks wait for I/O, such as API calls or file reads. Parallelism is useful when CPU-heavy work must use multiple cores.

## Threading

Threading runs multiple threads inside one process.

Use threading mostly for I/O-bound work:

- sending order emails
- downloading product images
- checking stock from external APIs
- writing logs

```python
import threading


def send_email(order_id):
    print(f"Sending email for order {order_id}")


thread = threading.Thread(target=send_email, args=(1001,))
thread.start()
thread.join()
```

`join()` waits for the thread to finish.

## Multiprocessing

Multiprocessing runs separate Python processes.

Use multiprocessing for CPU-bound work:

- large report generation
- image resizing
- heavy price analysis
- large data processing

```python
from multiprocessing import Process


def calculate_report(order_count):
    print(f"Generating report for {order_count} orders")


process = Process(target=calculate_report, args=(50000,))
process.start()
process.join()
```

Each process has separate memory.

## Asyncio

`asyncio` runs many tasks cooperatively in one thread using an event loop.

Use `asyncio` for many I/O-bound tasks:

- calling product APIs
- fetching shipping rates
- checking payment status
- waiting for network responses

```python
import asyncio


async def fetch_product(product_id):
    await asyncio.sleep(1)
    return f"Product {product_id}"


async def main():
    results = await asyncio.gather(
        fetch_product(101),
        fetch_product(102),
        fetch_product(103),
    )
    print(results)


asyncio.run(main())
```

`await` pauses one coroutine so another can run.

## Race Conditions

A race condition happens when multiple workers access shared data and the final result depends on timing.

```python
stock = 1


def buy_product():
    global stock
    if stock > 0:
        stock -= 1
```

If two threads run this at the same time, both may see `stock > 0` before either updates it.

## Fixing Race Conditions With Lock

```python
import threading

stock = 1
lock = threading.Lock()


def buy_product():
    global stock
    with lock:
        if stock > 0:
            stock -= 1
            print("Purchase successful")
        else:
            print("Out of stock")
```

A lock ensures only one thread enters the protected section at a time.

## The GIL

Python's Global Interpreter Lock (GIL) allows only one thread to execute Python bytecode at a time in the standard CPython implementation.

Important interview point:

- threads help I/O-bound tasks
- threads usually do not speed up CPU-bound Python code
- multiprocessing can use multiple CPU cores
- asyncio is efficient for many waiting tasks

## Choosing the Right Tool

| Need | Tool |
|------|------|
| many blocking I/O tasks | threading |
| CPU-heavy tasks | multiprocessing |
| many network tasks with async libraries | asyncio |
| shared state protection | lock |

## Common Gotchas

### Threading is not always faster

For CPU-bound work, the GIL can prevent true parallel speedup.

### Async code needs async libraries

`asyncio` works best with libraries that support `async`/`await`.

### Multiprocessing copies data

Processes do not share normal memory by default.

### Locks can cause deadlocks

Always keep locked sections small and predictable.

## See also

- [Concurrency reference](concurrency-reference.md)
- [Concurrency interview problems](interview-problems.md)
- [Concurrency FAQ](frequently-asked-questions.md)
- [Python iterators](../iterators/core-concepts.md)
- [Exception handling](../exception-handling/core-concepts.md)
