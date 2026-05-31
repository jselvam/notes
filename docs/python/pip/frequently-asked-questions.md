# Python pip: Frequently Asked Interview Questions

## Basic Level

### 1. What is pip?

`pip` is Python's package installer.

### 2. What does pip install?

It installs Python packages from indexes such as PyPI.

### 3. What is PyPI?

PyPI is the Python Package Index, a public repository of Python packages.

### 4. How do you check pip version?

```bash
python -m pip --version
```

### 5. How do you install a package?

```bash
python -m pip install requests
```

### 6. How do you uninstall a package?

```bash
python -m pip uninstall requests
```

### 7. How do you list installed packages?

```bash
python -m pip list
```

### 8. How do you show package details?

```bash
python -m pip show requests
```

### 9. Why use `python -m pip`?

It ensures `pip` runs with the intended Python interpreter.

### 10. What is `requirements.txt`?

A text file that lists project dependencies.

## Intermediate Level

### 11. How do you install from `requirements.txt`?

```bash
python -m pip install -r requirements.txt
```

### 12. How do you create `requirements.txt`?

```bash
python -m pip freeze > requirements.txt
```

### 13. What is the difference between `pip list` and `pip freeze`?

`pip list` is human-readable. `pip freeze` is formatted for requirements files.

### 14. How do you install an exact version?

```bash
python -m pip install "requests==2.32.0"
```

### 15. How do you upgrade a package?

```bash
python -m pip install --upgrade requests
```

### 16. How do you check dependency conflicts?

```bash
python -m pip check
```

### 17. Why should pip be used inside a virtual environment?

It keeps dependencies isolated per project.

### 18. What happens if you install globally?

Different projects can accidentally share and break each other's dependencies.

### 19. Why can import fail after pip install?

The package may have been installed into a different Python interpreter.

### 20. What is a pinned dependency?

A dependency fixed to an exact version, such as `pytest==8.0.0`.

## Advanced Level

### 21. What is a dependency conflict?

Two packages require incompatible versions of another package.

### 22. What is a transitive dependency?

A package installed because another package depends on it.

### 23. Should you commit a virtual environment folder?

No. Commit dependency files, not the environment folder.

### 24. Should you always commit `requirements.txt`?

For simple pip-based projects, yes, because it documents setup dependencies.

### 25. What is an editable install?

`pip install -e .` installs a local project so code changes are reflected immediately.

### 26. What is a package wheel?

A wheel is a built package distribution format that installs quickly.

### 27. What is the difference between package and module?

A package is distributable or importable code; a module is a Python file.

### 28. What is a common pip interview mistake?

Using plain `pip` without confirming which Python interpreter it belongs to.

### 29. What should you do after upgrading dependencies?

Run tests and update dependency files if the upgrade is accepted.

### 30. What should you remember?

Use `python -m pip`, work inside a virtual environment, pin important versions, and keep dependency files updated.

## See also

- [Python pip: core concepts](core-concepts.md)
- [Python pip reference](pip-reference.md)
- [Python pip interview problems](interview-problems.md)
- [Python virtual environments: core concepts](../virtual-environment/core-concepts.md)
