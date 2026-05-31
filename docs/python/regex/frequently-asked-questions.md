# Python RegEx: Frequently Asked Interview Questions

## Basic Level

### 1. What is RegEx?

RegEx is a pattern language for matching text.

### 2. Which Python module supports RegEx?

The built-in `re` module.

### 3. Why use raw strings for regex?

Raw strings prevent Python from treating backslashes as escape characters before the regex engine sees them.

### 4. What does `\d` mean?

It matches a digit.

### 5. What does `\w` mean?

It matches a word character.

### 6. What does `\s` mean?

It matches whitespace.

### 7. What does `.` mean?

It matches any character except newline by default.

### 8. What does `+` mean?

One or more repetitions.

### 9. What does `*` mean?

Zero or more repetitions.

### 10. What does `?` mean?

Zero or one repetition.

## Intermediate Level

### 11. What is `re.search()`?

It finds the first match anywhere in the string.

### 12. What is `re.match()`?

It checks only from the start of the string.

### 13. What is `re.fullmatch()`?

It checks whether the whole string matches the pattern.

### 14. Which function is best for validation?

`re.fullmatch()` is usually best.

### 15. What is `re.findall()`?

It returns all non-overlapping matches as a list.

### 16. What is `re.finditer()`?

It returns match objects lazily as an iterator.

### 17. What is `re.sub()`?

It replaces matches with another string.

### 18. What is `re.split()`?

It splits text using a regex pattern.

### 19. What are regex groups?

Groups capture parts of a match using parentheses.

### 20. What are named groups?

Named groups capture values with readable names.

## Advanced Level

### 21. What is `re.compile()`?

It creates a reusable regex pattern object.

### 22. Why compile a pattern?

It improves readability and is useful when the same pattern is used many times.

### 23. What is greedy matching?

Greedy quantifiers match as much text as possible.

### 24. What is non-greedy matching?

Non-greedy quantifiers match as little as possible, such as `.*?`.

### 25. What does `^` mean?

It matches the start of a string, or line with `re.MULTILINE`.

### 26. What does `$` mean?

It matches the end of a string, or line with `re.MULTILINE`.

### 27. What is `re.IGNORECASE`?

A flag for case-insensitive matching.

### 28. What is `re.MULTILINE`?

A flag that makes `^` and `$` work per line.

### 29. What is a common regex interview mistake?

Using `search()` when full validation requires `fullmatch()`.

### 30. What should you remember for interviews?

Know `search`, `match`, `fullmatch`, `findall`, `finditer`, `sub`, groups, flags, and raw strings.

## See also

- [Python RegEx: core concepts](core-concepts.md)
- [Python RegEx reference](regex-reference.md)
- [Python RegEx interview problems](interview-problems.md)
