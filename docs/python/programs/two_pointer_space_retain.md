## Problem

Reverse the characters in a string **without changing the positions of spaces**.

### Example

Input:

```python
"ab cd ef"
```

Output:

```python
"fe dc ba"
```

Notice:

* Spaces stay in the same index positions.
* Only characters are reversed.

---

# Python Program

```python
text = "ab cd ef"

# Convert string to list because strings are immutable
chars = list(text)

left = 0
right = len(chars) - 1

while left < right:

    # Skip spaces from left side
    if chars[left] == ' ':
        left += 1

    # Skip spaces from right side
    elif chars[right] == ' ':
        right -= 1

    else:
        # Swap characters
        chars[left], chars[right] = chars[right], chars[left]

        left += 1
        right -= 1

result = ''.join(chars)

print(result)
```

Output:

```python
fe dc ba
```

---

# Step-by-step Logic

For:

```python
"ab cd ef"
```

Character positions:

```python
a b _ c d _ e f
```

(`_` means space)

We:

1. Use two pointers:

   * `left` → start
   * `right` → end
2. Ignore spaces
3. Swap only characters
4. Keep moving inward

---

# Real-life Analogy

Imagine people standing in a queue with empty chairs between them.

Example:

```text
A B _ C D _ E F
```

People reverse positions:

```text
F E _ D C _ B A
```

But chairs (spaces) never move.

---

# Another Example

Input:

```python
"i love python"
```

Output:

```python
"n ohtypevoli"
```

Space positions remain same.

---

# Interview Points

This problem tests:

* Two pointer technique
* String manipulation
* Understanding immutable strings
* Edge case handling

---

# Time Complexity

* O(n)

# Space Complexity

* O(n) (because of list conversion)
