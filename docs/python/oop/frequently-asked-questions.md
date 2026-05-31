# Python OOP: Frequently Asked Interview Questions

## Basic Level

### 1. What does OOP stand for?

OOP stands for Object-Oriented Programming.

### 2. What is a class?

A class is a blueprint for creating objects.

### 3. What is an object?

An object is an instance of a class.

### 4. What is an attribute?

An attribute is data stored on an object or class.

### 5. What is a method?

A method is a function defined inside a class.

### 6. What is `self`?

`self` refers to the current object instance.

### 7. What is `__init__()`?

`__init__()` initializes a new object after it is created.

### 8. Is `__init__()` a constructor?

It is commonly called a constructor in interviews, but technically `__new__()` creates the object and `__init__()` initializes it.

### 9. How do you create an object?

```python
product = Product("Laptop", 999.99)
```

### 10. Why use OOP?

OOP organizes related data and behavior, making code easier to model, reuse, and maintain.

## Intermediate Level

### 11. What are the four pillars of OOP?

Encapsulation, inheritance, polymorphism, and abstraction.

### 12. What is encapsulation?

Encapsulation keeps data and related behavior together in a class.

### 13. What is inheritance?

Inheritance lets one class reuse or extend another class.

### 14. What is polymorphism?

Polymorphism allows different objects to respond to the same method name in different ways.

### 15. What is abstraction?

Abstraction hides internal details and exposes a simpler interface.

### 16. What is method overriding?

A child class provides its own version of a parent class method.

### 17. What is a class attribute?

A class attribute is shared by all instances of a class.

### 18. What is an instance attribute?

An instance attribute belongs to one object.

### 19. What is composition?

Composition means one object contains or uses another object.

### 20. What is `@property`?

`@property` makes a method accessible like an attribute.

## Advanced Level

### 21. Is Python object-oriented?

Yes. Python supports OOP, but it also supports procedural and functional styles.

### 22. What is multiple inheritance?

Multiple inheritance means a class inherits from more than one parent class.

### 23. What is MRO?

MRO stands for Method Resolution Order. It decides where Python looks for methods in inheritance chains.

### 24. What is `super()`?

`super()` calls methods from a parent or next class in the MRO.

### 25. What is the difference between inheritance and composition?

Inheritance models an is-a relationship. Composition models a has-a relationship.

### 26. When should you prefer composition?

Prefer composition when you only need to use another object's behavior instead of saying one class is a specialized version of another.

### 27. What is duck typing?

Duck typing means Python cares about what methods an object has, not strictly what class it belongs to.

### 28. What is a magic method?

A magic method is a special method with double underscores, such as `__init__`, `__str__`, or `__len__`.

### 29. What is a common OOP interview mistake?

Overusing inheritance when simple composition or functions would be clearer.

### 30. What should you remember?

Know class, object, attributes, methods, `self`, `__init__`, encapsulation, inheritance, polymorphism, abstraction, and composition.

## Final Interview Checklist

- Class is a blueprint; object is an instance.
- Attributes store data; methods define behavior.
- `self` refers to the current object.
- `__init__()` initializes object state.
- Encapsulation keeps data and behavior together.
- Inheritance reuses parent behavior.
- Polymorphism enables common interfaces.
- Abstraction hides details.
- Composition is often simpler than inheritance.

## See also

- [Python OOP: core concepts](core-concepts.md)
- [Python OOP reference](oop-reference.md)
- [Python OOP interview problems](interview-problems.md)
