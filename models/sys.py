from dataclasses import dataclass
from typing import Optional


@dataclass
class Sys:
    """
    Model for Sys data
    """
    
    country: str
    sunrise: int
    sunset: int
    type: Optional[int] = None
    id: Optional[int] = None