# Python Design Principles: Frequently Asked Interview Questions

## Basic Level

### 1. What are design principles?

Design principles are guidelines for writing code that is easier to understand, test, and change.

### 2. What is SOLID?

SOLID is a set of five object-oriented design principles: SRP, OCP, LSP, ISP, and DIP.

### 3. What is SRP?

Single Responsibility Principle means a class should have one main responsibility and one reason to change.

### 4. What is OCP?

Open/Closed Principle means code should be open for extension but closed for modification.

### 5. What is LSP?

Liskov Substitution Principle means subclasses should work wherever parent classes are expected.

### 6. What is ISP?

Interface Segregation Principle means clients should not be forced to depend on methods they do not use.

### 7. What is DIP?

Dependency Inversion Principle means high-level code should depend on abstractions, not concrete details.

### 8. What is DRY?

DRY means Don't Repeat Yourself. Keep each business rule in one place.

### 9. What is KISS?

KISS means Keep It Simple, Stupid. Prefer simple readable solutions.

### 10. What is composition over inheritance?

It means building behavior by combining objects instead of creating deep inheritance chains.

## Intermediate Level

### 11. Why is SRP useful?

It makes code easier to test, debug, and change because each class has a focused job.

### 12. Give a Python SRP example.

Keep `Order`, `OrderRepository`, and `EmailService` separate instead of placing all behavior inside one class.

### 13. How does OCP help in interviews?

It shows that you can add features, such as new discounts, without rewriting stable checkout code.

### 14. Give an OCP example.

Create a base `Discount` class and add `FestivalDiscount`, `StudentDiscount`, or `BulkDiscount` as separate classes.

### 15. What is an LSP violation?

A subclass violates LSP when it cannot safely replace its parent class.

### 16. Give an LSP example.

If `PaymentMethod.pay()` is expected to complete payment, a subclass that raises `NotImplementedError` breaks that contract.

### 17. Why is ISP useful in Python?

Even without formal interfaces, Python code benefits from small focused protocols and duck typing.

### 18. Give an ISP example.

Separate `Printer` and `Scanner` behavior so a receipt printer does not need scan methods.

### 19. What is dependency injection?

Dependency injection means passing required services into a class instead of creating them inside the class.

### 20. How does DIP improve testing?

You can pass a fake payment gateway or fake notifier during tests.

## Advanced Level

### 21. Is DRY always good?

No. Removing repetition too early can create confusing abstractions. DRY repeated knowledge, not every similar-looking line.

### 22. How can DRY go wrong?

It can couple unrelated code paths if they look similar today but will change differently later.

### 23. Is KISS against design patterns?

No. KISS says use patterns only when they make the solution clearer or more maintainable.

### 24. How does composition help avoid inheritance problems?

It lets behavior vary independently without creating many subclasses.

### 25. Give a composition example.

A `Cart` can have a `DiscountPolicy` instead of inheriting from `StudentDiscountCart` or `FestivalDiscountCart`.

### 26. When should you still use inheritance?

Use inheritance when there is a true is-a relationship and subclasses preserve parent behavior.

### 27. What is the difference between composition and aggregation?

Composition usually means strong ownership; aggregation usually means weaker ownership.

### 28. What is over-engineering?

Over-engineering means adding unnecessary layers, patterns, or abstractions for a simple problem.

### 29. How do you balance DRY and KISS?

First make code clear. Then remove duplication when the same rule appears repeatedly.

### 30. How do SOLID principles relate to Python duck typing?

Python often uses behavior-based interfaces. SOLID still applies, but code may use protocols, abstract base classes, or simple duck typing.

## Pro Level

### 31. How can Python protocols support DIP?

Protocols describe required behavior without tying code to one concrete class.

### 32. How can abstract base classes support OCP?

They define stable contracts while allowing new implementations to be added.

### 33. Why is subclassing sometimes risky?

Subclasses are tightly coupled to parent implementation details.

### 34. What is fragile base class problem?

It happens when parent class changes unexpectedly break subclasses.

### 35. How does composition reduce coupling?

Objects depend on small collaborator behavior rather than inherited internal details.

### 36. What is a good interview answer for composition over inheritance?

Use inheritance for stable is-a relationships and composition for changeable has-a behavior.

### 37. How does SRP relate to microservices?

Both prefer focused responsibilities, but SRP applies inside code and microservices apply at system boundaries.

### 38. How does DIP relate to mocking?

When dependencies are injected, tests can replace real services with fakes or mocks.

### 39. Can functions follow SOLID ideas?

Yes. Python design principles apply to functions and modules too, not only classes.

### 40. What is the best final interview summary?

Good Python design keeps code focused, simple, reusable where needed, easy to test, and flexible without unnecessary complexity.

## Final Interview Checklist

- Explain each SOLID letter clearly.
- Give one shopping-system example for every principle.
- Mention that Python uses duck typing and protocols often.
- Do not overuse inheritance.
- Prefer composition when behavior varies.
- Apply DRY carefully.
- Keep simple rules simple with KISS.
- Explain trade-offs, not just definitions.

## See also

- [Design principles: core concepts](core-concepts.md)
- [Design principles reference](design-principles-reference.md)
- [Design principles interview problems](interview-problems.md)
- [Python OOP](../oop/core-concepts.md)
- [Class relationships](../class-relationships/core-concepts.md)
