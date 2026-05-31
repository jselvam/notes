# Python Encapsulation: Frequently Asked Interview Questions

## Basic Level

### 1. What is encapsulation?

Encapsulation keeps data and related methods together and controls access to object state.

### 2. Why is encapsulation useful?

It protects data from invalid changes and keeps business rules inside the class.

### 3. Does Python have strict private variables?

No. Python mostly uses naming conventions and name mangling.

### 4. What is a public attribute?

An attribute intended for normal external use, such as `product.name`.

### 5. What does a single underscore mean?

A single underscore means internal or protected by convention, such as `_price`.

### 6. What does a double underscore mean?

Double underscore triggers name mangling, such as `__token`.

### 7. What is name mangling?

Python rewrites double-underscore names internally to reduce accidental access.

### 8. What is a getter?

A getter returns a value in a controlled way.

### 9. What is a setter?

A setter updates a value in a controlled way.

### 10. What is `@property`?

`@property` lets a method be accessed like an attribute.

## Intermediate Level

### 11. How do you validate assignment in Python?

Use a property setter.

### 12. Why use `_price` behind a `price` property?

`_price` stores the internal value while `price` controls public access.

### 13. What is a read-only property?

A property with a getter but no setter.

### 14. Can users still access `_price`?

Yes. The underscore is a convention, not a hard restriction.

### 15. Can users access `__token`?

Not directly by that name, but it can still be accessed through its mangled name. It is not true security.

### 16. Why return a copy of a list?

To prevent outside code from changing the object's internal list directly.

### 17. Should all attributes be private-style?

No. Use public attributes when direct access is safe and clear.

### 18. What is the difference between encapsulation and abstraction?

Encapsulation controls access to data. Abstraction hides implementation details behind a simpler interface.

### 19. How is encapsulation used in a shopping app?

It protects price, stock, payment tokens, cart items, and order status transitions.

### 20. What is a common beginner mistake?

Making everything public and allowing invalid state changes from outside the class.

## Advanced Level

### 21. Is encapsulation only about private variables?

No. It is mainly about protecting invariants and controlling how state changes.

### 22. What is an invariant?

An invariant is a rule that should always remain true, such as price must not be negative.

### 23. When should you use a method instead of a setter?

Use a method when the action represents behavior, such as `reserve_stock()` or `mark_paid()`.

### 24. Can encapsulation improve testing?

Yes. Business rules are centralized in methods and properties, so tests can focus on those APIs.

### 25. Does encapsulation prevent all misuse?

No. Python trusts developers, but encapsulation makes correct use obvious and misuse less likely.

### 26. What is the risk of exposing mutable data?

External code can mutate internal state without validation.

### 27. What is the best way to expose cart items safely?

Return a copy, tuple, or read-only view, depending on the design.

### 28. What is a common interview trap?

Saying Python has Java-style private fields. Python uses conventions and name mangling instead.

### 29. What is the relationship between encapsulation and `@property`?

`@property` provides controlled attribute access while keeping a clean public API.

### 30. What should you remember?

Protect object state, validate changes, use `_name` for internal attributes, use properties carefully, and avoid exposing mutable internals.

## Final Interview Checklist

- Encapsulation protects object state.
- Public names are normal API.
- `_name` means internal by convention.
- `__name` triggers name mangling.
- `@property` creates controlled attribute access.
- Setters validate assignments.
- Methods should enforce business rules.
- Return copies for mutable internal data when needed.
- Python privacy is convention-based, not absolute.

## See also

- [Python encapsulation: core concepts](core-concepts.md)
- [Python encapsulation reference](encapsulation-reference.md)
- [Python encapsulation interview problems](interview-problems.md)
- [Python class properties and self](../class-properties-self/core-concepts.md)
