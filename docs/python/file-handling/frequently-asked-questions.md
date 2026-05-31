# Python File Handling: Frequently Asked Interview Questions

## Basic Level

### 1. What is file handling in Python?

File handling means reading data from files and writing data to files using Python code.

### 2. Which function opens a file?

`open()` opens a file and returns a file object.

### 3. Why should you use `with open(...)`?

It automatically closes the file, even if an error happens.

### 4. What does file mode `r` mean?

`r` means read mode. The file must already exist.

### 5. What does file mode `w` mean?

`w` means write mode. It creates a new file or overwrites an existing file.

### 6. What does file mode `a` mean?

`a` means append mode. New content is added to the end of the file.

### 7. What does file mode `b` mean?

`b` means binary mode, used for non-text data such as Pickle files or images.

### 8. What is `encoding="utf-8"`?

It tells Python how to convert bytes into text characters.

### 9. How do you read an entire file?

Use `file.read()`.

### 10. How do you read a file line by line?

Iterate over the file object with `for line in file`.

## Intermediate Level

### 11. What is the difference between `read()`, `readline()`, and `readlines()`?

`read()` returns the full content, `readline()` returns one line, and `readlines()` returns a list of lines.

### 12. Why is line-by-line reading useful?

It avoids loading a large file fully into memory.

### 13. How do you write text to a file?

Use `file.write("text")`.

### 14. Does `write()` add a newline automatically?

No. Add `"\n"` yourself when needed.

### 15. What is CSV?

CSV stands for Comma-Separated Values. It stores tabular data.

### 16. Which module handles CSV files?

The `csv` module.

### 17. What is `csv.reader`?

It reads CSV rows as lists.

### 18. What is `csv.DictReader`?

It reads CSV rows as dictionaries using header names as keys.

### 19. Why use `newline=""` with CSV files?

It prevents extra blank lines and lets the `csv` module handle newlines correctly.

### 20. Are CSV values automatically converted to numbers?

No. CSV values are strings by default.

## Advanced Level

### 21. What is JSON?

JSON is a text format for structured data, commonly used by APIs and configuration files.

### 22. Which module handles JSON files?

The `json` module.

### 23. What is the difference between `json.load()` and `json.loads()`?

`json.load()` reads from a file object. `json.loads()` reads from a JSON string.

### 24. What is the difference between `json.dump()` and `json.dumps()`?

`json.dump()` writes JSON to a file object. `json.dumps()` returns a JSON string.

### 25. What is `indent=2` in `json.dump()`?

It pretty-prints JSON with two spaces of indentation.

### 26. What happens if JSON is invalid?

Python raises `json.JSONDecodeError`.

### 27. What is Pickle?

Pickle is a Python-specific binary serialization format for storing Python objects.

### 28. Which module handles Pickle?

The `pickle` module.

### 29. What modes are used for Pickle files?

Use `wb` for writing binary and `rb` for reading binary.

### 30. Why is Pickle unsafe for untrusted data?

Unpickling can execute code, so malicious Pickle files are dangerous.

## Pro Level

### 31. When should you choose CSV?

Choose CSV for simple tabular data such as product exports or inventory lists.

### 32. When should you choose JSON?

Choose JSON for nested, portable data such as orders, API payloads, and configuration.

### 33. When should you choose Pickle?

Choose Pickle only for trusted Python-specific object storage or caches.

### 34. What exception is raised when a file is missing?

`FileNotFoundError`.

### 35. What exception is raised for permission problems?

`PermissionError`.

### 36. What is a common file handling best practice?

Use `with open(...)`, specify encoding, and handle expected exceptions.

### 37. Why avoid hardcoded absolute paths?

They make programs less portable across machines and environments.

### 38. What is the difference between text and binary files?

Text files decode bytes into strings. Binary files work with raw bytes.

### 39. Can JSON store every Python object?

No. JSON supports common data types like dicts, lists, strings, numbers, booleans, and null, but not arbitrary Python objects.

### 40. What is the final interview rule?

Use the simplest file format that fits the data: text for lines, CSV for tables, JSON for portable structure, and Pickle only for trusted Python objects.

## Final Interview Checklist

- Know `open()` and `with open(...)`.
- Know `r`, `w`, `a`, `rb`, and `wb` modes.
- Use `encoding="utf-8"` for text files.
- Use `newline=""` for CSV.
- Know `csv.reader` vs `csv.DictReader`.
- Know `json.load` vs `json.loads`.
- Know `json.dump` vs `json.dumps`.
- Never unpickle untrusted data.
- Handle `FileNotFoundError`, `PermissionError`, and invalid JSON.

## See also

- [File handling: core concepts](core-concepts.md)
- [File handling reference](file-handling-reference.md)
- [File handling interview problems](interview-problems.md)
- [Python JSON](../json/core-concepts.md)
- [Exception handling](../exception-handling/core-concepts.md)
