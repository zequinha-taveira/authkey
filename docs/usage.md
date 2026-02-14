# Usage Guide

This guide provides examples of how to common tasks with `authkey-sdk`.

## Initialize the Client

The client requires a Relying Party (RP) ID, which is usually the domain name of your website.

```python
from authkey import SecurityKeyClient

client = SecurityKeyClient(rp_id="example.com")
```

## Device Discovery

You can list all connected FIDO2 security keys:

```python
devices = client.list_devices()
print(f"Found {len(devices)} security keys.")
```

## Credential Registration

To register a new security key for a user:

```python
try:
    credential = client.register(user_id="user_123", user_name="alice")
    print(f"New credential ID: {credential.credential_id.hex()}")
except Exception as e:
    print(f"Registration failed: {e}")
```

## Authentication

To authenticate an existing user using their credential ID:

```python
try:
    assertion = client.authenticate(credential_id=stored_cred_id)
    print("Authentication successful!")
    print(f"Signature: {assertion.signature.hex()}")
except Exception as e:
    print(f"Authentication failed: {e}")
```

## Error Handling

`authkey-sdk` provides specific exceptions for common failures:

```python
from authkey.exceptions import DeviceNotFoundError, RegistrationError

try:
    client.register(user_id="test")
except DeviceNotFoundError:
    print("Please plug in your security key!")
except RegistrationError as e:
    print(f"Security key error: {e}")
```
