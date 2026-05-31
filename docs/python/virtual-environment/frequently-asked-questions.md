# Python Virtual Environments: Frequently Asked Interview Questions

## Basic Level

### 1. What is a virtual environment?

A virtual environment is an isolated Python environment for a project.

### 2. Why use a virtual environment?

It prevents dependency conflicts between projects.

### 3. Which built-in module creates virtual environments?

`venv`.

### 4. How do you create a virtual environment?

```bash
python -m venv .venv
```

### 5. How do you activate it on macOS or Linux?

```bash
source .venv/bin/activate
```

### 6. How do you activate it on Windows?

```bash
.venv\Scripts\activate
```

### 7. How do you deactivate it?

```bash
deactivate
```

### 8. What is `.venv`?

A common folder name for a project virtual environment.

### 9. Should `.venv` be committed?

No. It should be ignored.

### 10. What should be committed instead?

Commit dependency files such as `requirements.txt`.

## Intermediate Level

### 11. How do you install packages inside a virtual environment?

Activate it, then run `python -m pip install package`.

### 12. How do you confirm the active Python?

Use `which python` on macOS/Linux or `where python` on Windows.

### 13. What is the difference between `venv` and `pip`?

`venv` creates isolated environments. `pip` installs packages.

### 14. What is the difference between `.venv` and `requirements.txt`?

`.venv` is a generated environment. `requirements.txt` is a dependency list.

### 15. Why can a package fail to import after installation?

It may have been installed into a different Python environment.

### 16. How do you recreate a virtual environment?

Create a new `.venv`, activate it, and run `pip install -r requirements.txt`.

### 17. Can each project have its own environment?

Yes. That is the recommended approach.

### 18. Does activation install packages?

No. Activation only selects the environment.

### 19. Does `deactivate` delete the environment?

No. It only exits the environment in the current shell.

### 20. How do you remove a virtual environment?

Delete the environment folder, such as `.venv`.

## Advanced Level

### 21. Why use `python -m venv` instead of a random tool?

It is built into Python and works for standard project isolation.

### 22. Why use `python -m pip` inside a venv?

It guarantees pip belongs to the active Python interpreter.

### 23. What happens if two projects need different package versions?

Separate virtual environments allow each project to use its own version.

### 24. Should production deploy `.venv` from a developer machine?

Usually no. Production should build/install dependencies in its own environment.

### 25. What belongs in `.gitignore`?

Virtual environment folders like `.venv/`, `venv/`, and `env/`.

### 26. What is a common interview mistake?

Saying `requirements.txt` isolates dependencies. It documents dependencies; the virtual environment isolates them.

### 27. What is an activation script?

A script that changes shell variables so `python` and `pip` point to the environment.

### 28. Can you use a virtual environment without activation?

Yes, by running its Python executable directly, but activation is simpler for daily work.

### 29. How is this useful in a shopping app?

The API, reports, and tests can keep independent dependency versions.

### 30. What should you remember?

Create per-project environments, install with `python -m pip`, commit dependency files, and ignore `.venv/`.

## See also

- [Python virtual environments: core concepts](core-concepts.md)
- [Python virtual environment reference](virtual-environment-reference.md)
- [Python virtual environment interview problems](interview-problems.md)
- [Python pip: core concepts](../pip/core-concepts.md)
