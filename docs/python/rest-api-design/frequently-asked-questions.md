# REST API Design: Frequently Asked Interview Questions

## Basic Level

### 1. What is REST?

REST is an architectural style for designing APIs around resources, HTTP methods, status codes, and representations such as JSON.

### 2. What is a resource?

A resource is a thing exposed by the API, such as product, cart, order, customer, or payment.

### 3. How should REST URLs be named?

Use plural nouns such as `/products`, `/orders`, and `/cart/items`.

### 4. Should REST URLs use verbs?

Usually no. Use HTTP methods for actions and nouns for resources.

### 5. What does `GET` do?

`GET` reads a resource or list of resources.

### 6. What does `POST` do?

`POST` usually creates a new resource or triggers a domain action.

### 7. What does `PUT` do?

`PUT` replaces an entire resource.

### 8. What does `PATCH` do?

`PATCH` updates selected fields of a resource.

### 9. What does `DELETE` do?

`DELETE` removes a resource or marks it deleted depending on business rules.

### 10. What format is commonly used in REST APIs?

JSON is the most common request and response format.

## Intermediate Level

### 11. What status code should creation return?

Use `201 Created`.

### 12. What status code should successful delete return?

Use `204 No Content` when no response body is needed.

### 13. What is `400 Bad Request`?

It means the request is invalid, malformed, or fails basic validation.

### 14. What is `401 Unauthorized`?

It means authentication is missing or invalid.

### 15. What is `403 Forbidden`?

It means the user is authenticated but not allowed to perform the action.

### 16. What is `404 Not Found`?

It means the requested resource does not exist.

### 17. What is `409 Conflict`?

It means the request conflicts with current server state, such as out-of-stock inventory.

### 18. What is `429 Too Many Requests`?

It means the client exceeded a rate limit.

### 19. What is pagination?

Pagination splits large result sets into smaller pages.

### 20. Why is pagination important?

It protects performance and avoids returning huge responses.

## Advanced Level

### 21. What is the difference between path parameters and query parameters?

Path parameters identify resources. Query parameters filter, sort, search, or paginate results.

### 22. Give an example of query parameters.

`GET /products?category=laptop&sort=-price&page=1&limit=20`.

### 23. What is idempotency?

An operation is idempotent if repeating it has the same final effect.

### 24. Which HTTP methods are usually idempotent?

`GET`, `PUT`, and `DELETE` are usually idempotent. `POST` usually is not.

### 25. Why are idempotency keys useful?

They prevent duplicate orders or payments when clients retry requests.

### 26. What is a consistent error response?

It is a predictable JSON structure for all API errors.

### 27. What should an error response contain?

An error code, human-readable message, optional field name, and optional details.

### 28. What is API versioning?

API versioning allows breaking changes without breaking existing clients.

### 29. Give a simple versioning example.

`GET /v1/products` and `GET /v2/products`.

### 30. What is rate limiting?

Rate limiting restricts how many requests a client can make in a time window.

## Pro Level

### 31. What is authentication?

Authentication verifies the identity of the client or user.

### 32. What is authorization?

Authorization checks whether the authenticated user can perform the requested action.

### 33. Why should APIs avoid exposing internal fields?

Internal fields can leak implementation details, security-sensitive data, or unstable contracts.

### 34. How should validation errors be returned?

Return a clear status code and field-level messages so clients can fix input.

### 35. When is `POST /orders/{id}/cancel` acceptable?

It is acceptable for domain actions that do not map cleanly to CRUD.

### 36. What is REST vs RPC?

REST focuses on resources and HTTP semantics. RPC focuses on calling named actions or procedures.

### 37. What is HATEOAS?

HATEOAS means responses include links that guide clients to related actions. It is part of strict REST but not always used in practical APIs.

### 38. What should you log for APIs?

Log request IDs, user IDs, endpoint, status code, latency, and important business errors. Avoid logging secrets.

### 39. What makes an API easy to consume?

Consistent naming, clear errors, good documentation, predictable status codes, and stable contracts.

### 40. What is the final interview rule?

Design APIs around resources, use HTTP semantics correctly, validate inputs, secure endpoints, and document examples clearly.

## Final Interview Checklist

- Use nouns for resources.
- Know `GET`, `POST`, `PUT`, `PATCH`, and `DELETE`.
- Know common `2xx`, `4xx`, and `5xx` status codes.
- Use query parameters for search, filter, sort, and pagination.
- Use consistent JSON error responses.
- Know `401` vs `403`.
- Know `PUT` vs `PATCH`.
- Use idempotency keys for duplicate-sensitive operations.
- Version breaking changes.
- Secure APIs with authentication, authorization, validation, rate limiting, and HTTPS.

## See also

- [REST API design: core concepts](core-concepts.md)
- [REST API design reference](rest-api-design-reference.md)
- [REST API design interview problems](interview-problems.md)
- [Python JSON](../json/core-concepts.md)
