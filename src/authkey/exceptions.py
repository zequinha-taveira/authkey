# Copyright (c) 2026 authkey
# Licensed under the MIT License

class SecureKeyError(Exception):
    """Base exception for all authkey errors."""
    pass

class DeviceNotFoundError(SecureKeyError):
    """Raised when no compatible security key is found."""
    pass

class AuthenticationError(SecureKeyError):
    """Raised when authentication fails (e.g., invalid signature)."""
    pass

class RegistrationError(SecureKeyError):
    """Raised when registration fails."""
    pass

class TimeoutError(SecureKeyError):
    """Raised when an operation times out (e.g., user didn't touch the key)."""
    pass
