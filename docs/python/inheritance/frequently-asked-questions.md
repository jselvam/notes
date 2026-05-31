# Python Inheritance: Frequently Asked Interview Questions

## Basic Level

### 1. What is inheritance?

Inheritance lets one class reuse or extend another class.

### 2. What is a parent class?

A parent class is the class being inherited from.

### 3. What is a child class?

A child class is the class that inherits from another class.

### 4. What is a base class?

Base class is another name for parent class.

### 5. What is a subclass?

Subclass is another name for child class.

### 6. How do you inherit in Python?

```python
class DigitalProduct(Product):
    pass
```

### 7. What does a child class inherit?

It can inherit attributes and methods from the parent class.

### 8. What is method overriding?

Method overriding happens when a child class defines a method with the same name as a parent method.

### 9. What is `super()`?

`super()` calls a method from the parent or next class in the MRO.

### 10. Why use inheritance?

Use inheritance to reuse common behavior and model is-a relationships.

## Intermediate Level

### 11. What is single inheritance?

A class inherits from one parent class.

### 12. What is multiple inheritance?

A class inherits from more than one parent class.

### 13. What is multilevel inheritance?

A class inherits from a child class that already inherits from another class.

### 14. What is hierarchical inheritance?

Multiple child classes inherit from the same parent class.

### 15. What is MRO?

MRO stands for Method Resolution Order, the order Python uses to find methods.

### 16. How do you inspect MRO?

```python
print(ClassName.mro())
```

### 17. What is `isinstance()`?

It checks whether an object is an instance of a class or its subclasses.

### 18. What is `issubclass()`?

It checks whether one class inherits from another class.

### 19. What is the difference between `type()` and `isinstance()`?

`type()` checks exact type. `isinstance()` respects inheritance.

### 20. What is the difference between inheritance and composition?

Inheritance is is-a. Composition is has-a.

## Advanced Level

### 21. Why is `super()` better than calling the parent class directly?

`super()` follows MRO and works better with multiple inheritance.

### 22. Should every shared method use inheritance?

No. Sometimes a helper function or composition is clearer.

### 23. What is the diamond problem?

It is a multiple inheritance issue where the same parent appears through multiple paths. Python handles it using MRO.

### 24. What is overloading vs overriding?

Overriding replaces parent behavior in a child class. Traditional method overloading by signature is not how Python normally works.

### 25. Can a child class call a parent method and add extra behavior?

Yes, use `super().method()` inside the child method.

### 26. Can a child override `__init__()`?

Yes. It should usually call `super().__init__()` if the parent initializes needed attributes.

### 27. What is a common inheritance mistake?

Using inheritance for a has-a relationship, such as making `Order` inherit from `Cart`.

### 28. When should you avoid inheritance?

Avoid it when classes are not true specializations or when it creates tight coupling.

### 29. How does inheritance apply to shopping apps?

Use it for specialized products or payment methods, such as `DigitalProduct` from `Product` or `CardPayment` from `PaymentMethod`.

### 30. What should you remember?

Use inheritance for is-a relationships, override carefully, call `super()` when extending parent initialization, and understand MRO.

## Final Interview Checklist

- Parent class is reused by child class.
- Child class can add or override methods.
- `super()` calls parent or next MRO method.
- `isinstance()` is inheritance-aware.
- `issubclass()` checks class relationship.
- MRO controls method lookup.
- Prefer composition for has-a relationships.
- Avoid deep inheritance when simple design works.

## See also

- [Python inheritance: core concepts](core-concepts.md)
- [Python inheritance reference](inheritance-reference.md)
- [Python inheritance interview problems](interview-problems.md)
- [Python OOP core concepts](../oop/core-concepts.md)
