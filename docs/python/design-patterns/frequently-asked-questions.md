# Python Design Patterns: Frequently Asked Interview Questions

## Basic Level

### 1. What is a design pattern?

A design pattern is a reusable solution idea for a common software design problem.

### 2. Are design patterns language-specific?

No. Patterns are general ideas, but their implementation changes based on the language.

### 3. Why are design patterns important in Python interviews?

They show that you can structure code, manage change, and explain trade-offs.

### 4. What is Singleton?

Singleton ensures a class has only one shared instance.

### 5. What is a common Singleton example?

A shared database connection or application configuration object.

### 6. What is Factory?

Factory creates objects without exposing object creation details to the caller.

### 7. What is a common Factory example?

Creating different product objects such as laptop, mouse, monitor, or software subscription.

### 8. What is Strategy?

Strategy lets you switch behavior or algorithms at runtime.

### 9. What is a common Strategy example?

Payment methods such as UPI, card, and PayPal.

### 10. What is Observer?

Observer notifies many subscribers when an object changes.

## Intermediate Level

### 11. What is a common Observer example?

Order status notifications to email, SMS, and push notification services.

### 12. What is Decorator?

Decorator adds behavior around a function or object without changing its core code.

### 13. What are common Decorator examples?

Logging, security checks, caching, validation, and timing.

### 14. What is Adapter?

Adapter converts an incompatible interface into the interface your code expects.

### 15. What is a common Adapter example?

Wrapping a third-party shipping API so the app can call `ship(order)`.

### 16. What is Command?

Command wraps an action as an object.

### 17. What is a common Command example?

Cancel order with undo support.

### 18. What is the difference between Factory and Strategy?

Factory creates objects. Strategy uses interchangeable behavior.

### 19. What is the difference between Adapter and Decorator?

Adapter changes an interface. Decorator adds behavior while keeping the same interface.

### 20. What is the difference between Observer and Strategy?

Observer handles event notification. Strategy handles interchangeable algorithms.

## Advanced Level

### 21. When should you avoid Singleton?

Avoid it when it hides dependencies, makes tests difficult, or behaves like a global variable.

### 22. What is a better alternative to Singleton in many Python apps?

Dependency injection, module-level objects, or framework-managed connection pools.

### 23. How does Factory improve code?

It centralizes object creation and keeps calling code independent of concrete classes.

### 24. How can Strategy remove conditionals?

Instead of `if payment_type == ...`, pass an object with a common `pay()` method.

### 25. How does Observer reduce coupling?

The subject publishes changes without knowing each concrete subscriber's business logic.

### 26. What is a risk of Observer?

Too many hidden notifications can make behavior harder to trace.

### 27. How do Python decorators relate to the Decorator pattern?

Python decorators are syntax for wrapping functions or classes, commonly used to implement decorator-style behavior.

### 28. Why is Adapter useful with third-party APIs?

It isolates external method names, payload formats, and provider changes.

### 29. How does Command support undo?

The command stores enough previous state to reverse its action.

### 30. How does Command support queues?

Commands can be stored and executed later by a worker or task runner.

## Pro Level

### 31. Which patterns are creational?

Singleton and Factory are creational patterns because they control object creation.

### 32. Which patterns are behavioral?

Strategy, Observer, and Command are behavioral patterns because they organize object behavior and communication.

### 33. Which patterns are structural?

Adapter is structural. Decorator is also often treated as structural, though Python decorators are function-level tools too.

### 34. Can Python functions replace some pattern classes?

Yes. Python's first-class functions often make Strategy, Factory, and Command simpler.

### 35. Give a function-based Strategy example.

Pass a payment function into checkout instead of a payment class when the behavior is simple.

### 36. Give a function-based Factory example.

Use a dictionary mapping product type strings to constructors.

### 37. What is overusing patterns called?

Over-engineering. It adds complexity without real benefit.

### 38. How should you answer pattern questions in interviews?

Explain the problem, choose the pattern, show a small code example, and mention trade-offs.

### 39. Which pattern fits logging?

Decorator is a good fit because logging wraps behavior.

### 40. Which pattern fits multiple notification channels?

Observer is a good fit because several subscribers react to one event.

### 41. Which pattern fits payment selection?

Strategy is a good fit because payment behavior changes while checkout stays stable.

### 42. Which pattern fits shipping provider integration?

Adapter is a good fit because third-party APIs often have incompatible interfaces.

### 43. Which pattern fits product object creation?

Factory is a good fit because product creation can vary by type.

### 44. Which pattern fits cancel and undo?

Command is a good fit because the action can be executed, stored, and undone.

### 45. What is the final rule for design patterns?

Use a pattern when it makes change easier and the code clearer, not just because the pattern exists.

## Final Interview Checklist

- Explain each pattern with one sentence.
- Give the shopping-system use case for each pattern.
- Know which patterns are creational, structural, and behavioral.
- Mention Python alternatives such as functions, dictionaries, and dependency injection.
- Discuss trade-offs such as hidden dependencies, over-engineering, and testability.
- Prefer simple code when a full pattern is unnecessary.

## See also

- [Design patterns: core concepts](core-concepts.md)
- [Design patterns reference](design-patterns-reference.md)
- [Design patterns interview problems](interview-problems.md)
- [Design principles](../design-principles/core-concepts.md)
