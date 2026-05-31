# Python Virtual Environments: Core Concepts

A **virtual environment** is an isolated Python environment for one project. It keeps project dependencies separate from the system Python and from other projects.

In an online computer shopping system, a virtual environment helps keep dependencies for the shopping API, admin scripts, tests, and reports predictable.

## Why Use a Virtual Environment?

Without a virtual environment, installing packages globally can cause conflicts.

Example:

- shopping API needs `pydantic` version 2
- older reporting script needs `pydantic` version 1

Separate virtual environments allow both projects to work.

## Create a Virtual Environment

```bash
python -m venv .venv
```

`.venv` is a common folder name for the environment.

## Activate on macOS or Linux

```bash
source .venv/bin/activate
```

## Activate on Windows

```bash
.venv\Scripts\activate
```

## Confirm Activation

```bash
which python
python -m pip --version
```

On Windows:

```bash
where python
python -m pip --version
```

## Install Packages Inside the Environment

```bash
python -m pip install requests
```

## Save Dependencies

```bash
python -m pip freeze > requirements.txt
```

## Deactivate

```bash
deactivate
```

## Recreate an Environment

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## What to Commit

Commit:

- `requirements.txt`
- source code
- tests
- documentation

Do not commit:

- `.venv/`
- installed packages
- generated cache folders

## Common Gotchas

### Forgetting to activate

Packages may install globally or into another environment.

### Committing `.venv`

Virtual environments are machine-specific and can be large.

### Using the wrong Python version

Create the environment with the intended Python version.

## Practice Problems

1. Create a `.venv` folder.
2. Activate the environment.
3. Install `requests`.
4. Save dependencies to `requirements.txt`.
5. Explain why `.venv` should not be committed.

## See also

- [Python virtual environment reference](virtual-environment-reference.md)
- [Python virtual environment interview problems](interview-problems.md)
- [Python virtual environment FAQ](frequently-asked-questions.md)
- [Python pip: core concepts](../pip/core-concepts.md)
