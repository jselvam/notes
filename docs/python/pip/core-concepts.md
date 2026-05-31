# Python pip: Core Concepts

`pip` is Python's package installer. It installs third-party packages from package indexes such as PyPI.

In an online computer shopping project, `pip` can install packages for:

- web APIs such as `fastapi` or `flask`
- database access such as `sqlalchemy`
- data validation such as `pydantic`
- testing such as `pytest`
- documentation such as `mkdocs`
- HTTP calls such as `requests`

## Check pip Version

```bash
python -m pip --version
```

Prefer `python -m pip` because it uses the `pip` that belongs to the selected Python interpreter.

## Install a Package

```bash
python -m pip install requests
```

Example use:

```python
import requests

response = requests.get("https://example.com/products")
print(response.status_code)
```

## Install a Specific Version

```bash
python -m pip install "requests==2.32.0"
```

## Upgrade a Package

```bash
python -m pip install --upgrade requests
```

## Uninstall a Package

```bash
python -m pip uninstall requests
```

## List Installed Packages

```bash
python -m pip list
```

## Freeze Dependencies

```bash
python -m pip freeze > requirements.txt
```

`requirements.txt` records package versions so another developer can recreate the same environment.

## Install From Requirements

```bash
python -m pip install -r requirements.txt
```

## Common Gotchas

### Global installs can conflict

Installing packages globally can mix dependencies from many projects. Use a virtual environment for each project.

### `pip` may point to a different Python

Use `python -m pip` to avoid installing into the wrong interpreter.

### `requirements.txt` is not the same as a virtual environment

`requirements.txt` is a dependency list. A virtual environment is an isolated Python environment.

## Practice Problems

1. Check the installed `pip` version.
2. Install `requests`.
3. Freeze dependencies into `requirements.txt`.
4. Install dependencies from `requirements.txt`.
5. Explain why `python -m pip` is safer than plain `pip`.

## See also

- [Python pip reference](pip-reference.md)
- [Python pip interview problems](interview-problems.md)
- [Python pip FAQ](frequently-asked-questions.md)
- [Python virtual environments: core concepts](../virtual-environment/core-concepts.md)
