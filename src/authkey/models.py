# Copyright (c) 2026 authkey
# Licensed under the MIT License

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Credential:
    """Represents a registered FIDO2 credential."""
    credential_id: bytes
    public_key: bytes
    aaguid: Optional[bytes] = None

@dataclass(frozen=True)
class Assertion:
    """Represents a signature from a FIDO2 security key."""
    signature: bytes
    authenticator_data: bytes
    client_data_hash: bytes
    user_handle: Optional[bytes] = None
