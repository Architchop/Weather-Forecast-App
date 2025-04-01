import requests
import orjson
from models.weather_data import WeatherData

class WeatherUtils:
    """
    Utils for getting the weather data
    Internally make use of geo_utils to get the latitude and longitude of the city by name
    """
    
    def __init__(self, config_manager, geo_utils):
        self.config_manager = config_manager
        self.geo_utils = geo_utils

    def get_weather(self, city):
        # Gets the latitude and longitude of the city by name
        geo_data = self.geo_utils.get_lat_lon(city)
        if geo_data is None:
            # If not found, return None
            return None
        
        # Prepare URL for the weather data
        url = f"{self.config_manager.base_url}?lat={geo_data.lat}&lon={geo_data.lon}&appid={self.config_manager.api_key}&units=metric"
    
        response = requests.get(url)
        if response.status_code == 200:
            # data Found, return the WeatherData object
            data = orjson.loads(response.content)
            return WeatherData.from_dict(data)
        else:
            # Not found, or error then return None
            return None
