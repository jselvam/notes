# Python Virtual Environment Interview Problems

## 1. Create and Activate a Virtual Environment

### Problem

Set up an isolated environment for a shopping API project.

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

## 2. Install Project Dependencies

```bash
python -m pip install requests pytest
```

Use this after activation so dependencies install inside `.venv`.

## 3. Save Dependencies

```bash
python -m pip freeze > requirements.txt
```

Commit `requirements.txt` so teammates can install the same dependencies.

## 4. Recreate a Project Environment

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

This is a common setup flow after cloning a repository.

## 5. Fix Package Installed in Wrong Python

```bash
which python
python -m pip --version
python -m pip show requests
```

If `Location` is outside `.venv`, the wrong environment may be active.

## 6. Explain Why `.venv` Should Not Be Committed

`.venv` contains generated, machine-specific files and installed packages. Commit `requirements.txt` instead.

## 7. Use Different Dependencies Per Project

```text
shopping-api/.venv      -> fastapi, pydantic v2
legacy-report/.venv     -> pandas, pydantic v1
```

Separate environments avoid dependency conflicts.

## 8. Deactivate an Environment

```bash
deactivate
```

This returns the shell to the normal Python environment.

## 9. Upgrade pip Inside a Virtual Environment

```bash
python -m pip install --upgrade pip
```

Do this after activation so only the environment's pip is upgraded.

## 10. Add venv to `.gitignore`

```text
.venv/
venv/
env/
```

This prevents accidentally committing environment files.

## Summary

| Problem pattern | Command or idea |
|-----------------|-----------------|
| isolate project | `python -m venv .venv` |
| activate | `source .venv/bin/activate` |
| install packages | `python -m pip install ...` |
| share setup | `requirements.txt` |
| leave environment | `deactivate` |
| avoid repo noise | ignore `.venv/` |

## See also

- [Python virtual environments: core concepts](core-concepts.md)
- [Python virtual environment reference](virtual-environment-reference.md)
- [Python virtual environment FAQ](frequently-asked-questions.md)
