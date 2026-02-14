# Copyright (c) 2026 authkey
# Licensed under the MIT License

"""
Internal transport abstractions for authkey.
"""

from fido2.hid import CtapHidDevice

def get_transport_info(device: CtapHidDevice) -> str:
    """Get basic info about the transport layer."""
    return f"USB HID: {device.descriptor}"
