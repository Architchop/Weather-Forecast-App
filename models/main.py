from dataclasses import dataclass
from typing import Optional

@dataclass
class Main:
    """
    Model for Main data
    """
    
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: Optional[int] = None
    grnd_level: Optional[int] = None