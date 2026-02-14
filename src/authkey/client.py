# Copyright (c) 2026 authkey
# Licensed under the MIT License

import secrets
from typing import Optional

from fido2.client import Fido2Client

from .device import get_first_device, list_devices
from .exceptions import AuthenticationError, RegistrationError
from .models import Assertion, Credential


class SecurityKeyClient:
    """
    Main client for interacting with a FIDO2 Security Key.

    This client provides a high-level API for discovering FIDO2 devices,
    registering new credentials, and performing authentication.

    Attributes:
        rp_id (str): Relying Party ID (usually the domain name).
        rp_name (str): Display name for the Relying Party.
        origin (str): Origin URL derived from the rp_id.
    """

    def __init__(self, rp_id: str, rp_name: Optional[str] = None):
        """
        Initialize the client.
        
        Args:
            rp_id: Relying Party ID (e.g., "example.com").
            rp_name: Display name for the Relying Party.
        """
        self.rp_id = rp_id
        self.rp_name = rp_name or rp_id
        self.origin = f"https://{rp_id}"
        
        # In a real scenario, we might want to delay device connection
        self._device = None
        self._client = None

    def _get_client(self) -> Fido2Client:
        if self._client is None:
            self._device = get_first_device()
            self._client = Fido2Client(self._device, self.origin)
        return self._client

    @staticmethod
    def list_devices():
        """
        List all connected FIDO2 HID devices.

        Returns:
            list[CtapHidDevice]: A list of discovered CTAP HID devices.
        """
        return list_devices()

    def register(self, user_id: str, user_name: Optional[str] = None) -> Credential:
        """
        Register a new credential on the security key (FIDO2 makeCredential).

        Args:
            user_id: Unique identifier for the user (e.g., a database UUID).
            user_name: Friendly name for the user (e.g., "alice@example.com").

        Returns:
            Credential: A container for the newly created credential ID and public key.

        Raises:
            DeviceNotFoundError: If no security key is connected.
            RegistrationError: If the hardware registration process fails.
        """
        user_name = user_name or user_id
        challenge = secrets.token_bytes(32)
        client = self._get_client()

        try:
            options, state = client.make_credential({
                "publicKey": {
                    "rp": {"id": self.rp_id, "name": self.rp_name},
                    "user": {
                        "id": user_id.encode(),
                        "name": user_name,
                        "displayName": user_name
                    },
                    "challenge": challenge,
                    "pubKeyCredParams": [{"type": "public-key", "alg": -7}] # ES256
                }
            })

            attestation = client.make_credential_complete(state, options)

            return Credential(
                credential_id=attestation.credential_id,
                public_key=attestation.public_key,
                aaguid=attestation.auth_data.aaguid
            )
        except Exception as e:
            raise RegistrationError(f"Failed to register credential: {e}") from e

    def authenticate(self, credential_id: bytes) -> Assertion:
        """
        Authenticate using an existing credential (FIDO2 getAssertion).

        Args:
            credential_id: The raw bytes of the credential ID to use for signing.

        Returns:
            Assertion: The signed assertion including signature and authenticator data.

        Raises:
            DeviceNotFoundError: If no security key is connected.
            AuthenticationError: If the hardware signing process fails.
        """
        challenge = secrets.token_bytes(32)
        client = self._get_client()

        try:
            assertion, _ = client.get_assertion({
                "publicKey": {
                    "challenge": challenge,
                    "rpId": self.rp_id,
                    "allowCredentials": [{
                        "type": "public-key",
                        "id": credential_id
                    }]
                }
            })

            # Get the first response (index 0)
            result = assertion.get_response(0)

            return Assertion(
                signature=result.signature,
                authenticator_data=result.authenticator_data,
                client_data_hash=assertion.client_data.hash,
                user_handle=result.user_handle
            )
        except Exception as e:
            raise AuthenticationError(f"Failed to authenticate: {e}") from e
