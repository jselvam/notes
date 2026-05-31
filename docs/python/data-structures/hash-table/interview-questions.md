# Hash Table: 10 Interview Questions

## 1. What is a hash table?

A hash table is a data structure that stores key-value pairs and supports fast average lookup, insert, and delete operations.

## 2. Which Python data structures use hash tables?

Python `dict` and `set` are hash-table based.

## 3. What is a hash function?

A hash function converts a key into a numeric hash value that helps locate where the value is stored.

## 4. What is the average time complexity of dictionary lookup?

Dictionary lookup is average `O(1)`.

## 5. What is a collision?

A collision happens when two different keys map to the same internal bucket or position.

## 6. What types can be dictionary keys?

Dictionary keys must be hashable, such as strings, numbers, booleans, or tuples containing only hashable values.

## 7. Why cannot a list be a dictionary key?

A list is mutable and unhashable. If it changed after hashing, the dictionary could not reliably find it.

## 8. What is the difference between `dict` and `set`?

A `dict` stores key-value pairs. A `set` stores unique hashable values without associated values.

## 9. What is the difference between `dict[key]` and `dict.get(key)`?

`dict[key]` raises `KeyError` if the key is missing. `dict.get(key)` returns `None` or a default value.

## 10. When should you use a hash table in interviews?

Use a hash table when you need fast lookup, membership checks, grouping, mapping, caching, or indexing by key.

## See also

- [Core concepts](core-concepts.md)
- [Interview problems](interview-problems.md)
