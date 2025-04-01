from dataclasses import dataclass
from typing import Optional

@dataclass
class Wind:
    """
    Model for Wind data
    """
    
    speed: float
    deg: int
    gust: Optional[float] = None