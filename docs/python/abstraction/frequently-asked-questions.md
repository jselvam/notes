# Python Data Abstraction: Frequently Asked Interview Questions

## Basic Level

### 1. What is data abstraction?

Data abstraction hides implementation details and exposes only the important behavior.

### 2. Why is abstraction useful?

It makes code easier to use, change, and test because callers depend on a simple interface.

### 3. What is an example of abstraction?

Calling `payment.pay(amount)` without knowing how payment is processed.

### 4. Is abstraction one of the OOP pillars?

Yes. Abstraction is one of the main OOP concepts.

### 5. How does Python support abstraction?

Python supports abstraction with classes, methods, properties, duck typing, and abstract base classes.

### 6. Which module supports abstract classes?

The `abc` module.

### 7. What is `ABC`?

`ABC` is the base class used to define abstract base classes.

### 8. What is `@abstractmethod`?

It marks a method that child classes must implement.

### 9. Can you instantiate an abstract class?

Not if it still has unimplemented abstract methods.

### 10. What is a concrete class?

A concrete class is a usable implementation of an abstract idea.

## Intermediate Level

### 11. What is an interface?

An interface is a set of expected behaviors, such as a `pay()` method for payment classes.

### 12. Does Python have Java-style interfaces?

No. Python commonly uses abstract base classes, protocols, or duck typing.

### 13. What is duck typing?

Duck typing means behavior matters more than exact type.

### 14. How is duck typing related to abstraction?

It lets code depend on expected methods instead of specific classes.

### 15. What is abstraction vs encapsulation?

Abstraction hides implementation details. Encapsulation controls access to data.

### 16. What is abstraction vs inheritance?

Inheritance models relationships and reuse. Abstraction hides details behind a simpler interface.

### 17. Can `@property` be abstraction?

Yes. It can hide a calculation behind attribute-style access.

### 18. Why keep interfaces small?

Small interfaces are easier to implement, test, and maintain.

### 19. What is a service abstraction?

A service class exposes simple methods while hiding internal storage, APIs, or algorithms.

### 20. How does abstraction help testing?

Tests can replace real implementations with simple fake objects that follow the same interface.

## Advanced Level

### 21. When should you use an abstract base class?

Use it when multiple classes must share a required method contract.

### 22. When should you avoid abstract classes?

Avoid them when they add complexity without multiple real implementations.

### 23. What is a strategy pattern?

It is a design pattern where interchangeable objects implement the same operation, such as discount strategies.

### 24. How does abstraction reduce coupling?

High-level code depends on behavior, not low-level implementation details.

### 25. What is the dependency inversion idea?

High-level logic should depend on abstractions instead of concrete low-level details.

### 26. What is a common abstraction mistake?

Creating too many abstract classes before the code actually needs them.

### 27. How does abstraction apply to shopping apps?

Payment, notification, inventory, discount, and shipping logic can be hidden behind simple methods.

### 28. What is a real-world payment abstraction?

`PaymentMethod.pay(amount)` can have card, UPI, wallet, and cash-on-delivery implementations.

### 29. How is abstraction different from hiding data?

Hiding data is encapsulation. Hiding implementation behavior behind a simple API is abstraction.

### 30. What should you remember?

Abstraction exposes what an object does and hides how it does it.

## Final Interview Checklist

- Abstraction hides implementation details.
- Use simple method names like `pay()`, `send()`, `reserve()`.
- Use `ABC` and `@abstractmethod` for explicit contracts.
- Use duck typing when a formal abstract class is unnecessary.
- Keep interfaces small.
- Do not over-engineer simple code.
- Know abstraction vs encapsulation.
- Know abstraction vs inheritance.

## See also

- [Python data abstraction: core concepts](core-concepts.md)
- [Python data abstraction reference](abstraction-reference.md)
- [Python data abstraction interview problems](interview-problems.md)
- [Python encapsulation](../encapsulation/core-concepts.md)
