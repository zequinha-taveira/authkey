# authkey-sdk

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

A professional, vendor-neutral Python library for interacting with FIDO2 Security Keys (hardware tokens).

## Features

- 🔌 **Device Discovery**: Automatically detect HID-based FIDO2 security keys.
- 🔐 **Registration**: Simple API for `makeCredential` (WebAuthn Registration).
- ✍️ **Authentication**: Easy assertion signing for `getAssertion` (WebAuthn Login).
- 🧠 **Robust Error Handling**: Clear exceptions instead of vague return values.
- 🛡 **Security Focused**: Built with threat modeling and secure coding practices.


## Installation

Install the stable version from PyPI:

```bash
pip install authkey-sdk
```

> [!NOTE]
> `authkey-sdk` requires a working installation of `libusb` or `udev` rules on Linux for HID communication.

### Development Setup

```bash
git clone https://github.com/authkey/authkey-sdk.git
cd authkey-sdk
pip install -e ".[dev,test]"
```


## Quick Start

```python
from authkey import SecurityKeyClient

# Initialize client for your Relying Party ID
client = SecurityKeyClient(rp_id="example.com")

# Register a new credential
credential = client.register(user_id="user_123")
print(f"Registered: {credential.credential_id.hex()}")

# Authenticate
assertion = client.authenticate(credential.credential_id)
print(f"Authenticated with signature: {assertion.signature.hex()}")
```

## Documentation

For more detailed information, check out:
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [SECURITY.md](SECURITY.md)
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

## License

MIT - See the [LICENSE](LICENSE) file for details.

