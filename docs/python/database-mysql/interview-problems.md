# Python MySQL CRUD Interview Problems

## 1. Connect Python to MySQL

### Problem

Create a MySQL connection for a computer shopping database.

```python
import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="computer_shop",
)

cursor = connection.cursor(dictionary=True)
```

### Interview Point

In real projects, keep credentials in environment variables.

## 2. Create Products Table

```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sku VARCHAR(30) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL
)
""")
```

## 3. Insert Product

```python
def create_product(cursor, connection, sku, name, price, stock):
    query = """
    INSERT INTO products (sku, name, price, stock)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (sku, name, price, stock))
    connection.commit()
```

Use parameterized queries to avoid SQL injection.

## 4. Read Product by SKU

```python
def get_product_by_sku(cursor, sku):
    query = "SELECT id, sku, name, price, stock FROM products WHERE sku = %s"
    cursor.execute(query, (sku,))
    return cursor.fetchone()
```

## 5. List Products With Pagination

```python
def list_products(cursor, limit, offset):
    query = "SELECT id, sku, name, price FROM products LIMIT %s OFFSET %s"
    cursor.execute(query, (limit, offset))
    return cursor.fetchall()
```

Pagination avoids loading too many rows.

## 6. Update Product Price

```python
def update_product_price(cursor, connection, sku, price):
    query = "UPDATE products SET price = %s WHERE sku = %s"
    cursor.execute(query, (price, sku))
    connection.commit()
    return cursor.rowcount
```

`rowcount` can help detect whether a row was updated.

## 7. Delete Product

```python
def delete_product(cursor, connection, sku):
    query = "DELETE FROM products WHERE sku = %s"
    cursor.execute(query, (sku,))
    connection.commit()
    return cursor.rowcount
```

Discuss soft delete in interviews when data history matters.

## 8. Reduce Stock Safely

```python
def reduce_stock(cursor, connection, sku, quantity):
    query = """
    UPDATE products
    SET stock = stock - %s
    WHERE sku = %s AND stock >= %s
    """
    cursor.execute(query, (quantity, sku, quantity))
    connection.commit()
    return cursor.rowcount == 1
```

The `stock >= %s` condition prevents negative stock.

## 9. Place Order With Transaction

```python
def place_order(cursor, connection, customer_id, sku, quantity, total):
    try:
        cursor.execute(
            "INSERT INTO orders (customer_id, total) VALUES (%s, %s)",
            (customer_id, total),
        )
        cursor.execute(
            """
            UPDATE products
            SET stock = stock - %s
            WHERE sku = %s AND stock >= %s
            """,
            (quantity, sku, quantity),
        )
        if cursor.rowcount != 1:
            raise ValueError("Insufficient stock")
        connection.commit()
    except Exception:
        connection.rollback()
        raise
```

Order creation and stock update must succeed or fail together.

## 10. Prevent SQL Injection

Bad:

```python
query = f"SELECT * FROM products WHERE sku = '{sku}'"
```

Good:

```python
cursor.execute("SELECT * FROM products WHERE sku = %s", (sku,))
```

## 11. Handle Duplicate SKU

```python
import mysql.connector


try:
    create_product(cursor, connection, "LAP-101", "Laptop", 999.99, 5)
except mysql.connector.IntegrityError:
    print("SKU already exists")
```

## 12. Close Database Resources

```python
try:
    cursor.execute("SELECT 1")
finally:
    cursor.close()
    connection.close()
```

## Summary

CRUD interviews focus on safe SQL, parameterized queries, transactions, error handling, and knowing when to commit or roll back.

## See also

- [Python MySQL CRUD: core concepts](core-concepts.md)
- [MySQL CRUD reference](mysql-crud-reference.md)
- [MySQL CRUD FAQ](frequently-asked-questions.md)
