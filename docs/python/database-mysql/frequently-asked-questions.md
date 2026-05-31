# Python MySQL CRUD: Frequently Asked Interview Questions

## Basic Level

### 1. What is CRUD?

CRUD means Create, Read, Update, and Delete.

### 2. Which SQL command creates data?

`INSERT`.

### 3. Which SQL command reads data?

`SELECT`.

### 4. Which SQL command updates data?

`UPDATE`.

### 5. Which SQL command deletes data?

`DELETE`.

### 6. Which Python package can connect to MySQL?

`mysql-connector-python` is a common choice.

### 7. How do you install MySQL connector?

```bash
python -m pip install mysql-connector-python
```

### 8. What is a cursor?

A cursor is an object used to execute SQL statements and fetch results.

### 9. What does `commit()` do?

`commit()` permanently saves changes made by `INSERT`, `UPDATE`, or `DELETE`.

### 10. What does `rollback()` do?

`rollback()` undoes uncommitted changes in the current transaction.

## Intermediate Level

### 11. What is a parameterized query?

A parameterized query separates SQL from input values.

### 12. Why use parameterized queries?

They help prevent SQL injection and handle values safely.

### 13. What placeholder does MySQL connector use?

It uses `%s` placeholders.

### 14. Why does a one-value tuple need a comma?

`(sku,)` is a tuple. `(sku)` is just the value inside parentheses.

### 15. What is `fetchone()`?

It returns one row from the result set.

### 16. What is `fetchall()`?

It returns all remaining rows from the result set.

### 17. What is a dictionary cursor?

A dictionary cursor returns rows as dictionaries instead of tuples.

### 18. What is `executemany()`?

It executes the same SQL statement for multiple rows.

### 19. What is `rowcount`?

`rowcount` tells how many rows were affected by the last operation.

### 20. Why use pagination in `SELECT` queries?

Pagination avoids loading too many rows at once.

## Advanced Level

### 21. What is SQL injection?

SQL injection happens when unsafe user input changes the meaning of a SQL query.

### 22. Give a SQL injection prevention rule.

Never concatenate user input into SQL. Use parameters.

### 23. What is a transaction?

A transaction is a group of database operations that succeed or fail together.

### 24. Why use transactions for order placement?

The order insert and stock update must stay consistent.

### 25. What happens if one step in a transaction fails?

Use `rollback()` to undo previous uncommitted steps.

### 26. What is an `IntegrityError`?

It happens for constraint failures such as duplicate unique keys or foreign key violations.

### 27. What is a foreign key?

A foreign key links one table to another table's primary key.

### 28. What is a primary key?

A primary key uniquely identifies each row in a table.

### 29. What is a unique constraint?

A unique constraint prevents duplicate values in a column or column group.

### 30. What is soft delete?

Soft delete marks a row inactive instead of physically deleting it.

## Pro Level

### 31. Why avoid hardcoded database credentials?

Hardcoded credentials can leak secrets and make deployments harder.

### 32. Where should credentials be stored?

Use environment variables, secret managers, or deployment configuration.

### 33. What is connection pooling?

Connection pooling reuses database connections instead of opening a new connection for every request.

### 34. Why is connection pooling useful in web apps?

It reduces connection overhead and improves performance under load.

### 35. How do you prevent negative stock?

Use an atomic SQL update with a condition such as `WHERE stock >= quantity`.

### 36. Why check `rowcount` after stock update?

It tells whether the conditional update actually succeeded.

### 37. What is an index?

An index helps the database find rows faster for filtered or sorted columns.

### 38. When should you add an index?

Add indexes on columns frequently used in `WHERE`, `JOIN`, `ORDER BY`, or uniqueness checks.

### 39. Can too many indexes hurt performance?

Yes. Indexes speed reads but add overhead to writes.

### 40. What is the final MySQL CRUD interview rule?

Use parameterized queries, transactions, validation, error handling, and clear resource cleanup.

## Final Interview Checklist

- Know CRUD and SQL commands.
- Know connection, cursor, execute, commit, rollback.
- Use parameterized queries.
- Avoid SQL injection.
- Know `fetchone()` vs `fetchall()`.
- Use transactions for multi-step writes.
- Handle duplicate keys and missing rows.
- Close connections and cursors.
- Do not hardcode credentials.
- Mention indexes and connection pooling for production systems.

## See also

- [Python MySQL CRUD: core concepts](core-concepts.md)
- [MySQL CRUD reference](mysql-crud-reference.md)
- [MySQL CRUD interview problems](interview-problems.md)
- [REST API design](../rest-api-design/core-concepts.md)
