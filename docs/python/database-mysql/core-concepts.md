# Python MySQL CRUD Operations: Core Concepts

Python can work with MySQL databases using packages such as `mysql-connector-python` or `PyMySQL`.

This page covers:

- connecting Python to MySQL
- creating tables
- CRUD operations: create, read, update, delete
- parameterized queries
- transactions
- safe database practices

Examples use an online computer shopping system.

## What Is CRUD?

CRUD stands for:

| Letter | Operation | SQL example |
|--------|-----------|-------------|
| C | Create | `INSERT` |
| R | Read | `SELECT` |
| U | Update | `UPDATE` |
| D | Delete | `DELETE` |

In a shopping system, CRUD is used for products, customers, carts, orders, inventory, and payments.

## Install MySQL Connector

```bash
python -m pip install mysql-connector-python
```

Import it in Python:

```python
import mysql.connector
```

## Connect to MySQL

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

In real projects, do not hardcode credentials. Use environment variables or a secrets manager.

## Create Table

```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL
)
""")
```

## Create: Insert Product

Use parameterized queries instead of string formatting.

```python
query = """
INSERT INTO products (name, category, price, stock)
VALUES (%s, %s, %s, %s)
"""

values = ("Laptop", "computer", 999.99, 5)
cursor.execute(query, values)
connection.commit()
```

`commit()` saves the change permanently.

## Read: Select Products

```python
cursor.execute("SELECT id, name, price, stock FROM products")

for product_id, name, price, stock in cursor.fetchall():
    print(product_id, name, price, stock)
```

## Read One Product

```python
query = "SELECT id, name, price, stock FROM products WHERE id = %s"
cursor.execute(query, (101,))
product = cursor.fetchone()
```

The comma in `(101,)` makes it a one-item tuple.

## Update Product

```python
query = "UPDATE products SET price = %s WHERE id = %s"
cursor.execute(query, (899.99, 101))
connection.commit()
```

## Delete Product

```python
query = "DELETE FROM products WHERE id = %s"
cursor.execute(query, (101,))
connection.commit()
```

Use deletes carefully. Many real systems prefer soft delete with an `is_active` or `deleted_at` column.

## Parameterized Queries

Do this:

```python
cursor.execute("SELECT * FROM products WHERE name = %s", ("Laptop",))
```

Avoid this:

```python
name = "Laptop"
cursor.execute(f"SELECT * FROM products WHERE name = '{name}'")
```

Parameterized queries help prevent SQL injection.

## Transactions

A transaction groups multiple database changes.

Example: placing an order should insert the order and reduce inventory together.

```python
try:
    cursor.execute("INSERT INTO orders (customer_id, total) VALUES (%s, %s)", (7, 999.99))
    cursor.execute("UPDATE products SET stock = stock - 1 WHERE id = %s", (101,))
    connection.commit()
except Exception:
    connection.rollback()
    raise
```

Use `rollback()` when a multi-step operation fails.

## Closing Connection

```python
cursor.close()
connection.close()
```

Always close cursors and connections when done.

## Common Gotchas

### Forgetting `commit()`

`INSERT`, `UPDATE`, and `DELETE` usually need `connection.commit()`.

### SQL injection

Never build SQL by concatenating user input.

### Not handling transactions

Order placement and stock updates should succeed or fail together.

### Hardcoding credentials

Use environment variables in real applications.

## See also

- [MySQL CRUD reference](mysql-crud-reference.md)
- [MySQL CRUD interview problems](interview-problems.md)
- [MySQL CRUD FAQ](frequently-asked-questions.md)
- [REST API design](../rest-api-design/core-concepts.md)
- [Exception handling](../exception-handling/core-concepts.md)
