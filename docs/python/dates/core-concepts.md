# Python Dates & Times: Core Concepts

Python date/time work is mostly done with the `datetime` module.

In an online computer shopping system, dates are used for:

- order created time
- delivery date
- subscription expiry
- coupon validity
- refund windows
- report ranges

## Important Classes

```python
from datetime import date, time, datetime, timedelta
```

| Class | Use |
|-------|-----|
| `date` | Year, month, day |
| `time` | Hour, minute, second |
| `datetime` | Date + time |
| `timedelta` | Duration/difference |
| `timezone` | Time zone offset |

## Current Date and Time

```python
from datetime import date, datetime

print(date.today())
print(datetime.now())
```

## Creating Dates

```python
from datetime import date, datetime

order_date = date(2026, 5, 31)
created_at = datetime(2026, 5, 31, 10, 30)

print(order_date)
print(created_at)
```

## Date Arithmetic

```python
from datetime import date, timedelta

order_date = date(2026, 5, 31)
delivery_date = order_date + timedelta(days=5)

print(delivery_date)
```

## Difference Between Dates

```python
from datetime import date

start = date(2026, 5, 1)
end = date(2026, 5, 31)

days = (end - start).days
print(days)
```

## Formatting Dates

Use `strftime()` to convert date/time to string.

```python
from datetime import datetime

created_at = datetime(2026, 5, 31, 10, 30)

print(created_at.strftime("%Y-%m-%d"))
print(created_at.strftime("%d/%m/%Y %H:%M"))
```

## Parsing Dates

Use `strptime()` to convert string to date/time.

```python
from datetime import datetime

text = "2026-05-31"
parsed = datetime.strptime(text, "%Y-%m-%d")

print(parsed)
```

## ISO Format

```python
from datetime import datetime

now = datetime.now()
text = now.isoformat()

print(text)
print(datetime.fromisoformat(text))
```

## Timezone Basics

Prefer timezone-aware datetimes for real systems.

```python
from datetime import datetime, timezone

now_utc = datetime.now(timezone.utc)
print(now_utc)
```

## Common Interview Points

### What is the difference between `date` and `datetime`?

`date` has only year/month/day. `datetime` has date plus time.

### What is `timedelta`?

A duration used for adding, subtracting, and comparing dates/times.

### What is the difference between `strftime` and `strptime`?

`strftime` formats date to string. `strptime` parses string to datetime.

## Practice Problems

1. Add 7 days to an order date.
2. Check if a coupon expired.
3. Parse `"2026-05-31"` into a datetime.
4. Format an order date as `DD/MM/YYYY`.
5. Calculate days between order and delivery.
6. Create a UTC timestamp.

## See also

- [Python dates reference](date-reference.md)
- [Python dates interview problems](interview-problems.md)
- [Python dates FAQ](frequently-asked-questions.md)
