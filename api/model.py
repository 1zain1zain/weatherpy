from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Coord:
    lon: float
    lat: float

@dataclass
class Weather:
    id: int
    main: str
    description: str
    icon: str

@dataclass
class Main:
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: int
    grnd_level: int

@dataclass
class Wind:
    speed: float
    deg: int
    gust: float

@dataclass
class Clouds:
    all: int

@dataclass
class Sys:
    type: int
    id: int
    country: str
    sunrise: int
    sunset: int

@dataclass
class WeatherResponse:
    coord: Coord
    weather: List[Weather]
    base: str
    main: Main
    visibility: int
    wind: Wind
    clouds: Clouds
    dt: int
    sys: Sys
    timezone: int
    id: int
    name: str
    cod: int
