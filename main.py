import sys
from datetime import datetime
from utils.geo_utils import GeoUtils
from utils.weather_utils import WeatherUtils
from utils.menu_utils import MenuUtils
from utils.configuration_manager import ConfigurationManager

if __name__ == "__main__":
    # Initializing required classes
    confg_manager = ConfigurationManager()
    geo_utils = GeoUtils(confg_manager)
    weather_utils = WeatherUtils(confg_manager, geo_utils)
    menu_utils = MenuUtils()

    # Welcome the user
    menu_utils.show_welcome_message()

    app_running = True
    # Run the app until the flag is true
    while app_running:
        # Take user input
        city = menu_utils.take_city_input()
        
        # Getting weather data
        weather = weather_utils.get_weather(city)

        if weather is None:
            # If data not found, let the user know
            print("Data not found!!")
        else:
            # Data Found, show details
            print(f"""
        Weather Status for - {weather.name}, {weather.sys.country}

        Status : {weather.weather[0].main}
        Temprature: {weather.main.temp} °C
        Feels Like: {weather.main.feels_like} °C
        Minimum Temprature: {weather.main.temp_min} °C
        Maximum Temprature: {weather.main.temp_max} °C
        Pressure: {weather.main.pressure} hPa
        Humidity: {weather.main.humidity} %
        Clouds: {weather.clouds.all} %
        Wind Speed: {weather.wind.deg} deg, {weather.wind.speed} m/s
        Sunrise: {datetime.fromtimestamp(weather.sys.sunrise)}
        Sunset: {datetime.fromtimestamp(weather.sys.sunset)}
        """)
        
        # Ask for further choice
        choice = input("Do you want to continue? (Y/N): ")
        if choice.lower() != "y":
            app_running = False
    
    # Exit the app with a mesage
    menu_utils.show_exit_message()
