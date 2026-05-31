# REST API Design Reference

## Quick Reference

| Design area | Recommended practice |
|-------------|----------------------|
| resources | use plural nouns, such as `/products` |
| methods | use HTTP verbs for actions |
| status codes | return meaningful HTTP status |
| request body | use JSON for create/update |
| query params | use for filter, search, sort, pagination |
| errors | return consistent error shape |
| security | use authentication and authorization |
| versioning | version breaking changes |
| idempotency | prevent duplicate risky operations |

## Resource Naming

Use nouns, not verbs.

```http
GET /products
GET /products/101
POST /orders
GET /customers/7/orders
```

Avoid:

```http
GET /getProducts
POST /createOrder
```

## CRUD Mapping

| Operation | HTTP method | Endpoint |
|-----------|-------------|----------|
| list products | `GET` | `/products` |
| get one product | `GET` | `/products/{id}` |
| create product | `POST` | `/products` |
| replace product | `PUT` | `/products/{id}` |
| partially update product | `PATCH` | `/products/{id}` |
| delete product | `DELETE` | `/products/{id}` |

## Status Code Reference

| Code | Use case |
|------|----------|
| `200 OK` | read or update succeeded |
| `201 Created` | new resource created |
| `202 Accepted` | request accepted for async processing |
| `204 No Content` | success without response body |
| `400 Bad Request` | invalid request format or validation error |
| `401 Unauthorized` | authentication required or invalid |
| `403 Forbidden` | authenticated but not allowed |
| `404 Not Found` | resource does not exist |
| `409 Conflict` | conflict with current state |
| `422 Unprocessable Entity` | semantic validation failure |
| `429 Too Many Requests` | rate limit exceeded |
| `500 Internal Server Error` | unexpected server error |

## Request Validation Example

```json
{
  "product_id": 101,
  "quantity": 2
}
```

Validate:

- required fields
- data types
- allowed ranges
- business rules

Example error:

```json
{
  "error": {
    "code": "INVALID_QUANTITY",
    "message": "Quantity must be greater than zero",
    "field": "quantity"
  }
}
```

## Filtering, Sorting, and Pagination

```http
GET /products?category=laptop&min_price=500&sort=-price&page=1&limit=20
```

Common conventions:

- `category=laptop` for filtering
- `sort=price` for ascending sort
- `sort=-price` for descending sort
- `page` and `limit` for pagination

## Nested Resources

Use nested resources when the child belongs naturally to the parent.

```http
GET /orders/5001/items
POST /orders/5001/items
```

Avoid deeply nested URLs:

```http
GET /customers/7/orders/5001/items/9/refunds/2/status
```

Prefer simpler resources when nesting gets too deep.

## PUT vs PATCH

| Method | Meaning |
|--------|---------|
| `PUT` | replace the full resource |
| `PATCH` | update selected fields |

Example `PATCH`:

```http
PATCH /products/101
```

```json
{
  "price": 899.99
}
```

## Idempotency Key

Use idempotency keys for operations where duplicate requests are dangerous.

```http
POST /orders
Idempotency-Key: checkout-1001-user-7
```

If the same key is repeated, the server should return the same result instead of creating duplicate orders.

## Security Reference

| Concern | API design practice |
|---------|---------------------|
| authentication | bearer token, session, API key |
| authorization | role and ownership checks |
| validation | reject malformed input |
| rate limiting | prevent abuse |
| sensitive data | do not expose passwords or secrets |
| transport | use HTTPS |

## Common Endpoint Examples

```http
GET /products
GET /products/101
POST /cart/items
PATCH /cart/items/10
DELETE /cart/items/10
POST /orders
GET /orders/5001
POST /orders/5001/cancel
```

`POST /orders/5001/cancel` is acceptable because cancel is a domain action, not a simple CRUD update.

## Common Comparisons

| Comparison | Difference |
|------------|------------|
| path params vs query params | identity vs filtering/options |
| `401` vs `403` | not authenticated vs not allowed |
| `400` vs `422` | bad request format vs semantic validation failure |
| `PUT` vs `PATCH` | full replace vs partial update |
| REST vs RPC | resources and HTTP semantics vs action-style procedures |
| authentication vs authorization | who you are vs what you can do |

## See also

- [REST API design: core concepts](core-concepts.md)
- [REST API design interview problems](interview-problems.md)
- [REST API design FAQ](frequently-asked-questions.md)
- [Python JSON](../json/core-concepts.md)
