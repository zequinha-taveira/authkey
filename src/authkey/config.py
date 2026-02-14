# Copyright (c) 2026 authkey
# Licensed under the MIT License

from dataclasses import dataclass


@dataclass

class Config:
    """Library configuration options."""
    default_timeout: int = 30 # Seconds
    allow_unprotected_uv: bool = False
    
DEFAULT_CONFIG = Config()
