# Project Instructions for Claude

## Project Overview

<!-- Briefly describe what this project does and its primary goals. -->

## Tech Stack

<!-- List the main technologies, frameworks, and languages used. -->
- Language: Python 3
- Testing: pytest
- Linting: ruff / flake8
- Formatting: black
- Dependency management: pip / pip-tools

## Development Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python -m <module_name>     # replace <module_name> with your package, e.g. python -m myapp

# Run tests
pytest

# Run tests with coverage
pytest --cov
```

## Common Commands

| Task   | Command                        |
|--------|--------------------------------|
| Test   | `pytest`                       |
| Lint   | `ruff check .` / `flake8 .`    |
| Format | `black .`                      |
| Type   | `mypy .`                       |

## Code Style & Conventions

- Follow PEP 8 style guidelines
- Use type hints for all public functions and methods
- Co-locate test files under `tests/` using the `test_<module>.py` naming convention
- <!-- e.g. API responses follow `{ data, error }` shape -->

## Repository Structure

```
src/           # Application source code
tests/         # Test files (test_*.py)
docs/          # Documentation
.claude/       # Claude Code configuration
```

## Important Notes

<!-- Add any constraints, gotchas, or context Claude should always be aware of. -->
