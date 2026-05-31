# Python Strings: Core Concepts & Operations

Strings in Python are **sequences of characters** used for textual data. They are **immutable**: methods that “change” a string return a new string unless you reassign the variable.

## Basics

### Quotes

Use single (`'`) or double (`"`) quotes. Mix them so you do not need escapes for the inner quote, or escape with `\'` inside a single-quoted string.

```python
single = 'hello'
double = "hello"
possessive = "Bobby's World"   # double quotes wrap a single quote in the text
escaped = 'Bobby\'s World'     # or escape the apostrophe
```

### Multi-line strings

Triple quotes (`'''` or `"""`) span multiple lines. They are often used for docstrings and blocks of text.

```python
poem = """Line one
Line two
Still the same string"""
```

## Length, indexing, and slicing

### `len()`

`len(s)` returns how many characters are in the string.

```python
s = "Python"
print(len(s))  # 6
```

### Indexing

Use `[index]` to read one character. Indexing **starts at 0**. Negative indices count from the end (`-1` is the last character).

```python
s = "Python"
print(s[0])   # P
print(s[-1])  # n
```

### Slicing

`[start:stop]` returns a substring. **Start is inclusive; stop is exclusive.** Omitting `start` means “from the beginning”; omitting `stop` means “through the end”.

```python
s = "Python"
print(s[0:3])   # Pyt  (indices 0, 1, 2 — not 3)
print(s[2:])    # thon
print(s[:4])    # Pyth
```

## Common string methods

### Case

```python
t = "Hello World"
print(t.lower())  # hello world
print(t.upper())  # HELLO WORLD
# t is unchanged; these return new strings
```

### Search and count

```python
s = "banana"
print(s.count("a"))    # 3
print(s.count("na"))   # 2
print(s.find("na"))    # 2 — index of first occurrence
print(s.find("xyz"))   # -1 — not found
```

### Replacement

`replace(old, new)` returns a **new** string. The original is unchanged unless you assign back.

```python
msg = "hello world"
fixed = msg.replace("world", "there")
print(fixed)  # hello there
print(msg)    # hello world
msg = msg.replace("world", "there")  # now msg points to the new string
```

## Concatenation and formatting

### `+`

```python
first = "Hello"
second = "World"
print(first + ", " + second + "!")  # Hello, World!
```

### `.format()`

Use `{}` placeholders and pass values positionally or by name.

```python
name = "Sam"
score = 95
print("{}, you scored {}.".format(name, score))
print("{n} scored {s}.".format(n=name, s=score))
```

### F-strings (Python 3.6+)

Prefix the string with `f` and put expressions inside `{...}`.

```python
name = "Sam"
print(f"{name} scored {95}.")
print(f"Shout: {name.upper()}")  # expressions allowed in braces
```

## Exploring the string API in the REPL

Use `dir` on a string (or any object) to see available attributes and methods. Use `help` for documentation on the `str` type or a specific method.

```python
s = "demo"
print([x for x in dir(s) if not x.startswith("_")])  # public methods, quick peek

help(str)           # overview of string methods
help(str.replace)   # one method’s docstring
```

In practice you often rely on editor completion and the official docs; `help` is handy when you are offline or in the REPL.

---

**Quick recap**

| Topic | Idea |
|-------|------|
| Quotes / multiline | `'`, `"`, `'''` / `"""` |
| Length / access | `len(s)`, `s[i]`, `s[start:stop]` (stop exclusive) |
| Case | `.lower()`, `.upper()` |
| Find / count | `.find()`, `.count()` |
| Replace | `.replace(old, new)` → new string |
| Build text | `+`, `.format()`, `f"..."` |
| Discovery | `dir(x)`, `help(str)` |

## See also

- [Strings practice (to-do tasks)](practice-tasks.md)
- [Python interview questions & answers](../interview-questions.md)

> Why is `len()` a function and not a string method?

You can say:

> In Python, `len()` is a built-in function that works on any object implementing the `__len__()` method. This design keeps the language consistent and allows a single interface to work across multiple data types like strings, lists, tuples, and dictionaries.
