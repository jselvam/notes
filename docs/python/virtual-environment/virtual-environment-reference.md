# Python Virtual Environment Reference

## Quick Command Table

| Task | macOS/Linux | Windows |
|------|-------------|---------|
| Create venv | `python -m venv .venv` | `python -m venv .venv` |
| Activate | `source .venv/bin/activate` | `.venv\Scripts\activate` |
| Deactivate | `deactivate` | `deactivate` |
| Check Python | `which python` | `where python` |
| Install package | `python -m pip install requests` | `python -m pip install requests` |
| Freeze deps | `python -m pip freeze > requirements.txt` | `python -m pip freeze > requirements.txt` |
| Install deps | `python -m pip install -r requirements.txt` | `python -m pip install -r requirements.txt` |

## Standard Setup Flow

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Create a New Project Environment

```bash
mkdir shopping-api
cd shopping-api
python -m venv .venv
source .venv/bin/activate
python -m pip install fastapi uvicorn pytest
python -m pip freeze > requirements.txt
```

## Rebuild an Existing Environment

```bash
rm -rf .venv
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## `.gitignore`

Add virtual environment folders to `.gitignore`.

```text
.venv/
venv/
env/
__pycache__/
```

## Confirm Package Location

```bash
python -m pip show requests
```

Check `Location` to confirm the package is installed inside `.venv`.

## Common Interview Comparisons

| Topic | Key point |
|-------|-----------|
| virtual environment vs system Python | venv isolates dependencies |
| `venv` vs `pip` | `venv` creates isolation; `pip` installs packages |
| `.venv` vs `requirements.txt` | `.venv` is generated; requirements file is committed |
| activation vs installation | activation selects environment; pip installs dependencies |

## See also

- [Python virtual environments: core concepts](core-concepts.md)
- [Python virtual environment interview problems](interview-problems.md)
- [Python virtual environment FAQ](frequently-asked-questions.md)
