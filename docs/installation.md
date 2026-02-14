# Installation Guide

## Basic Installation

You can install `authkey-sdk` from PyPI using `pip`:

```bash
pip install authkey-sdk
```

## System Dependencies

`authkey-sdk` depends on `fido2`, which uses HID communication. This may require system-level dependencies depending on your OS.

### Linux

On Linux, you generally need `libusb` and appropriate `udev` rules to allow your user to access HID devices without `sudo`.

1. **Install libusb**:
   ```bash
   sudo apt-get install libusb-1.0-0-dev
   ```

2. **Add udev rules**:
   You can find standard udev rules from the [Yubico](https://github.com/Yubico/libu2f-host/blob/master/70-u2f.rules) or [Nitrokey](https://github.com/Nitrokey/nitrokey-udev-rules) projects.

### Windows

On Windows, no extra drivers are usually required as the Windows HID driver is used. However, ensure you are running with appropriate permissions if you encounter "Access Denied" errors.

### macOS

No additional configuration is typically needed for macOS.

## Troubleshooting

### "Device Not Found"
- Ensure the security key is plugged in.
- Check if another application (like a browser or another WebAuthn client) is hogging the device.
- On Linux, verify your `udev` rules.

### "Access Denied"
- On Linux, this is a clear sign of missing `udev` rules.
- On Windows, try running your script in a shell with elevated permissions only if necessary for debugging.
