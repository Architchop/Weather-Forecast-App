import requests
import orjson
from models.geocode_response import GeoCodeResponse

class GeoUtils:
    """
    Get Latitude and Longitude of a city based on the name
    """
    
    def __init__(self, config_manager):
        self.config_manager = config_manager

    def get_lat_lon(self, city):
        # Prepare the geo code api url
        url = f"{self.config_manager.geocode_base_url}?q={city}&limit=1&appid={self.config_manager.api_key}"

        # Get the response from the api
        response = requests.get(url)
        if response.status_code == 200:
            # data Found, return the GeoCodeResponse object
            data = orjson.loads(response.content)
            return GeoCodeResponse.from_dict(data)
        else:
            # Not found, or error then return None
            return None
