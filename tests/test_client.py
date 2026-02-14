import pytest
from authkey import SecurityKeyClient
from authkey.exceptions import DeviceNotFoundError

def test_client_init():
    """Test that the client initializes correctly with an RP ID."""
    client = SecurityKeyClient(rp_id="example.com")
    assert client.rp_id == "example.com"

def test_client_discovery_no_devices():
    """Test that searching for devices returns empty or raises expected error if no hardware present."""
    client = SecurityKeyClient(rp_id="example.com")
    # This might raise DeviceNotFoundError or return an empty list depending on implementation
    # We'll assert it doesn't crash
    try:
        devices = client.list_devices()
        assert isinstance(devices, list)
    except DeviceNotFoundError:
        pass
