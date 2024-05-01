from fastapi.testclient import TestClient
from api.controller import app

client = TestClient(app)


def test_get_weather_endpoint():
    response = client.get("/weather/42.278046,-83.738220")
    assert response.status_code == 200
    assert "fahrenheit" in response.json()['message']
    assert "condition" in response.json()['message']
