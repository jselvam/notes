# Python Binary Interview Problems

Binary interview problems test whether you understand bytes vs text, mutability, file signatures, encoding/decoding, and memory-efficient processing.

## Interview Pattern: When to Think About Binary Types

Use binary types when the problem involves:

- file uploads
- images, PDFs, ZIPs, or binary headers
- network payloads
- encryption/compression
- byte-level mutation
- zero-copy slicing
- encoding and decoding text

## 1. Encode Product Name to Bytes

### Problem

Convert a product name string into UTF-8 bytes.

### Python Solution

```python
def encode_product_name(name):
    return name.encode("utf-8")


print(encode_product_name("laptop"))
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

## 2. Decode Bytes to Text

### Problem

Convert API response bytes into text.

### Python Solution

```python
def decode_response(data):
    return data.decode("utf-8")


print(decode_response(b"order-paid"))
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

## 3. Check PDF File Signature

### Problem

Check whether uploaded file bytes look like a PDF.

### Python Solution

```python
def is_pdf(data):
    return data.startswith(b"%PDF")


print(is_pdf(b"%PDF-1.7..."))
print(is_pdf(b"PNG..."))
```

### Complexity

- Time: **O(1)** for fixed signature length
- Space: **O(1)**

## 4. Check PNG File Signature

### Problem

Check whether uploaded image bytes look like a PNG.

### Python Solution

```python
def is_png(data):
    return data.startswith(b"\x89PNG\r\n\x1a\n")


print(is_png(b"\x89PNG\r\n\x1a\n..."))
```

### Interview Point

Many file formats start with known magic bytes.

## 5. Redact Token in Binary Payload

### Problem

Replace a token inside bytes.

### Python Solution

```python
def redact_token(payload):
    return payload.replace(b"secret-token", b"[redacted]")


print(redact_token(b"user=101&token=secret-token"))
```

### Complexity

- Time: **O(n)**
- Space: **O(n)** because bytes are immutable

## 6. Mutate Binary Buffer In Place

### Problem

Change a mutable binary buffer.

### Python Solution

```python
def uppercase_first_byte(data):
    if data:
        data[0] = ord(chr(data[0]).upper())
    return data


print(uppercase_first_byte(bytearray(b"pdf")))
```

### Complexity

- Time: **O(1)**
- Space: **O(1)**

## 7. Convert Bytes to Hex for Debugging

### Problem

Display binary data as a hex string.

### Python Solution

```python
def to_hex(data):
    return data.hex()


print(to_hex(b"PDF"))
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

## 8. Convert Hex Back to Bytes

### Problem

Parse a hex string into bytes.

### Python Solution

```python
def from_hex(hex_text):
    return bytes.fromhex(hex_text)


print(from_hex("504446"))
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

## 9. Find Marker in Binary Payload

### Problem

Find the index of a marker in bytes.

### Python Solution

```python
def find_marker(payload, marker):
    return payload.find(marker)


print(find_marker(b"header|payload|footer", b"payload"))
```

### Complexity

- Time: **O(n * m)** conceptual worst case
- Space: **O(1)**

## 10. Slice Large Buffer With `memoryview`

### Problem

Read part of a large binary buffer without copying.

### Python Solution

```python
def first_chunk_view(data, size):
    view = memoryview(data)
    return view[:size]


buffer = bytearray(b"large-product-image-data")
chunk = first_chunk_view(buffer, 5)

print(chunk.tobytes())
```

### Complexity

- Time: **O(1)** to create the view
- Space: **O(1)** for the view

## Summary: Binary Patterns to Remember

| Pattern | Binary idea | Example |
|---------|-------------|---------|
| Text to binary | `encode()` | product name to bytes |
| Binary to text | `decode()` | API response body |
| File detection | `startswith()` | PDF/PNG signature |
| Byte mutation | `bytearray` | edit buffer |
| Debug display | `.hex()` | show binary content |
| Parse hex | `bytes.fromhex()` | convert hex input |
| Search payload | `.find()` | marker lookup |
| Zero-copy slice | `memoryview` | large buffer chunk |

## See also

- [Python binary core concepts](core-concepts.md)
- [Python binary operations](operations-and-methods.md)
- [Python binary FAQ](frequently-asked-questions.md)
- [Python strings: core concepts](../strings/core-concepts.md)
