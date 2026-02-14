# Copyright (c) 2026 authkey
# Licensed under the MIT License

"""
authkey - A professional Python library for FIDO2 Security Keys.
"""

from .client import SecurityKeyClient
from .exceptions import AuthenticationError, DeviceNotFoundError, SecureKeyError
from .models import Assertion, Credential

__all__ = [
    "SecurityKeyClient",
    "Credential",
    "Assertion",
    "SecureKeyError",
    "DeviceNotFoundError",
    "AuthenticationError",
]

__version__ = "0.1.0"
