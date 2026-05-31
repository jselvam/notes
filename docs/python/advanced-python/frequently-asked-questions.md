# Advanced Python: Frequently Asked Interview Questions

## Basic Level

### 1. What is the GIL?

The GIL is the Global Interpreter Lock. In CPython, it allows only one thread to execute Python bytecode at a time.

### 2. Why does Python have a GIL?

It simplifies CPython memory management and protects internal interpreter data structures.

### 3. Does every Python implementation have a GIL?

No. The GIL is mainly associated with CPython, the most common Python implementation.

### 4. Does the GIL prevent all concurrency?

No. Threads can still be useful for I/O-bound tasks.

### 5. What is CPU-bound work?

CPU-bound work spends most time doing calculations.

### 6. What is I/O-bound work?

I/O-bound work spends most time waiting for network, disk, database, or external services.

### 7. What is memory management?

Memory management is how Python allocates, tracks, and frees memory used by objects.

### 8. Does Python require manual memory allocation?

No. Python manages object memory automatically.

### 9. What is garbage collection?

Garbage collection is the process of freeing memory used by objects that are no longer reachable.

### 10. What is reference counting?

Reference counting tracks how many references point to an object.

## Intermediate Level

### 11. How does CPython usually free objects?

When an object's reference count reaches zero, CPython can destroy it.

### 12. What is a reference?

A reference is a name, container entry, or object attribute that points to an object.

### 13. What does `del` do?

`del` removes a reference. It does not necessarily destroy the object if other references still exist.

### 14. What is a circular reference?

A circular reference happens when objects refer to each other in a cycle.

### 15. Why is reference counting not enough for cycles?

Objects in a cycle can keep each other's reference count above zero even when unreachable from the program.

### 16. What handles circular references?

Python's cyclic garbage collector.

### 17. What is generational garbage collection?

It groups objects by age and checks younger objects more often because many objects die young.

### 18. What is the `gc` module?

The `gc` module exposes tools for controlling and inspecting Python's cyclic garbage collector.

### 19. Should you call `gc.collect()` often?

Usually no. Python manages garbage collection automatically.

### 20. What is a memory leak in Python?

A memory leak happens when objects are no longer needed but are still referenced.

## Advanced Level

### 21. Why do threads not speed up CPU-heavy Python code much?

Because the GIL allows only one thread to execute Python bytecode at a time in CPython.

### 22. When are threads useful despite the GIL?

Threads help when tasks wait for I/O, such as API calls, file reads, or database operations.

### 23. How can Python use multiple CPU cores?

Use multiprocessing, native extensions that release the GIL, or external systems.

### 24. What is multiprocessing's memory trade-off?

Processes have separate memory, so data sharing is more expensive than with threads.

### 25. What is the difference between GIL and a normal lock?

The GIL protects interpreter internals. A normal lock protects your application data.

### 26. Can race conditions still happen with the GIL?

Yes. The GIL does not make multi-step application logic automatically safe.

### 27. Give an example of a Python memory leak.

An unbounded global cache that stores every order forever can leak memory.

### 28. How can you prevent unbounded cache memory growth?

Use a bounded cache, eviction policy, TTL, or clear unused entries.

### 29. Why do context managers help memory and resources?

They release resources such as files, locks, and connections reliably.

### 30. Why do generators help memory?

They produce values one at a time instead of storing all values in a list.

## Pro Level

### 31. What is `sys.getsizeof()`?

It returns the shallow size of an object in bytes.

### 32. What does shallow size mean?

It measures the object itself, not every object it references.

### 33. Why can measuring Python memory be tricky?

Objects reference other objects, memory allocators reuse memory, and process memory may not shrink immediately.

### 34. What are object pools?

CPython may reuse memory for small objects to improve performance.

### 35. Why might memory not return to the OS immediately?

Python's allocator can keep memory available for future Python objects.

### 36. What is a weak reference?

A weak reference points to an object without increasing its lifetime.

### 37. When are weak references useful?

They are useful for caches, observers, and non-owning references.

### 38. What is a finalizer?

A finalizer is cleanup logic that runs when an object is destroyed, such as `__del__()`.

### 39. Why should `__del__()` be used carefully?

Finalizers can make object cleanup order and cycles harder to reason about.

### 40. What is the final advanced Python interview answer?

Python manages memory automatically, CPython uses reference counting plus cyclic garbage collection, the GIL limits CPU-bound threading, and good code avoids unnecessary long-lived references.

## Final Interview Checklist

- Explain the GIL clearly.
- Know that the GIL mainly affects CPU-bound threading.
- Use multiprocessing for CPU-bound parallelism.
- Use threading or asyncio for I/O-bound work.
- Explain reference counting.
- Explain circular references.
- Know why garbage collection is still needed.
- Know common memory leak patterns.
- Use generators and context managers for memory-friendly code.
- Measure before optimizing.

## See also

- [Advanced Python: core concepts](core-concepts.md)
- [Advanced Python reference](advanced-python-reference.md)
- [Advanced Python interview problems](interview-problems.md)
- [Concurrency](../concurrency/core-concepts.md)
- [Advanced functions](../advanced-functions/core-concepts.md)
