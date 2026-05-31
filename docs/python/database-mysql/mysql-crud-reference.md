# Python MySQL CRUD Reference

## Quick Reference

| Task | SQL | Python method |
|------|-----|---------------|
| create table | `CREATE TABLE` | `cursor.execute()` |
| insert row | `INSERT` | `execute()` + `commit()` |
| read rows | `SELECT` | `fetchone()`, `fetchall()` |
| update row | `UPDATE` | `execute()` + `commit()` |
| delete row | `DELETE` | `execute()` + `commit()` |
| undo failed transaction | `ROLLBACK` | `connection.rollback()` |

## Connection Pattern

```python
import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="computer_shop",
)

cursor = connection.cursor()
```

## Dictionary Cursor

A dictionary cursor returns rows as dictionaries.

```python
cursor = connection.cursor(dictionary=True)
cursor.execute("SELECT id, name, price FROM products")
products = cursor.fetchall()
```

Example row:

```python
{"id": 101, "name": "Laptop", "price": 999.99}
```

## Create Table

```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sku VARCHAR(30) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
```

## Insert One Row

```python
query = """
INSERT INTO products (sku, name, price, stock)
VALUES (%s, %s, %s, %s)
"""

cursor.execute(query, ("LAP-101", "Laptop", 999.99, 5))
connection.commit()
```

## Insert Many Rows

```python
query = """
INSERT INTO products (sku, name, price, stock)
VALUES (%s, %s, %s, %s)
"""

rows = [
    ("LAP-101", "Laptop", 999.99, 5),
    ("MOU-201", "Mouse", 25.50, 30),
]

cursor.executemany(query, rows)
connection.commit()
```

## Select Rows

```python
cursor.execute("SELECT id, sku, name, price, stock FROM products")
rows = cursor.fetchall()
```

## Select With Filter

```python
query = "SELECT id, name, price FROM products WHERE category = %s"
cursor.execute(query, ("computer",))
rows = cursor.fetchall()
```

## Update Row

```python
query = "UPDATE products SET stock = %s WHERE sku = %s"
cursor.execute(query, (10, "LAP-101"))
connection.commit()
```

## Delete Row

```python
query = "DELETE FROM products WHERE sku = %s"
cursor.execute(query, ("MOU-201",))
connection.commit()
```

## Soft Delete

Soft delete keeps the row but marks it inactive.

```python
query = "UPDATE products SET is_active = FALSE WHERE sku = %s"
cursor.execute(query, ("MOU-201",))
connection.commit()
```

## Transaction Pattern

```python
try:
    cursor.execute(
        "INSERT INTO orders (customer_id, total) VALUES (%s, %s)",
        (7, 1025.49),
    )
    cursor.execute(
        "UPDATE products SET stock = stock - %s WHERE sku = %s",
        (1, "LAP-101"),
    )
    connection.commit()
except Exception:
    connection.rollback()
    raise
```

## Parameterized Query Pattern

| Connector | Placeholder style |
|-----------|-------------------|
| `mysql-connector-python` | `%s` |
| `PyMySQL` | `%s` |
| SQLite `sqlite3` | `?` |

For MySQL connector, use `%s` even for numbers.

## Common Exceptions

| Exception | Meaning |
|-----------|---------|
| `mysql.connector.Error` | base connector database error |
| `IntegrityError` | duplicate key or foreign key violation |
| `ProgrammingError` | invalid SQL or wrong database usage |
| `OperationalError` | connection or server problem |

## Best Practices

- Use parameterized queries.
- Use transactions for multi-step writes.
- Commit only after successful writes.
- Roll back on errors.
- Close cursors and connections.
- Store credentials outside source code.
- Validate user input before database writes.
- Use indexes on commonly filtered columns.
- Prefer connection pooling in web apps.

## See also

- [Python MySQL CRUD: core concepts](core-concepts.md)
- [MySQL CRUD interview problems](interview-problems.md)
- [MySQL CRUD FAQ](frequently-asked-questions.md)
