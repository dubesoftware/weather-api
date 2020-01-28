
import datetime, requests, random

from django.conf import settings
from django.utils import timezone

from .models import WeatherRequest


HTTP_MESSAGES = {
    'index_view': 'Hello, weather world.',
    'not_successful': "Request unsuccessful due to the following exception: '{}'. Please provide a valid request.",
}

REQUEST_LOCATIONS = [
    'booking',
    'current'
]


class WeatherAPI:
    '''A utility class encapsulating the DarkSky weather API and the Django model API.
    
    It provides utilities to fetch and save weather data.
    '''
    def get_weather_data(self, location):
        '''A function to poll weather data the DarkSky API for data.

        It uses the `requests` library to perform a REST call.

        Parameters:
            location (list): A pair of coordinates.
        
        Returns:
            weather_data (dict): A dictionary with weather information.
        '''
        weather_url = settings.DARKSKY_URL.format(
            settings.DARKSKY_API_KEY,
            location[0],
            location[1])
        resp = requests.get(weather_url).json()
        weather_data = {
            'date': timezone.now(),
            'type_icon': resp['currently']['icon'],
            'description': resp['currently']['summary'],
            'temperature': resp['currently']['temperature'],
            'wind': {
                'speed': resp['currently']['windSpeed'],
                'bearing': resp['currently']['windBearing'],
                'gust': resp['currently']['windGust']
            },
            'rain_prob': resp['currently']['precipProbability'],
            'latitude': location[0],
            'longitude': location[1]
        }
        return weather_data

    def save_weather_request(self, weather_data):
        '''A function to persist weather requests to database.

        It uses the Django model API to instantiate and save WeatherRequests.

        Parameters:
            weather_data (list): A list of dictionaries containing weather information.
        
        Returns:
            Nothing.
        '''
        for item in weather_data:
            data = item[next(iter(item))]
            WeatherRequest(
                date=data['date'],
                request_id=data['request_id'],
                request_location=data['request_location'],
                type_icon=data['type_icon'],
                description=data['description'],
                temperature=data['temperature'],
                wind_speed=data['wind']['speed'],
                wind_bearing=data['wind']['bearing'],
                wind_gust=data['wind']['gust'],
                rain_prob=data['rain_prob'],
                latitude=data['latitude'],
                longitude=data['longitude']
            ).save()
