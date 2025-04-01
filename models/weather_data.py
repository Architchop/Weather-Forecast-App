from dataclasses import dataclass
from typing import List, Optional

from models.clouds import Clouds
from models.main import Main
from models.sys import Sys
from models.weather import Weather
from models.wind import Wind

@dataclass
class WeatherData:
    """
    Model for Weather API Response
    """
    
    weather: List[Weather]
    main: Main
    wind: Wind
    clouds: Clouds
    sys: Sys
    name: str

    @staticmethod
    def from_dict(data: dict):
        return WeatherData(
            weather=[Weather(**w) for w in data["weather"]],
            main=Main(**data["main"]),
            wind=Wind(**data["wind"]),
            clouds=Clouds(**data["clouds"]),
            sys=Sys(**data["sys"]),
            name=data["name"],
        )