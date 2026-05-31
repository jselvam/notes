# Python Class Relationships: Frequently Asked Interview Questions

## Basic Level

### 1. What are class relationships?

Class relationships describe how classes connect, use, contain, or depend on each other.

### 2. What is association?

Association means one class uses or knows another class.

### 3. What is aggregation?

Aggregation is a weak has-a relationship where the contained object can live independently.

### 4. What is composition?

Composition is a strong has-a relationship where the contained object is owned by the parent object.

### 5. What is inheritance?

Inheritance is an is-a relationship where one class extends another.

### 6. What is an example of association?

A `Customer` places an `Order`.

### 7. What is an example of aggregation?

A `Cart` has `Product` objects, but products can exist outside the cart.

### 8. What is an example of composition?

An `Order` owns `OrderLine` objects created inside the order.

### 9. What phrase describes aggregation and composition?

Both are has-a relationships.

### 10. What phrase describes inheritance?

Inheritance is an is-a relationship.

## Intermediate Level

### 11. What is the difference between association and aggregation?

Association means uses-a or knows-a. Aggregation means has-a with weak ownership.

### 12. What is the difference between aggregation and composition?

In aggregation, the child can exist independently. In composition, the child is strongly owned by the parent.

### 13. What is the difference between composition and inheritance?

Composition is has-a. Inheritance is is-a.

### 14. Why is composition often preferred?

It usually creates simpler, more flexible designs than deep inheritance.

### 15. When should you use association?

Use association when one object only needs to interact with another object.

### 16. When should you use aggregation?

Use aggregation when one object stores references to other independent objects.

### 17. When should you use composition?

Use composition when one object owns and manages the lifetime of another object.

### 18. Is `Order` inheriting from `Cart` a good design?

Usually no. An order is not a cart; it may have a cart or order lines.

### 19. Is `DigitalProduct` inheriting from `Product` a good design?

Yes, if a digital product is a specialized product.

### 20. Can the same real-world relationship be modeled in different ways?

Yes. Ownership and lifecycle rules decide the best model.

## Advanced Level

### 21. How do you identify composition?

Look for objects created inside and controlled by the owning class.

### 22. How do you identify aggregation?

Look for objects created outside and passed into the container class.

### 23. Can composition use constructor injection?

Yes. Some designs pass a child object in but still treat it as owned by the parent. Be clear about ownership rules.

### 24. Why does lifetime matter?

It tells whether the child should survive independently when the parent is gone.

### 25. What is a common interview mistake?

Confusing composition with inheritance because both reuse code.

### 26. How does composition reuse code?

One object delegates work to another object it contains.

### 27. How does inheritance reuse code?

A child class gets behavior from a parent class.

### 28. How does aggregation apply to products?

Products often exist independently and can be referenced by carts, wishlists, or orders.

### 29. How does composition apply to order lines?

Order lines usually belong to one order and are created as part of that order.

### 30. What should you remember?

Association is uses-a, aggregation is weak has-a, composition is strong owns-a, and inheritance is is-a.

## Final Interview Checklist

- Association: uses-a or knows-a.
- Aggregation: weak has-a.
- Composition: strong owns-a.
- Inheritance: is-a.
- Use composition for object parts.
- Use aggregation for independent contained objects.
- Use association for temporary interaction.
- Use inheritance only for true specialization.
- Always think about object lifetime.

## See also

- [Python class relationships: core concepts](core-concepts.md)
- [Python class relationships reference](class-relationships-reference.md)
- [Python class relationships interview problems](interview-problems.md)
- [Python inheritance](../inheritance/core-concepts.md)
