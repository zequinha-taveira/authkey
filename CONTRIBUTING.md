# Contributing to authkey-sdk

Thank you for your interest in contributing to `authkey-sdk`! We welcome all contributions, from bug reports and feature requests to code changes and documentation improvements.

## How to Contribute

### Reporting Bugs
If you find a bug, please search existing issues to see if it has already been reported. If not, open a new issue with:
- A clear, descriptive title.
- Steps to reproduce the issue.
- Expected and actual results.
- Your environment details (OS, Python version, device model).

### Suggesting Enhancements
We love new ideas! To suggest an enhancement:
- Check if it's already been proposed.
- Open an issue describing the feature and why it would be useful.

### Pull Requests
1. Fork the repository.
2. Create a new branch for your changes (`git checkout -b feature/awesome-feature`).
3. Make your changes, following the [Coding Standards](#coding-standards).
4. Run tests to ensure everything is working: `pytest tests/`.
5. Submit a pull request with a clear description of your changes.

## Coding Standards

- **Style**: We use [Ruff](https://github.com/astral-sh/ruff) for linting and formatting.
- **Types**: All public APIs should have type hints.
- **Tests**: New features should include unit tests.
- **Documentation**: Updatedocstrings and the README if necessary.

## Development Setup

```bash
# Clone the repo
git clone https://github.com/authkey/authkey-sdk.git
cd authkey-sdk

# Install in editable mode with development dependencies
pip install -e ".[dev]"
```

## Community

Please adhere to our [Code of Conduct](CODE_OF_CONDUCT.md) in all interactions.
