# authkey-sdk

A professional Python library for interacting with FIDO2 Security Keys (hardware tokens).

## Features

- 🔌 **Device Discovery**: Automatically detect HID-based FIDO2 security keys.
- 🔐 **Registration**: Simple API for `makeCredential` (WebAuthn Registration).
- ✍️ **Authentication**: Easy assertion signing for `getAssertion` (WebAuthn Login).
- 🧠 **Robust Error Handling**: Clear exceptions instead of vague return values.
- 🛡 **Security Focused**: Built with threat modeling and secure coding practices.

## Installation

```bash
pip install authkey-sdk
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

## License

MIT
