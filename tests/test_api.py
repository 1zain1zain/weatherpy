import pytest
from api.service import Service


@pytest.fixture
def weather_service():
    return Service(api_key="test_api_key")


def test_get_weather_success(weather_service, requests_mock):
    requests_mock.get(
        "https://api.openweathermap.org/data/2.5/weather?units=imperial&lat=35.0&lon=139.0&appid=test_api_key",
        json={"weather": [{"main": {"temp": 51.2}}]},
    )
    weather_data = weather_service.get_weather(35.0, 139.0)
    print(weather_data)
    assert weather_data["weather"][0]["main"]["temp"] == 51.2
