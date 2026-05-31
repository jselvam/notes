# Python Date Reference: Interview Notes

## Quick Table

| Task | Code |
|------|------|
| Today | `date.today()` |
| Current datetime | `datetime.now()` |
| UTC now | `datetime.now(timezone.utc)` |
| Add days | `dt + timedelta(days=7)` |
| Difference | `(end - start).days` |
| Format | `dt.strftime("%Y-%m-%d")` |
| Parse | `datetime.strptime(text, "%Y-%m-%d")` |
| ISO string | `dt.isoformat()` |

## Imports

```python
from datetime import date, datetime, timedelta, timezone
```

## Date Formats

| Format | Meaning | Example |
|--------|---------|---------|
| `%Y` | 4-digit year | `2026` |
| `%m` | month | `05` |
| `%d` | day | `31` |
| `%H` | hour 24h | `14` |
| `%M` | minute | `30` |
| `%S` | second | `59` |

```python
from datetime import datetime

dt = datetime(2026, 5, 31, 14, 30)
print(dt.strftime("%Y-%m-%d %H:%M"))
```

## Coupon Expiry Check

```python
from datetime import date

expiry = date(2026, 6, 30)
today = date.today()

print(today <= expiry)
```

## Delivery Estimate

```python
from datetime import date, timedelta

delivery = date.today() + timedelta(days=5)
print(delivery)
```

## Timezone-Aware Datetime

```python
from datetime import datetime, timezone

created_at = datetime.now(timezone.utc)
print(created_at)
```

## Common Interview Questions

### What is naive datetime?

A datetime without timezone info.

### What is aware datetime?

A datetime with timezone info.

### Which is safer for backend systems?

Use timezone-aware datetimes, often UTC.

## See also

- [Python dates core concepts](core-concepts.md)
- [Python dates interview problems](interview-problems.md)
- [Python dates FAQ](frequently-asked-questions.md)
