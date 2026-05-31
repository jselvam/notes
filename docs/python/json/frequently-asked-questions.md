# Python JSON: Frequently Asked Interview Questions

## Basic Level

### 1. What is JSON?

JSON is a text format for exchanging structured data between systems.

### 2. Which Python module handles JSON?

The built-in `json` module.

### 3. How do you convert a Python object to a JSON string?

Use `json.dumps()`.

### 4. How do you convert a JSON string to Python?

Use `json.loads()`.

### 5. What is the difference between `dump()` and `dumps()`?

`dump()` writes to a file. `dumps()` returns a string.

### 6. What is the difference between `load()` and `loads()`?

`load()` reads from a file object. `loads()` reads from a string.

### 7. What does JSON object become in Python?

It becomes a dictionary.

### 8. What does JSON array become in Python?

It becomes a list.

### 9. What does JSON `null` become in Python?

It becomes `None`.

### 10. What do JSON `true` and `false` become?

They become `True` and `False`.

## Intermediate Level

### 11. How do you pretty print JSON?

Use `indent`.

```python
json.dumps(data, indent=2)
```

### 12. How do you sort JSON keys?

Use `sort_keys=True`.

### 13. How do you preserve non-ASCII characters?

Use `ensure_ascii=False`.

### 14. What exception is raised for invalid JSON?

`json.JSONDecodeError`.

### 15. Can JSON store Python sets?

Not directly. Convert sets to lists first.

### 16. Can JSON keys be integers?

JSON object keys are strings.

### 17. Why is JSON common in APIs?

It is language independent and easy to parse.

### 18. How do you validate required fields?

Parse JSON into a dictionary and check keys.

### 19. How do you read JSON from a file?

Use `json.load(file)`.

### 20. How do you write JSON to a file?

Use `json.dump(data, file)`.

## Advanced Level

### 21. What is serialization?

Serialization converts an in-memory object into a storable or transferable format.

### 22. What is deserialization?

Deserialization converts stored or transferred data back into an in-memory object.

### 23. Is JSON the same as a Python dictionary?

No. JSON is text; a dictionary is a Python object.

### 24. Why can `json.dumps()` raise `TypeError`?

Some Python objects, like sets or custom objects, are not JSON serializable by default.

### 25. How can you serialize a custom object?

Convert it to a dictionary first or provide a custom encoder.

### 26. Should JSON be used for secrets?

Not by itself. JSON is not encrypted.

### 27. How do you handle missing JSON fields?

Use `dict.get()` or validate before access.

### 28. What is a common API parsing mistake?

Using Python booleans inside raw JSON text instead of lowercase JSON booleans.

### 29. Why specify `encoding="utf-8"` when reading JSON files?

It makes text encoding explicit and portable.

### 30. What should you remember for interviews?

Know `dump`, `dumps`, `load`, `loads`, type mapping, invalid JSON handling, and serialization limits.

## See also

- [Python JSON: core concepts](core-concepts.md)
- [Python JSON reference](json-reference.md)
- [Python JSON interview problems](interview-problems.md)
