# Copyright (c) 2026 authkey
# Licensed under the MIT License

"""
authkey - A professional Python library for FIDO2 Security Keys.
"""

from .client import SecurityKeyClient
from .models import Credential, Assertion
from .exceptions import SecureKeyError, DeviceNotFoundError, AuthenticationError

__all__ = [
    "SecurityKeyClient",
    "Credential",
    "Assertion",
    "SecureKeyError",
    "DeviceNotFoundError",
    "AuthenticationError",
]

__version__ = "0.1.0"
