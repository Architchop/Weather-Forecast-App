from dataclasses import dataclass


@dataclass
class Weather:
    """
    Model for Weather data
    """
    
    id: int
    main: str
    description: str
    icon: str