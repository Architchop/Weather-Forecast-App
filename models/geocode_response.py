from dataclasses import dataclass

@dataclass
class GeoCodeResponse:
    """
    Model for GetoCode API response
    """
    
    lat: float
    lon: float

    @staticmethod
    def from_dict(data: dict):
        if(len(data) == 0):
            return None
        return GeoCodeResponse(
            lat=data[0]["lat"],
            lon=data[0]["lon"]
        )