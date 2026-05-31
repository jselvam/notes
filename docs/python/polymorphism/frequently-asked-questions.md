# Python Polymorphism: Frequently Asked Interview Questions

## Basic Level

### 1. What is polymorphism?

Polymorphism means one interface can have many implementations.

### 2. What does polymorphism mean in OOP?

Different classes can respond to the same method call in different ways.

### 3. What is a simple example?

`CardPayment.pay()` and `UPIPayment.pay()` use the same method name but different behavior.

### 4. Why is polymorphism useful?

It makes code flexible and easier to extend.

### 5. Is polymorphism only possible with inheritance?

No. Python also supports polymorphism through duck typing and dunder methods.

### 6. What is duck typing?

Duck typing means Python cares about what methods an object has, not only what class it belongs to.

### 7. What is method overriding?

A child class provides its own version of a parent class method.

### 8. What is built-in polymorphism?

Built-in functions such as `len()` work with many different types.

### 9. What is operator polymorphism?

The same operator behaves differently for different types, such as `+` for numbers, strings, and lists.

### 10. What is an interface in polymorphism?

An interface is the expected method or behavior, such as `pay()` or `send()`.

## Intermediate Level

### 11. How does polymorphism help checkout code?

Checkout can call `payment_method.pay(amount)` without knowing the exact payment type.

### 12. How does polymorphism reduce `if`/`else` code?

Instead of checking every payment type, each payment class implements its own behavior.

### 13. What is polymorphism vs inheritance?

Inheritance is a class relationship. Polymorphism is using the same interface with different behavior.

### 14. What is polymorphism vs abstraction?

Abstraction hides details behind an interface. Polymorphism lets multiple implementations use that interface.

### 15. What is polymorphism vs overloading?

Polymorphism is broader. Overloading means same name with different parameter patterns; Python does not use Java-style overloads normally.

### 16. Can functions be polymorphic in Python?

Yes. A function can accept any object that supports the needed behavior.

### 17. How does `len()` show polymorphism?

It calls type-specific behavior for strings, lists, dictionaries, and custom objects with `__len__()`.

### 18. How does `+` show polymorphism?

It adds numbers, concatenates strings, combines lists, or calls custom `__add__()`.

### 19. What dunder methods support polymorphism?

Examples include `__len__`, `__add__`, `__eq__`, `__lt__`, and `__iter__`.

### 20. Should every polymorphic design use an abstract class?

No. Use abstract classes when an explicit contract helps; otherwise duck typing can be enough.

## Advanced Level

### 21. What is runtime polymorphism?

Runtime polymorphism means Python decides which method implementation to call while the program runs.

### 22. What is compile-time polymorphism?

In languages like Java, it often refers to method overloading. Python handles this differently with dynamic typing and default arguments.

### 23. What is the Open/Closed Principle connection?

Polymorphism helps code stay open for extension and closed for modification.

### 24. How does polymorphism support strategy pattern?

Different strategy objects implement the same method, such as `apply(price)` for discounts.

### 25. What is a common polymorphism mistake?

Using the same method name for unrelated behavior, making the interface confusing.

### 26. What happens if an object lacks the expected method?

Python raises `AttributeError`.

### 27. How do you make a custom object work with `len()`?

Implement `__len__()`.

### 28. How do you make a custom object work with `+`?

Implement `__add__()`.

### 29. How does polymorphism apply to shopping apps?

Payments, discounts, notifications, shipping, and product delivery can all use common interfaces with different implementations.

### 30. What should you remember?

Polymorphism lets code call the same method or operation while objects decide their own behavior.

## Final Interview Checklist

- Polymorphism means many forms.
- Same method name can have different implementations.
- Method overriding is a common OOP form.
- Duck typing is very important in Python.
- Built-ins like `len()` are polymorphic.
- Operators like `+` are polymorphic.
- Dunder methods enable custom polymorphic behavior.
- Use polymorphism to reduce repeated type checks.

## See also

- [Python polymorphism: core concepts](core-concepts.md)
- [Python polymorphism reference](polymorphism-reference.md)
- [Python polymorphism interview problems](interview-problems.md)
- [Python data abstraction](../abstraction/core-concepts.md)
