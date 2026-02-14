from typing import List
from fido2.hid import CtapHidDevice
from .exceptions import DeviceNotFoundError

def list_devices() -> List[CtapHidDevice]:
    """
    List all connected FIDO2 HID devices.
    """
    return list(CtapHidDevice.list_devices())

def get_first_device() -> CtapHidDevice:
    """
    Get the first available FIDO2 HID device.
    
    Raises:
        DeviceNotFoundError: If no FIDO2 device is found.
    """
    devices = list_devices()
    if not devices:
        raise DeviceNotFoundError("No FIDO2 security key found via USB HID.")
    return devices[0]
