import requests
from api.condition import WeatherCondition


def describe_condition(feels_like: float):
    if feels_like >= 85:
        return WeatherCondition.HOT
    elif feels_like <= 50:
        return WeatherCondition.COLD
    else:
        return WeatherCondition.MODERATE


class Service:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather?units=imperial"

    def get_weather(self, lat, lon):
        # print(self.api_key)
        url = f"{self.base_url}&lat={lat}&lon={lon}&appid={self.api_key}"
        # print(url)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch weather data. Status code: {response.status_code}")
