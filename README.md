# Description

A study of the OOP design patterns described in the ["Design Patterns: Elements of Reusable Object-Oriented Software"](https://en.wikipedia.org/wiki/Design_Patterns)
aka the Gang of Four book.

Additionally, SOLID principles are demonstrated:

- S: Single Responsibility Principle states that a class should have one reason to change.
- O: Open/Closed Principle states that a class should be open to extension but closed to change.
- L: Liskov Substitution Principle states that a child class should be interchangeable with the parent without breaking the program's correctness or expected behavior.
- I: Interface Segregation Principle statest that interfaces shouldn't be thick, i.e. they should be focused on one thing.
- D: Dependency Inversion Principle statest that higher-level modules should depend on an interface, and not call lower-level modules directly.

# Installation

- Install poetry: `curl -sSL https://install.python-poetry.org | python3 -`
- Install dependencies: `poetry install`

# Running Tests

`poetry run pytest`
