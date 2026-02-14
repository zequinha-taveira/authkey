# Release Guide

This guide outlines the process for releasing a new version of `authkey-sdk` to PyPI.

## Prerequisites

- Access to the `authkey-sdk` project on PyPI.
- `build` and `twine` installed in your environment.

## Step-by-Step Release

### 1. Update Version
Bump the version in `pyproject.toml`:
```toml
[project]
version = "0.1.1" # Example bump
```

### 2. Update Changelog
Add the new version and its changes to `CHANGELOG.md`.

### 3. Run Tests
Ensure everything is passing:
```bash
pytest tests/
```

### 4. Build the Package
```bash
python -m build
```

### 5. Upload to PyPI
First, upload to TestPyPI to verify:
```bash
python -m twine upload --repository testpypi dist/*
```
If everything looks good, upload to the real PyPI:
```bash
python -m twine upload dist/*
```

### 6. Create a Git Tag
```bash
git tag -a v0.1.1 -m "Version 0.1.1"
git push origin v0.1.1
```
