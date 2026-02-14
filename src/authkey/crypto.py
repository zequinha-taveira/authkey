import hmac
import secrets

def constant_time_compare(val1: bytes, val2: bytes) -> bool:
    """
    Compare two byte strings in constant time to prevent timing attacks.
    """
    return hmac.compare_digest(val1, val2)

def generate_challenge(length: int = 32) -> bytes:
    """
    Generate a cryptographically secure random challenge.
    """
    return secrets.token_bytes(length)
