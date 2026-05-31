# Python Binary Operations & Methods: Interview Notes

Binary interview questions usually focus on encoding/decoding, immutability, file modes, byte values, mutation with `bytearray`, and avoiding copies with `memoryview`.

## Quick Method Table

| Operation / Method | Type | What it does | Interview use case |
|--------------------|------|--------------|--------------------|
| `encode()` | `str` | Text to bytes | API/file encoding |
| `decode()` | `bytes` | Bytes to text | Read response body |
| `bytes()` | built-in | Create bytes | Convert iterable |
| `bytearray()` | built-in | Create mutable bytes | Edit binary data |
| `.hex()` | bytes-like | Bytes to hex string | Debug/checksum display |
| `bytes.fromhex()` | `bytes` | Hex string to bytes | Parse hex input |
| `.startswith()` | bytes-like | Prefix check | File signature |
| `.find()` | bytes-like | Find byte sequence | Scan payload |
| `.replace()` | bytes-like | Replace bytes | Normalize payload |
| `memoryview()` | built-in | View buffer | Avoid copying |

## Encoding Text to Bytes

```python
product_name = "laptop"
data = product_name.encode("utf-8")

print(data)
# b"laptop"
```

### Interview Point

Always know the encoding. UTF-8 is the common default for modern text.

## Decoding Bytes to Text

```python
data = b"laptop"
text = data.decode("utf-8")

print(text)
```

### Interview Point

Decoding with the wrong encoding can raise `UnicodeDecodeError` or produce wrong text.

## Creating `bytes`

```python
print(bytes([80, 68, 70]))
# b"PDF"
```

Byte values must be between `0` and `255`.

```python
# bytes([300])  # ValueError
```

## Creating `bytearray`

```python
data = bytearray(b"image")
data[0] = ord("I")

print(data)
```

## Indexing Bytes

Indexing returns an integer.

```python
data = b"ABC"

print(data[0])  # 65
```

Slicing returns bytes.

```python
data = b"ABCDEF"

print(data[0:3])
# b"ABC"
```

## `.hex()`

Converts bytes to a hexadecimal string.

```python
data = b"PDF"

print(data.hex())
# 504446
```

## `bytes.fromhex()`

Converts hex string to bytes.

```python
data = bytes.fromhex("504446")

print(data)
# b"PDF"
```

## `.startswith()`

Useful for file signatures.

```python
header = b"%PDF-1.7"

print(header.startswith(b"%PDF"))
# True
```

## `.find()`

Finds a byte sequence.

```python
payload = b"product_id=101&status=paid"

print(payload.find(b"status"))
```

Returns `-1` if not found.

## `.replace()`

Returns new bytes for `bytes`; modifies nothing because bytes are immutable.

```python
payload = b"mouse mouse"
new_payload = payload.replace(b"mouse", b"keyboard")

print(new_payload)
```

## `bytearray.append()`

Adds one byte.

```python
data = bytearray(b"PDF")
data.append(10)

print(data)
```

## `bytearray.extend()`

Adds multiple bytes.

```python
data = bytearray(b"PDF")
data.extend(b"-DATA")

print(data)
```

## `memoryview()`

Creates a zero-copy view.

```python
data = bytearray(b"product-image")
view = memoryview(data)

print(view[0:7].tobytes())
```

### Interview Point

Slicing bytes copies data. Slicing a memoryview creates a view, which can avoid copying large buffers.

## Reading Binary Files

```python
with open("product-image.png", "rb") as file:
    header = file.read(8)

print(header)
```

## Writing Binary Files

```python
with open("export.bin", "wb") as file:
    file.write(b"catalog-data")
```

## Common Interview Questions

### What is the difference between `encode()` and `decode()`?

`encode()` converts text to bytes. `decode()` converts bytes to text.

### What does `bytes[0]` return?

An integer byte value between `0` and `255`.

### Why use binary file mode?

Binary mode avoids text encoding/line-ending transformations.

### Why use `memoryview`?

To work with large binary buffers without copying data.

## Practice Problems

1. Encode `"invoice"` to bytes.
2. Decode `b"invoice"` to string.
3. Convert `b"PDF"` to hex.
4. Convert `"504446"` back to bytes.
5. Check whether bytes start with `b"%PDF"`.
6. Modify a `bytearray` in place.
7. Use `memoryview` to slice binary data.

## See also

- [Python binary core concepts](core-concepts.md)
- [Python binary interview problems](interview-problems.md)
- [Python binary FAQ](frequently-asked-questions.md)
