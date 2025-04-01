import orjson

class ConfigurationManager:
    """
    Loads the data from config.json file to class variables
    """

    def __init__(self):
        # set data from config file to class variables
        with open("config.json", "rb") as configFile:
            config = orjson.loads(configFile.read())
            self.geocode_base_url = config["geocode_base_url"]
            self.base_url = config["base_url"]
            self.api_key = config["api_key"]