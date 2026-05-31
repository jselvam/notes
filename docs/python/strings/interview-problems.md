# Python String Interview Problems

String interview problems usually test indexing, slicing, two pointers, hashing with dictionaries/sets, normalization, and immutability.

## Interview Pattern: When to Think About Strings

Use string techniques when the problem needs:

- character traversal
- substring checks
- reversal
- palindrome validation
- anagram/frequency counting
- parsing text
- case-insensitive comparison
- building output efficiently

## 1. Reverse a Product Name

### Problem

Reverse a string.

```python
name = "laptop"
```

### Python Solution

```python
def reverse_string(text):
    return text[::-1]


print(reverse_string("laptop"))
# potpal
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

## 2. Reverse String Without Slicing

### Problem

Reverse a string without using `[::-1]`.

### Python Solution

```python
def reverse_without_slicing(text):
    result = []

    for index in range(len(text) - 1, -1, -1):
        result.append(text[index])

    return "".join(result)


print(reverse_without_slicing("mouse"))
```

### Interview Point

Use a list + `join()` because repeated string concatenation is inefficient.

## 3. Check Palindrome

### Problem

Check whether a string reads the same forward and backward.

### Python Solution

```python
def is_palindrome(text):
    normalized = text.lower()
    return normalized == normalized[::-1]


print(is_palindrome("Level"))  # True
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

## 4. Valid Palindrome Ignoring Non-Alphanumeric

### Problem

Ignore spaces, punctuation, and case.

### Python Solution

```python
def is_clean_palindrome(text):
    cleaned = []

    for ch in text:
        if ch.isalnum():
            cleaned.append(ch.lower())

    normalized = "".join(cleaned)
    return normalized == normalized[::-1]


print(is_clean_palindrome("A man, a plan, a canal: Panama"))
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

## 5. Check Anagram

### Problem

Check whether two strings contain the same characters with the same counts.

### Python Solution

```python
def is_anagram(a, b):
    if len(a) != len(b):
        return False

    counts = {}

    for ch in a:
        counts[ch] = counts.get(ch, 0) + 1

    for ch in b:
        if ch not in counts:
            return False
        counts[ch] -= 1
        if counts[ch] == 0:
            del counts[ch]

    return not counts


print(is_anagram("listen", "silent"))
```

### Complexity

- Time: **O(n)**
- Space: **O(k)** unique characters

## 6. First Non-Repeating Character

### Problem

Return the first character that appears once.

### Python Solution

```python
def first_unique_character(text):
    counts = {}

    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1

    for ch in text:
        if counts[ch] == 1:
            return ch

    return None


print(first_unique_character("swiss"))  # w
```

### Complexity

- Time: **O(n)**
- Space: **O(k)**

## 7. Count Vowels

### Problem

Count vowels in a product description.

### Python Solution

```python
def count_vowels(text):
    vowels = {"a", "e", "i", "o", "u"}
    count = 0

    for ch in text.lower():
        if ch in vowels:
            count += 1

    return count


print(count_vowels("wireless mouse"))
```

### Complexity

- Time: **O(n)**
- Space: **O(1)**

## 8. Remove Duplicate Characters Preserve Order

### Problem

Remove repeated characters while preserving first occurrence order.

### Python Solution

```python
def remove_duplicate_chars(text):
    seen = set()
    result = []

    for ch in text:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)

    return "".join(result)


print(remove_duplicate_chars("keyboard"))
```

### Complexity

- Time: **O(n)**
- Space: **O(k)**

## 9. Longest Word in Search Query

### Problem

Find the longest word in a search query.

### Python Solution

```python
def longest_word(query):
    words = query.split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


print(longest_word("wireless ergonomic keyboard"))
```

### Complexity

- Time: **O(n)**
- Space: **O(w)** words

## 10. Compress Repeated Characters

### Problem

Compress `"aaabbc"` into `"a3b2c1"`.

### Python Solution

```python
def compress_string(text):
    if not text:
        return ""

    result = []
    count = 1

    for index in range(1, len(text)):
        if text[index] == text[index - 1]:
            count += 1
        else:
            result.append(text[index - 1] + str(count))
            count = 1

    result.append(text[-1] + str(count))

    return "".join(result)


print(compress_string("aaabbc"))
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

## Summary: String Patterns to Remember

| Pattern | String idea | Example |
|---------|-------------|---------|
| Slicing | `[::-1]` | reverse/palindrome |
| Two pointers | left/right chars | palindrome |
| Hash map | char counts | anagram |
| Set | seen chars | remove duplicates |
| Parsing | `split()` | search query |
| Building | list + `join()` | compression |
| Normalization | `strip()`, `lower()` | input compare |

## See also

- [Python strings: core concepts](core-concepts.md)
- [Python string methods](methods.md)
- [Python string FAQ](frequently-asked-questions.md)
- [Python set interview problems](../set/interview-problems.md)
