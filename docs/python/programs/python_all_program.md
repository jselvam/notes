## 1. Reverse String Without Built-in Methods

```python
text = "Python"

reversed_text = ""

for ch in text:
    reversed_text = ch + reversed_text

print(reversed_text)
```

### Output

```python
nohtyP
```

### How it works

Suppose:

```python
text = "ABC"
```

Step-by-step:

| Character | reversed_text |
| --------- | ------------- |
| A         | A             |
| B         | BA            |
| C         | CBA           |

We keep adding the new character at the beginning.

---

# Another Without Built-in (Two Pointer Technique)

```python
text = "Python"

left = 0
right = len(text) - 1

chars = list(text)

while left < right:
    temp = chars[left]
    chars[left] = chars[right]
    chars[right] = temp

    left += 1
    right -= 1

reversed_text = ""

for ch in chars:
    reversed_text += ch

print(reversed_text)
```

### Real-world analogy

Like swapping first and last books on a shelf repeatedly:

```text
P y t h o n
^         ^
swap
```

then move inward.

---

# 2. Reverse String With Built-in

## Using slicing

```python
text = "Python"

print(text[::-1])
```

### Output

```python
nohtyP
```

`[::-1]` means:

```python
[start : end : step]
```

Here step is `-1`, so Python moves backward.

---

# 3. Using reversed() built-in

```python
text = "Python"

result = "".join(reversed(text))

print(result)
```

### Output

```python
nohtyP
```

`reversed(text)` gives characters in reverse order, and `"".join()` combines them into a string.

---

# Interview Comparison

| Method           | Built-in? | Interview Friendly? | Time Complexity |
| ---------------- | --------- | ------------------- | --------------- |
| Loop prepend     | No        | Yes                 | O(n²)           |
| Two pointer      | No        | Very Good           | O(n)            |
| Slicing `[::-1]` | Yes       | Most common         | O(n)            |
| `reversed()`     | Yes       | Good                | O(n)            |

---

# Best answer in interviews

If interviewer says:

* **"Without built-in"** → Use **Two Pointer**
* **"Any method"** → Use `[::-1]`
