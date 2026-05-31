# REST API Design Interview Problems

## 1. Design Product CRUD APIs

### Problem

Design REST endpoints for product management.

### Solution

```http
GET /products
GET /products/101
POST /products
PUT /products/101
PATCH /products/101
DELETE /products/101
```

### Interview Point

Use plural nouns for resources and HTTP methods for actions.

## 2. Design Add to Cart API

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

Possible response:

```http
201 Created
```

```json
{
  "cart_item_id": 10,
  "product_id": 101,
  "quantity": 2
}
```

## 3. Choose Status Code for Missing Product

If a product does not exist:

```http
404 Not Found
```

```json
{
  "error": {
    "code": "PRODUCT_NOT_FOUND",
    "message": "Product 101 was not found"
  }
}
```

## 4. Design Product Search API

```http
GET /products?query=laptop&category=computer&sort=-price&page=1&limit=20
```

Use query parameters for searching, filtering, sorting, and pagination.

## 5. Design Order Creation API

```http
POST /orders
Idempotency-Key: checkout-user-7-cart-88
```

```json
{
  "cart_id": 88,
  "shipping_address_id": 5,
  "payment_method": "card"
}
```

Return:

```http
201 Created
```

## 6. Handle Out-of-Stock Error

Use `409 Conflict` when the request conflicts with current inventory state.

```http
409 Conflict
```

```json
{
  "error": {
    "code": "OUT_OF_STOCK",
    "message": "Only 1 laptop is available",
    "field": "quantity"
  }
}
```

## 7. Design Cancel Order API

For a domain action, this is acceptable:

```http
POST /orders/5001/cancel
```

Return:

```json
{
  "order_id": 5001,
  "status": "cancelled"
}
```

## 8. Design Authentication Rules

### Problem

Who can access order data?

### Answer

- Customer can view their own orders.
- Admin can view all orders.
- Unauthenticated user gets `401`.
- Authenticated user without permission gets `403`.

## 9. Design Consistent Error Response

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Request body has invalid fields",
    "details": [
      {
        "field": "quantity",
        "message": "Quantity must be greater than zero"
      }
    ]
  }
}
```

## 10. Explain PUT vs PATCH

`PUT` replaces a full resource. `PATCH` updates selected fields.

```http
PATCH /products/101
```

```json
{
  "price": 899.99
}
```

## 11. Design Rate Limit Response

```http
429 Too Many Requests
Retry-After: 60
```

Use rate limiting to protect login, checkout, search, and public APIs.

## 12. Choose API Versioning Strategy

Simple URL versioning:

```http
GET /v1/products
GET /v2/products
```

Use a new version for breaking changes, not every small change.

## Summary

In REST API interviews, explain resources, methods, status codes, validation, security, pagination, and idempotency with concrete endpoint examples.

## See also

- [REST API design: core concepts](core-concepts.md)
- [REST API design reference](rest-api-design-reference.md)
- [REST API design FAQ](frequently-asked-questions.md)
