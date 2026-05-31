# Python pip Reference

## Quick Command Table

| Command | Meaning |
|---------|---------|
| `python -m pip --version` | Show pip version |
| `python -m pip install package` | Install package |
| `python -m pip install "package==version"` | Install exact version |
| `python -m pip install --upgrade package` | Upgrade package |
| `python -m pip uninstall package` | Remove package |
| `python -m pip list` | List installed packages |
| `python -m pip show package` | Show package details |
| `python -m pip freeze` | Print pinned dependencies |
| `python -m pip install -r requirements.txt` | Install from dependency file |

## Install Packages

```bash
python -m pip install requests
python -m pip install pytest
python -m pip install mkdocs
```

## Install Multiple Packages

```bash
python -m pip install requests pydantic pytest
```

## Pin Versions

```bash
python -m pip install "fastapi==0.115.0"
python -m pip install "requests>=2.31,<3"
```

Version pins help prevent unexpected behavior after dependency upgrades.

## Requirements File

Example `requirements.txt`:

```text
requests==2.32.0
pytest==8.0.0
mkdocs==1.6.0
```

Install it:

```bash
python -m pip install -r requirements.txt
```

## Show Package Metadata

```bash
python -m pip show requests
```

This shows version, location, dependencies, and package metadata.

## Check Dependency Problems

```bash
python -m pip check
```

## Use pip Inside a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install requests
```

On Windows:

```bash
.venv\Scripts\activate
python -m pip install requests
```

## Common Interview Comparisons

| Topic | Key point |
|-------|-----------|
| `pip install` vs `pip freeze` | install adds packages; freeze records installed versions |
| `requirements.txt` vs virtual environment | requirements is a file; venv is an isolated environment |
| global pip vs venv pip | venv pip avoids polluting system Python |
| `pip list` vs `pip freeze` | list is human-friendly; freeze is requirements-friendly |

## See also

- [Python pip: core concepts](core-concepts.md)
- [Python pip interview problems](interview-problems.md)
- [Python pip FAQ](frequently-asked-questions.md)
