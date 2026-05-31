# Python Interview Questions & Answers

Short answers you can use in interviews, with examples. For string fundamentals, see [Python strings: core concepts](strings/core-concepts.md).

## Strings and text

### Are Python strings mutable?

**Answer:** No. `str` is **immutable**. Methods like `.replace()` and `.upper()` return **new** strings; the original object is unchanged unless you reassign the variable.

```python
s = "hello"
s.upper()
print(s)  # still "hello"
```

### What is the difference between `.find()` and `.index()`?

**Answer:** Both search for a substring. `.find()` returns **-1** if nothing matches. `.index()` raises **`ValueError`** if the substring is missing. Use `.find()` when “not found” is normal; use `.index()` when absence should be an error.

```python
"abc".find("z")   # -1
"abc".index("z")  # ValueError
```

### Why prefer `str.join()` over `+` in a loop?

**Answer:** Repeated `+` builds many intermediate string objects (O(n²) time and memory for n pieces). `join` allocates once over the iterable of pieces—clearer and usually much faster.

```python
parts = ["a", "b", "c"]
"".join(parts)  # preferred for many parts
```

### How does slicing `s[start:stop]` work?

**Answer:** **Start** is inclusive; **stop** is **exclusive**. Omitted `start` means from the beginning; omitted `stop` means through the end. Negative indices count from the right.

```python
s = "Python"
s[1:4]  # "yth" — indices 1, 2, 3 only
```

## Language basics

### What is the difference between `==` and `is`?

**Answer:** `==` compares **values** (equality). `is` compares **identity** (same object in memory). For strings, small literals may be interned, but you should use `==` for textual equality and `is` only for singletons like `None` (`x is None`).

```python
a = "hello"
b = "hello"
a == b   # True
a is b   # often True for CPython small strings, but do not rely on it for logic
```

### What are `*args` and `**kwargs`?

**Answer:** `*args` collects extra **positional** arguments into a **tuple**. `**kwargs` collects extra **keyword** arguments into a **dict**. Names `args`/`kwargs` are convention; the `*` and `**` matter.

```python
def f(a, *args, **kwargs):
    return a, args, kwargs

f(1, 2, 3, x=10)  # (1, (2, 3), {'x': 10})
```

### What is a list comprehension? When use it?

**Answer:** A compact way to build a list from an iterable, optionally with a filter. Prefer it for simple transforms; use a plain loop when logic is long or side effects make readability worse.

```python
[n * 2 for n in range(5) if n % 2 == 0]  # [0, 4, 8]
```

### What is the difference between a shallow copy and a deep copy?

**Answer:** A **shallow** copy duplicates the outer container but shares nested mutable objects. A **deep** copy recursively copies nested structures. Use `copy.copy` / `copy.deepcopy` from the `copy` module when you need explicit behavior.

```python
import copy
outer = [[1]]
shallow = copy.copy(outer)
deep = copy.deepcopy(outer)
shallow[0].append(2)  # mutates nested list shared with outer
```


### Why is `len()` a function and not a string method?

**Answer:** A **shallow**  In Python, `len()` is a built-in function that works on any object implementing the `__len__()` method. This design keeps the language consistent and allows a single interface to work across multiple data types like strings, lists, tuples, and dictionaries.


## Quick checklist before a screen

- Immutable types: `str`, `tuple`, `int`, etc.; mutable: `list`, `dict`, `set`.
- `None` checks: use `x is None`, not `x == None`.
- Strings: slicing rules, `.find` vs `.index`, `join` vs `+` in loops.
