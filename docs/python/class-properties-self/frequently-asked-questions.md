# Python Class Properties and self: Frequently Asked Interview Questions

## Basic Level

### 1. What is `self` in Python?

`self` refers to the current object instance.

### 2. Is `self` a Python keyword?

No. It is a naming convention, but Python developers strongly expect it.

### 3. Why do instance methods need `self`?

They need `self` to access or update the current object's data.

### 4. What is an instance property?

An instance property is data stored on a specific object, such as `self.price`.

### 5. What is a class property?

A class property is data stored on the class and shared by instances.

### 6. How do you create an instance property?

Assign to `self` inside a method.

```python
self.name = name
```

### 7. How do you create a class property?

Assign inside the class body, outside methods.

```python
class Product:
    currency = "USD"
```

### 8. What is `@property`?

`@property` lets a method be accessed like an attribute.

### 9. What is a setter?

A setter controls what happens when a property is assigned.

### 10. What does `_price` mean?

It is a convention that the attribute is internal to the class.

## Intermediate Level

### 11. What is the difference between class property and instance property?

Class properties are shared. Instance properties belong to one object.

### 12. Can an instance access a class property?

Yes.

```python
product.currency
```

### 13. Can a class access an instance property?

Not without an object, because instance properties belong to objects.

### 14. What happens when you assign `product.currency = "INR"`?

It creates or updates an instance attribute named `currency`, shadowing the class property for that object.

### 15. Why avoid mutable class properties?

They are shared across instances and can cause accidental shared state.

### 16. When should you use `@property`?

Use it for computed values or controlled access that should look like an attribute.

### 17. When should you use a normal method instead of `@property`?

Use a method when the operation is expensive, changes state, or requires parameters.

### 18. What is a read-only property?

A property with no setter.

### 19. Can a setter raise an exception?

Yes. Setters often raise `ValueError` for invalid values.

### 20. What is method binding?

When you call `object.method()`, Python automatically passes the object as the first argument.

## Advanced Level

### 21. Why does `Product.label(product)` work?

Methods are functions stored on the class, and passing the object manually can work like the automatic `self` binding.

### 22. What is attribute shadowing?

It happens when an instance attribute has the same name as a class attribute.

### 23. How do you access a class property inside a method?

Use `self.property_name` or `ClassName.property_name`.

### 24. Which is better: `self.tax_rate` or `Product.tax_rate`?

Use `self.tax_rate` if subclasses or instances may override it. Use `Product.tax_rate` when you specifically want the base class value.

### 25. Does `@property` store data?

No. It defines a method that computes or returns data. The actual storage is usually another attribute like `_price`.

### 26. Can `@property` be used for validation?

Validation usually happens in the setter, not in the getter.

### 27. What is a common `self` mistake?

Forgetting `self` in the method definition or forgetting `self.` when assigning object data.

### 28. What is a common class property mistake?

Using a class-level list or dictionary for per-object data.

### 29. How does this apply to shopping systems?

Products use instance properties for price/name, class properties for shared currency/tax rules, and properties for formatted or validated values.

### 30. What should you remember?

Use `self` for object state, class properties for shared state, `@property` for computed attributes, and setters for validation.

## Final Interview Checklist

- `self` means current object.
- Instance properties are per object.
- Class properties are shared.
- Methods need `self` to access object state.
- `@property` makes a method look like an attribute.
- Setters validate assignments.
- Avoid mutable class properties for per-object state.
- Attribute shadowing can hide class properties on one object.

## See also

- [Python class properties and self: core concepts](core-concepts.md)
- [Python class properties and self reference](class-properties-self-reference.md)
- [Python class properties and self interview problems](interview-problems.md)
- [Python classes and objects](../classes-and-objects/core-concepts.md)
