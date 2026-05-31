# Python Binary Types: `bytes`, `bytearray`, and `memoryview`

Python binary types store raw bytes instead of text characters. They are important for files, network responses, images, PDFs, uploads, encryption, compression, and low-level performance questions.

In an online computer shopping management system, binary data can appear in:

- uploaded product images
- PDF invoices
- office-suite license files
- exported reports
- compressed catalog feeds
- API responses from payment/shipping services
- encrypted tokens or signatures

## Overview

Python has three main binary sequence types:

| Type | Mutable? | Main use |
|------|----------|----------|
| `bytes` | No | Immutable binary data |
| `bytearray` | Yes | Editable binary data |
| `memoryview` | View | Zero-copy access to binary buffers |

## `bytes`

`bytes` is an immutable sequence of integers from `0` to `255`.

```python
data = b"PDF"

print(data)
print(type(data))
print(data[0])  # 80, ASCII code for P
```

### Common use cases

```python
invoice_header = b"%PDF"
image_header = b"\x89PNG"
```

Use `bytes` when binary data should not be changed.

## `bytearray`

`bytearray` is a mutable sequence of bytes.

```python
data = bytearray(b"cart")
data[0] = ord("p")

print(data)
# bytearray(b"part")
```

Use `bytearray` when you need to modify binary data in place.

## `memoryview`

`memoryview` gives a view into an existing bytes-like object without copying data.

```python
data = bytearray(b"product-image")
view = memoryview(data)

print(view[0])
```

Use `memoryview` for performance-sensitive slicing or binary processing.

## Text vs Binary

Text (`str`) and binary (`bytes`) are different.

```python
text = "laptop"
binary = b"laptop"

print(type(text))    # <class 'str'>
print(type(binary))  # <class 'bytes'>
```

Convert text to bytes using **encoding**.

```python
text = "laptop"
data = text.encode("utf-8")

print(data)
```

Convert bytes to text using **decoding**.

```python
data = b"laptop"
text = data.decode("utf-8")

print(text)
```

## Creating Binary Data

```python
data1 = b"invoice"
data2 = bytes("invoice", "utf-8")
data3 = bytes([80, 68, 70])
data4 = bytearray(b"invoice")
```

## Byte Values

Each byte is an integer between `0` and `255`.

```python
data = b"ABC"

print(data[0])  # 65
print(data[1])  # 66
print(data[2])  # 67
```

## Immutability vs Mutability

`bytes` cannot be changed.

```python
data = b"mouse"

# data[0] = 77  # TypeError
```

`bytearray` can be changed.

```python
data = bytearray(b"mouse")
data[0] = ord("M")

print(data)
```

## Binary File Reading

Use `"rb"` to read binary files.

```python
with open("invoice.pdf", "rb") as file:
    header = file.read(4)

print(header)
```

Use `"wb"` to write binary files.

```python
with open("copy.bin", "wb") as file:
    file.write(b"binary-data")
```

## Common Interview Points

### What is the difference between `str` and `bytes`?

`str` is text. `bytes` is raw binary data.

### What is the difference between `bytes` and `bytearray`?

`bytes` is immutable. `bytearray` is mutable.

### Why use `memoryview`?

Use `memoryview` to avoid copying large binary data when slicing or sharing buffers.

## Practice Problems

1. Encode a product name into UTF-8 bytes.
2. Decode bytes back into text.
3. Check whether a file starts with PDF header `b"%PDF"`.
4. Modify a `bytearray` in place.
5. Read the first 8 bytes of an uploaded image.
6. Use `memoryview` to inspect part of a large buffer.
7. Explain why `bytes[0]` returns an integer.

## See also

- [Python binary operations](operations-and-methods.md)
- [Python binary interview problems](interview-problems.md)
- [Python binary FAQ](frequently-asked-questions.md)
- [Python strings: core concepts](../strings/core-concepts.md)
