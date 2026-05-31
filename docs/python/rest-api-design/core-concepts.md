# REST API Design: Core Concepts

REST API design is about creating HTTP APIs that are predictable, consistent, secure, and easy for clients to use.

Examples use an online computer shopping system.

## What Is REST?

REST stands for Representational State Transfer. In practical API design, it means using HTTP methods, URLs, status codes, and representations such as JSON in a consistent way.

Example resource:

```http
GET /products/101
```

Example response:

```json
{
  "id": 101,
  "name": "Laptop",
  "price": 999.99
}
```

## Resources

REST APIs are centered around resources, usually nouns.

Good:

```http
GET /products
GET /products/101
GET /orders/5001
```

Avoid action-heavy URLs:

```http
GET /getProduct
POST /createOrder
```

## HTTP Methods

| Method | Meaning | Example |
|--------|---------|---------|
| `GET` | read data | `GET /products` |
| `POST` | create data | `POST /orders` |
| `PUT` | replace full resource | `PUT /products/101` |
| `PATCH` | update part of resource | `PATCH /products/101` |
| `DELETE` | delete resource | `DELETE /cart/items/10` |

## Status Codes

| Code | Meaning | Example |
|------|---------|---------|
| `200 OK` | successful read/update | product returned |
| `201 Created` | resource created | order placed |
| `204 No Content` | success with no body | item deleted |
| `400 Bad Request` | invalid input | missing quantity |
| `401 Unauthorized` | not logged in | missing token |
| `403 Forbidden` | no permission | non-admin updating price |
| `404 Not Found` | resource missing | product not found |
| `409 Conflict` | state conflict | out-of-stock order |
| `500 Internal Server Error` | server bug | unexpected failure |

## JSON Request and Response

Use JSON for most API request and response bodies.

```http
POST /cart/items
Content-Type: application/json
```

```json
{
  "product_id": 101,
  "quantity": 2
}
```

Response:

```json
{
  "cart_id": 88,
  "items": [
    {
      "product_id": 101,
      "quantity": 2
    }
  ]
}
```

## Query Parameters

Use query parameters for filtering, sorting, searching, and pagination.

```http
GET /products?category=laptop&sort=price&page=1&limit=20
```

## Path Parameters

Use path parameters for resource identity.

```http
GET /products/101
GET /orders/5001/items
```

## Pagination

Do not return huge lists in one response.

```http
GET /products?page=2&limit=20
```

Example response:

```json
{
  "data": [],
  "page": 2,
  "limit": 20,
  "total": 125
}
```

## Error Response Shape

Keep error responses consistent.

```json
{
  "error": {
    "code": "OUT_OF_STOCK",
    "message": "Only 1 item is available",
    "field": "quantity"
  }
}
```

## Idempotency

An operation is idempotent if making the same request multiple times has the same final effect.

| Method | Usually idempotent? |
|--------|---------------------|
| `GET` | yes |
| `PUT` | yes |
| `PATCH` | depends |
| `DELETE` | usually yes |
| `POST` | usually no |

For payment or order creation APIs, use idempotency keys to avoid duplicate orders.

```http
POST /orders
Idempotency-Key: order-abc-123
```

## Authentication and Authorization

Authentication verifies who the user is. Authorization verifies what the user can do.

```http
Authorization: Bearer <token>
```

Example:

- customer can read their own orders
- admin can update product prices
- warehouse user can update stock

## Versioning

Version APIs when breaking changes are needed.

```http
GET /v1/products
GET /v2/products
```

Avoid breaking clients silently.

## REST API Design Checklist

- Use nouns for resources.
- Use HTTP methods correctly.
- Use consistent status codes.
- Validate request bodies.
- Return consistent error shapes.
- Support pagination for lists.
- Use filtering and sorting with query parameters.
- Protect APIs with authentication and authorization.
- Use idempotency for risky create operations.
- Document request and response examples.

## See also

- [REST API design reference](rest-api-design-reference.md)
- [REST API design interview problems](interview-problems.md)
- [REST API design FAQ](frequently-asked-questions.md)
- [Python JSON](../json/core-concepts.md)
- [Exception handling](../exception-handling/core-concepts.md)
