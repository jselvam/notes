# Python pip Interview Problems

## 1. Install a Package for API Calls

### Problem

Install `requests` for calling a product API.

```bash
python -m pip install requests
```

```python
import requests

response = requests.get("https://example.com/products")
print(response.status_code)
```

## 2. Install an Exact Package Version

```bash
python -m pip install "requests==2.32.0"
```

Use exact versions when a project must be reproducible.

## 3. Create a Requirements File

```bash
python -m pip freeze > requirements.txt
```

This records installed package versions for the current environment.

## 4. Install Project Dependencies

```bash
python -m pip install -r requirements.txt
```

Use this when setting up the shopping project on a new machine.

## 5. Check Installed Package Version

```bash
python -m pip show requests
```

This helps debug version-related issues.

## 6. Upgrade a Dependency

```bash
python -m pip install --upgrade requests
```

After upgrading, run tests because behavior can change.

## 7. Uninstall an Unused Package

```bash
python -m pip uninstall requests
```

Use this to remove unused dependencies from a project environment.

## 8. Debug Wrong pip Interpreter

```bash
python -m pip --version
which python
```

If a package installs but cannot be imported, `pip` may belong to a different Python.

## 9. Check Dependency Conflicts

```bash
python -m pip check
```

This reports broken or incompatible installed dependencies.

## 10. Explain Why Virtual Environments Matter

Global package installs can conflict between projects. A shopping API and a reporting script may need different versions of the same dependency, so each project should use its own virtual environment.

## Summary

| Problem pattern | pip command |
|-----------------|-------------|
| install dependency | `python -m pip install package` |
| exact version | `package==version` |
| recreate environment | `pip install -r requirements.txt` |
| record versions | `pip freeze > requirements.txt` |
| inspect package | `pip show package` |
| detect conflicts | `pip check` |

## See also

- [Python pip: core concepts](core-concepts.md)
- [Python pip reference](pip-reference.md)
- [Python pip FAQ](frequently-asked-questions.md)
