# Python Binary Types: Frequently Asked Interview Questions

This page collects frequently asked Python binary type interview questions for `bytes`, `bytearray`, and `memoryview` from **basic** to **pro** level.

## Basic Level

### 1. What are Python binary types?

Python binary types store raw byte data. Main types are `bytes`, `bytearray`, and `memoryview`.

```python
data = b"PDF"
```

### 2. What is `bytes`?

`bytes` is an immutable sequence of byte values.

```python
data = b"laptop"
```

### 3. What is `bytearray`?

`bytearray` is a mutable sequence of byte values.

```python
data = bytearray(b"laptop")
```

### 4. What is `memoryview`?

`memoryview` is a view into an existing bytes-like object without copying.

```python
view = memoryview(bytearray(b"image"))
```

### 5. What is the difference between `str` and `bytes`?

`str` is text. `bytes` is raw binary data.

```python
print(type("laptop"))
print(type(b"laptop"))
```

### 6. How do you create bytes literal?

Prefix a string literal with `b`.

```python
data = b"invoice"
```

### 7. Are `bytes` mutable?

No.

```python
data = b"abc"
# data[0] = 65  # TypeError
```

### 8. Is `bytearray` mutable?

Yes.

```python
data = bytearray(b"abc")
data[0] = 65
```

### 9. What does indexing bytes return?

It returns an integer from `0` to `255`.

```python
print(b"ABC"[0])
```

### 10. What does slicing bytes return?

It returns a new `bytes` object.

```python
print(b"ABCDEF"[0:3])
```

### 11. How do you convert text to bytes?

Use `encode()`.

```python
print("laptop".encode("utf-8"))
```

### 12. How do you convert bytes to text?

Use `decode()`.

```python
print(b"laptop".decode("utf-8"))
```

### 13. What encoding is commonly used?

UTF-8.

```python
data = "invoice".encode("utf-8")
```

### 14. What are byte values allowed range?

Each byte must be between `0` and `255`.

```python
print(bytes([65, 66, 67]))
```

### 15. What happens with bytes value above 255?

Python raises `ValueError`.

```python
# bytes([300])  # ValueError
```

## Intermediate Level

### 16. What is the difference between `encode()` and `decode()`?

`encode()` converts text to bytes. `decode()` converts bytes to text.

### 17. What happens when decoding with wrong encoding?

It may raise `UnicodeDecodeError` or produce incorrect text.

```python
# b"\xff".decode("utf-8")  # UnicodeDecodeError
```

### 18. How do you read a binary file?

Use `"rb"` mode.

```python
with open("invoice.pdf", "rb") as file:
    data = file.read()
```

### 19. How do you write a binary file?

Use `"wb"` mode.

```python
with open("export.bin", "wb") as file:
    file.write(b"data")
```

### 20. How do you check if bytes start with a prefix?

Use `startswith()`.

```python
print(b"%PDF-1.7".startswith(b"%PDF"))
```

### 21. How do you check if bytes end with a suffix?

Use `endswith()`.

```python
print(b"image.png".endswith(b".png"))
```

### 22. How do you search inside bytes?

Use `find()` or `in`.

```python
payload = b"product_id=101"
print(payload.find(b"101"))
print(b"product" in payload)
```

### 23. How do you replace bytes?

Use `replace()`.

```python
print(b"mouse mouse".replace(b"mouse", b"keyboard"))
```

### 24. Does `bytes.replace()` mutate original bytes?

No. It returns new bytes.

### 25. How do you modify binary data in place?

Use `bytearray`.

```python
data = bytearray(b"abc")
data[0] = ord("A")
```

### 26. How do you append one byte to `bytearray`?

Use `append()` with an integer byte value.

```python
data = bytearray(b"ABC")
data.append(10)
```

### 27. How do you append multiple bytes?

Use `extend()`.

```python
data = bytearray(b"ABC")
data.extend(b"DEF")
```

### 28. How do you convert bytes to hex?

Use `.hex()`.

```python
print(b"PDF".hex())
```

### 29. How do you convert hex to bytes?

Use `bytes.fromhex()`.

```python
print(bytes.fromhex("504446"))
```

### 30. How do you compare bytes?

Bytes compare lexicographically by byte values.

```python
print(b"ABC" < b"ABD")
```

## Advanced Level

### 31. Why use `memoryview`?

To avoid copying large binary buffers.

```python
data = bytearray(b"large-buffer")
view = memoryview(data)
```

### 32. Does slicing bytes copy data?

Yes, slicing `bytes` creates a new bytes object.

```python
chunk = b"abcdef"[0:3]
```

### 33. Does slicing a memoryview copy data?

No, it creates another view.

```python
view = memoryview(bytearray(b"abcdef"))
chunk = view[0:3]
```

### 34. How do you convert memoryview back to bytes?

Use `.tobytes()`.

```python
view = memoryview(b"abc")
print(view.tobytes())
```

### 35. Can memoryview modify original data?

Yes, if the underlying buffer is mutable.

```python
data = bytearray(b"abc")
view = memoryview(data)
view[0] = ord("A")
print(data)
```

### 36. Can memoryview modify `bytes`?

No, because `bytes` is immutable.

```python
view = memoryview(b"abc")
# view[0] = 65  # TypeError
```

### 37. What is a file signature?

Known starting bytes that identify file type.

```python
print(b"%PDF-1.7".startswith(b"%PDF"))
```

### 38. What are magic bytes?

Magic bytes are fixed byte patterns used to identify binary formats.

```python
png_magic = b"\x89PNG\r\n\x1a\n"
```

### 39. Why use binary mode for images/PDFs?

Text mode may decode or transform data; binary mode preserves exact bytes.

### 40. What is `UnicodeDecodeError`?

An error raised when bytes cannot be decoded with the chosen encoding.

### 41. How do you ignore decode errors?

Use `errors`, but be careful because data may be lost.

```python
text = b"\xff".decode("utf-8", errors="ignore")
```

### 42. How do you replace decode errors?

Use `errors="replace"`.

```python
text = b"\xff".decode("utf-8", errors="replace")
```

### 43. How do you handle binary API response?

Keep it as bytes for files; decode only if it is text.

### 44. How do you send binary data over network?

Usually as bytes, multipart upload, or encoded form such as base64 when text transport is required.

### 45. What is base64?

Base64 encodes binary data as ASCII text.

```python
import base64

encoded = base64.b64encode(b"invoice")
print(encoded)
```

## Pro Level

### 46. Why are bytes immutable?

Immutability makes bytes safe to share and usable as dictionary keys.

### 47. Can bytes be dictionary keys?

Yes, bytes are hashable.

```python
headers = {b"%PDF": "pdf"}
```

### 48. Can bytearray be dictionary keys?

No, bytearray is mutable and unhashable.

```python
# data = {bytearray(b"abc"): "value"}  # TypeError
```

### 49. Is memoryview hashable?

Some read-only memoryviews can be hashable, but do not rely on memoryview as a common dictionary key in interviews.

### 50. What is the buffer protocol?

A Python protocol that lets objects expose raw memory to other objects without copying.

### 51. Which objects support the buffer protocol?

Examples include `bytes`, `bytearray`, `array.array`, and many NumPy arrays.

### 52. Why is zero-copy important?

It reduces memory usage and improves performance for large binary data.

### 53. What is the difference between binary and text file modes?

Binary mode reads/writes bytes. Text mode reads/writes strings with encoding/decoding.

### 54. What is endianess?

Endianess describes byte order for multi-byte numbers.

```python
value = int.from_bytes(b"\x00\x10", byteorder="big")
print(value)
```

### 55. How do you convert int to bytes?

Use `int.to_bytes()`.

```python
print((16).to_bytes(2, byteorder="big"))
```

### 56. How do you convert bytes to int?

Use `int.from_bytes()`.

```python
print(int.from_bytes(b"\x00\x10", byteorder="big"))
```

### 57. What is a common mistake with bytes and strings?

Comparing `str` and `bytes` directly.

```python
print("PDF" == b"PDF")  # False
```

### 58. Why can binary data not always be decoded as UTF-8?

Many binary files contain byte sequences that are not valid UTF-8 text.

### 59. When should you choose `bytes` vs `bytearray`?

Use `bytes` for immutable data and `bytearray` when you need in-place mutation.

### 60. When should you choose `memoryview`?

Use `memoryview` when working with large buffers and you want slices/views without copying.

## Final Interview Checklist

- `str` is text; `bytes` is binary.
- `bytes` is immutable; `bytearray` is mutable.
- `bytes[index]` returns an integer.
- Use `encode()` for text to bytes.
- Use `decode()` for bytes to text.
- Use `"rb"` / `"wb"` for binary files.
- Use file signatures/magic bytes for file type checks.
- Use `memoryview` for zero-copy buffer access.
- Be careful with encodings and `UnicodeDecodeError`.
- Use `int.to_bytes()` and `int.from_bytes()` for numeric byte conversion.

## See also

- [Python binary core concepts](core-concepts.md)
- [Python binary operations](operations-and-methods.md)
- [Python binary interview problems](interview-problems.md)
- [Python strings FAQ](../strings/frequently-asked-questions.md)
