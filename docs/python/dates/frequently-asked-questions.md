# Python Dates: Frequently Asked Interview Questions

## Basic Level

### 1. Which module handles dates in Python?

The `datetime` module.

### 2. What is `date`?

It stores year, month, and day.

### 3. What is `datetime`?

It stores date and time together.

### 4. What is `time`?

It stores time of day.

### 5. What is `timedelta`?

It represents a duration.

### 6. How do you get today's date?

```python
from datetime import date
print(date.today())
```

### 7. How do you get current datetime?

```python
from datetime import datetime
print(datetime.now())
```

### 8. How do you create a date?

```python
from datetime import date
value = date(2026, 5, 31)
```

### 9. How do you add days?

```python
from datetime import timedelta
new_date = value + timedelta(days=7)
```

### 10. How do you subtract dates?

```python
days = (end - start).days
```

## Intermediate Level

### 11. What is `strftime()`?

Formats date/datetime to string.

### 12. What is `strptime()`?

Parses string to datetime.

### 13. What does `%Y-%m-%d` mean?

Four-digit year, month, day.

### 14. What is ISO format?

A standard date/time text format, available with `isoformat()`.

### 15. How do you parse ISO datetime?

Use `datetime.fromisoformat()`.

### 16. What is a naive datetime?

A datetime without timezone information.

### 17. What is an aware datetime?

A datetime with timezone information.

### 18. How do you get UTC now?

```python
from datetime import datetime, timezone
print(datetime.now(timezone.utc))
```

### 19. How do you compare dates?

Use comparison operators like `<`, `<=`, `>`, `>=`.

### 20. How do you sort by date?

Use `sorted(..., key=...)`.

## Advanced Level

### 21. Why store UTC in backend systems?

It avoids ambiguity across time zones.

### 22. What is a timezone bug?

Comparing or storing local times without knowing their timezone.

### 23. What is `weekday()`?

Returns Monday as `0` and Sunday as `6`.

### 24. How do you detect weekend?

```python
value.weekday() >= 5
```

### 25. How do you calculate subscription days left?

Subtract today from expiry date and clamp at zero.

### 26. What happens if date string format does not match `strptime`?

It raises `ValueError`.

### 27. Can you add an int directly to a date?

No. Use `timedelta`.

### 28. What is `timestamp()`?

Seconds since Unix epoch for a datetime.

### 29. What is Unix epoch?

1970-01-01 00:00:00 UTC.

### 30. What should you remember?

Use `timedelta` for durations, `strftime` to format, `strptime` to parse, and UTC-aware datetimes for backend timestamps.

## See also

- [Python dates core concepts](core-concepts.md)
- [Python dates reference](date-reference.md)
- [Python dates interview problems](interview-problems.md)
