import os
from fastapi import FastAPI
from api.service import Service, describe_condition

app = FastAPI()
api_key = os.environ.get("API_KEY")

service = Service(api_key=api_key)


@app.get("/weather/{lat},{lon}")
def get_weather(lat: float, lon: float):
    response = service.get_weather(lat, lon)
    temp = response['main']['temp']
    condition = describe_condition(temp)
    message = {
        'fahrenheit': temp,
        'condition': condition
    }
    return { 'message': message}
