# Weather Forecast App

## Description
Weather Forecast App is a console application developed using python. It provides real time weather data based on the city name. It uses OpenWeather API(_openweathermap.org_) to fetch the data. The app provides a user-friendly format for user-interaction. It provides a minimal way to get the current weather details.

### Why This App?
The app provides a minimalistic approach to get the current weather details. The data is reliable since it is fetched from trusted sources. Using the data, one can plan his outing.

---

## Architecture Diagram

```
+-----------------------+
|  ConfigurationManager |
+-----------------------+
           |
           v
+-----------------------+
|       GeoUtils        |
+-----------------------+
           |
           v
+-----------------------+
|     WeatherUtils      |
+-----------------------+
           |
           v
+-----------------------+
|      MenuUtils        |
+-----------------------+
           |
           v
+-----------------------+
|        main.py        |
+-----------------------+
```

---

## How to Compile and Run

### Prerequisites
- Python 3.8 or higher
- Required Python libraries, run following commands to install the required libraries
  - `pip install requests`
  - `pip install orjson`

### Steps to Run
```bash
python main.py
```

---

## Challenges Faced
1. **API Integration**: Handling the invalid city names.
2. **User Input Validation**: Ensuring a valid string input and ask again till valid data is provided.
3. **Time Zone Adjustments**: Converting timestamps to local time zones for sunrise and sunset data.

---

## Future Enhancements
1. **Graphical User Interface (GUI)**: Develop a GUI version of the app.
2. **API Services**: Developing a API so that multiple clients(web app, windows app, mobile, etc) can use it.
3. **Advanced Weather Insights**: More detailed weather metrics.

---

## Contact
Reach out to _architchopra98@gmail.com_ for any support.