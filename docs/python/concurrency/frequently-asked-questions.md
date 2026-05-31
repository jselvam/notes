# Python Concurrency: Frequently Asked Interview Questions

## Basic Level

### 1. What is concurrency?

Concurrency means managing multiple tasks during the same time period.

### 2. What is parallelism?

Parallelism means running multiple tasks at the exact same time, usually on multiple CPU cores.

### 3. What is threading?

Threading runs multiple threads inside the same process.

### 4. What is multiprocessing?

Multiprocessing runs multiple separate processes.

### 5. What is asyncio?

`asyncio` is Python's library for cooperative asynchronous programming using an event loop.

### 6. What is a race condition?

A race condition happens when the result depends on timing between concurrent workers.

### 7. What is a lock?

A lock allows only one worker to enter a critical section at a time.

### 8. What is the GIL?

The Global Interpreter Lock allows only one thread to execute Python bytecode at a time in CPython.

### 9. What is I/O-bound work?

I/O-bound work spends most time waiting for network, disk, database, or external services.

### 10. What is CPU-bound work?

CPU-bound work spends most time doing calculations.

## Intermediate Level

### 11. When should you use threading?

Use threading for blocking I/O tasks such as sending emails, reading files, or calling APIs.

### 12. When should you use multiprocessing?

Use multiprocessing for CPU-heavy tasks that can benefit from multiple cores.

### 13. When should you use asyncio?

Use asyncio for many I/O tasks when libraries support `async` and `await`.

### 14. What does `thread.start()` do?

It starts executing the thread's target function.

### 15. What does `thread.join()` do?

It waits until the thread finishes.

### 16. What does `process.join()` do?

It waits until the process finishes.

### 17. What is `async def`?

It defines a coroutine function.

### 18. What does `await` do?

It pauses a coroutine until the awaited operation is ready, allowing other coroutines to run.

### 19. What does `asyncio.gather()` do?

It schedules multiple awaitable tasks and waits for their results.

### 20. What does `asyncio.run()` do?

It starts an event loop, runs the main coroutine, and closes the loop.

## Advanced Level

### 21. Why does threading not speed up CPU-bound Python code much?

The GIL prevents multiple Python threads from executing Python bytecode in parallel in CPython.

### 22. Can threads still be useful despite the GIL?

Yes. Threads are useful when tasks spend time waiting for I/O.

### 23. Why can multiprocessing use multiple CPU cores?

Each process has its own Python interpreter and memory space.

### 24. What is a critical section?

A critical section is code that accesses shared state and must not be run by multiple workers at the same time.

### 25. How do you fix a race condition?

Use locks, queues, atomic operations, database transactions, or avoid shared mutable state.

### 26. What is a deadlock?

A deadlock happens when workers wait forever for locks held by each other.

### 27. How do you reduce deadlock risk?

Keep locked sections small and acquire locks in a consistent order.

### 28. What is the difference between threading and asyncio?

Threading uses OS-managed threads. Asyncio uses one event loop and cooperative coroutines.

### 29. What is the difference between multiprocessing and threading?

Threads share memory in one process. Processes have separate memory and higher overhead.

### 30. What is the difference between `ThreadPoolExecutor` and `ProcessPoolExecutor`?

`ThreadPoolExecutor` uses threads for I/O-bound work. `ProcessPoolExecutor` uses processes for CPU-bound work.

## Pro Level

### 31. What is cooperative multitasking?

Tasks voluntarily give control back to the event loop, usually at `await` points.

### 32. What happens if CPU-heavy code runs inside an asyncio coroutine?

It blocks the event loop and delays other coroutines.

### 33. How can asyncio run blocking code safely?

Use executors such as `loop.run_in_executor()` or move CPU-heavy work to processes.

### 34. Is a Python list thread-safe?

Some individual operations may be atomic in CPython, but relying on that for program correctness is unsafe.

### 35. Why is shared mutable state dangerous?

Multiple workers can read and write in unexpected orders.

### 36. How can queues help threading?

Queues provide safer communication between producer and consumer threads.

### 37. Should inventory stock updates rely only on Python locks?

In real systems, use database transactions or atomic database updates because multiple app servers may be involved.

### 38. Can multiprocessing share data?

Yes, but it needs special tools such as queues, pipes, shared memory, or managers.

### 39. What should you say in an interview about concurrency choice?

Use threads for I/O-bound blocking work, processes for CPU-bound work, asyncio for async I/O, and locks or transactions for shared state.

### 40. What is the final concurrency warning?

Concurrency can improve throughput, but it also adds complexity, race conditions, debugging difficulty, and coordination overhead.

## Final Interview Checklist

- Know concurrency vs parallelism.
- Use threading for I/O-bound tasks.
- Use multiprocessing for CPU-bound tasks.
- Use asyncio for async I/O.
- Understand the GIL.
- Explain race conditions clearly.
- Fix shared state with locks, queues, or transactions.
- Avoid blocking the asyncio event loop.
- Keep concurrency code simple and testable.

## See also

- [Concurrency: core concepts](core-concepts.md)
- [Concurrency reference](concurrency-reference.md)
- [Concurrency interview problems](interview-problems.md)
- [Exception handling](../exception-handling/core-concepts.md)
