# Python Dates Interview Problems

## 1. Add Delivery Days

```python
from datetime import date, timedelta


def delivery_date(order_date, days):
    return order_date + timedelta(days=days)


print(delivery_date(date(2026, 5, 31), 5))
```

## 2. Check Coupon Expiry

```python
from datetime import date


def is_coupon_valid(today, expiry_date):
    return today <= expiry_date


print(is_coupon_valid(date(2026, 5, 31), date(2026, 6, 1)))
```

## 3. Days Between Order and Delivery

```python
from datetime import date


def days_between(start, end):
    return (end - start).days


print(days_between(date(2026, 5, 1), date(2026, 5, 31)))
```

## 4. Parse Order Date

```python
from datetime import datetime


def parse_order_date(text):
    return datetime.strptime(text, "%Y-%m-%d").date()


print(parse_order_date("2026-05-31"))
```

## 5. Format Invoice Date

```python
from datetime import date


def invoice_date_text(value):
    return value.strftime("%d/%m/%Y")


print(invoice_date_text(date(2026, 5, 31)))
```

## 6. Subscription Remaining Days

```python
from datetime import date


def remaining_days(today, expiry):
    return max((expiry - today).days, 0)


print(remaining_days(date(2026, 5, 31), date(2026, 6, 10)))
```

## 7. Create UTC Timestamp

```python
from datetime import datetime, timezone


def utc_timestamp():
    return datetime.now(timezone.utc).isoformat()


print(utc_timestamp())
```

## 8. Filter Orders by Date Range

```python
from datetime import date


def orders_in_range(orders, start, end):
    return [order for order in orders if start <= order["date"] <= end]


orders = [
    {"id": 1, "date": date(2026, 5, 1)},
    {"id": 2, "date": date(2026, 6, 1)},
]

print(orders_in_range(orders, date(2026, 5, 1), date(2026, 5, 31)))
```

## 9. Is Weekend Delivery

```python
from datetime import date


def is_weekend(value):
    return value.weekday() >= 5


print(is_weekend(date(2026, 5, 31)))
```

## 10. Sort Orders by Created Date

```python
def sort_orders_by_date(orders):
    return sorted(orders, key=lambda order: order["created_at"])
```

## Summary

| Pattern | Date idea |
|---------|-----------|
| Add duration | `timedelta` |
| Compare dates | `<=`, `>=` |
| Format output | `strftime()` |
| Parse input | `strptime()` |
| Store timestamps | UTC aware `datetime` |

## See also

- [Python dates core concepts](core-concepts.md)
- [Python dates reference](date-reference.md)
- [Python dates FAQ](frequently-asked-questions.md)
