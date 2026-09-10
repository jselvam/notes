# Selvam's Python Notes

This repository contains a MkDocs study site for Python concepts, interview preparation, data structures, and practical backend topics. The notes are organized for quick revision, hands-on examples, common interview questions, and problem-solving practice.

## Topics Covered

### Core Language

- User input and validation
- Operators and precedence
- Control flow with conditions, loops, loop `else`, and `match`
- Functions, parameters, arguments, scope, and common function patterns
- Advanced functions, including generators, decorators, and context managers
- Iterators and iteration protocol
- Modules and imports
- Exception handling with `try`, `except`, `else`, `finally`, and `raise`
- Common Python error types and debugging basics

### Built-in Types

- Strings and string methods
- String formatting with f-strings, `str.format()`, and `%` formatting
- Lists, list methods, and list item removal
- Tuples and tuple usage patterns
- Dictionaries and dictionary methods
- Sets and set methods
- Numbers, numeric operations, and precision topics
- `range` usage patterns
- Booleans, truthiness, `any()`, and `all()`
- `NoneType`, optional returns, and sentinel patterns
- Binary types such as `bytes`, `bytearray`, and `memoryview`

### Data Structures and Algorithms

- Recursion and backtracking foundations
- Dynamic programming
- Searching algorithms, including linear and binary search patterns
- Sorting algorithms and sorting trade-offs
- Sliding window problems for fixed-size and moving-window arrays
- Stacks, queues, and linked lists
- Hash tables
- Trees and tree traversal
- Heap and priority queue problems
- Graph basics, BFS, DFS, and graph representations
- Advanced graph algorithms, including shortest paths, MSTs, and Union Find

### Object-Oriented Programming

- OOP fundamentals
- Classes and objects
- Dunder methods and operator overloading
- Class properties, instance properties, and `self`
- Inheritance and method overriding
- Encapsulation and controlled mutation
- Data abstraction and abstract base classes
- Polymorphism and duck typing
- Class relationships such as association, aggregation, and composition
- Advanced OOP concepts such as MRO, mixins, and introspection
- Python-specific OOP features such as dataclasses, slots, descriptors, and metaclasses
- Design principles such as SOLID, DRY, KISS, and dependency injection
- Design patterns such as Factory, Strategy, Observer, Decorator, Adapter, and Command

### Advanced Python

- Python internals and CPython behavior
- The GIL and concurrency trade-offs
- Memory management, references, garbage collection, and memory-friendly patterns
- Threading, multiprocessing, and `asyncio`

### Standard Library

- Dates and times with `datetime`, `date`, and `timedelta`
- Maths with `math`, `statistics`, `random`, `Decimal`, and `Fraction`
- JSON parsing and serialization
- Regular expressions with the `re` module
- File handling, CSV, JSON files, Pickle, and file exceptions

### Web, API, Database, and Tooling

- REST API design, HTTP methods, status codes, pagination, validation, and versioning
- MySQL CRUD from Python, parameterized queries, transactions, and SQL safety
- `pip`, package installation, dependency management, and `requirements.txt`
- Virtual environments with `venv`

### Interview Preparation

- Topic-specific interview problems
- Frequently asked questions for each major topic
- Data-structure interview questions
- Python tricky topics and common pitfalls

## Repository Layout

```text
mkdocs.yml          # MkDocs configuration and sidebar navigation
docs/               # Markdown source files
docs/python/        # Python notes organized by topic
site/               # Generated build output, not edited manually
```

## Running the Notes Locally

Install MkDocs if it is not already available:

```bash
python -m pip install mkdocs
```

Start a local preview server:

```bash
mkdocs serve
```

Build the static site:

```bash
mkdocs build
```

For a stricter validation build:

```bash
mkdocs build --strict
```

## Exporting as a Printable Book

Generate one HTML file from the order in `mkdocs.yml`:

```bash
python scripts/build_book_html.py
```

Generate only the Python notes:

```bash
python scripts/build_book_html.py --section Python --output site/python-book.html
```

Open the generated HTML file in a browser and use the browser print dialog to save it as a PDF.

## Study Flow

Start with the core language and built-in types, then move into object-oriented programming, data structures, and standard library topics. For interview preparation, review each topic's core concepts first, then solve the interview problems and finish with the frequently asked questions.
