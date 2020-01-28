import pytest, requests

from django.conf import settings
from django.urls import resolve, reverse
# from django.test import TestCase

from .services import HTTP_MESSAGES, REQUEST_LOCATIONS, WeatherAPI


class TestWeatherAPI:

    def test_darksky_url_present(self):
        assert settings.DARKSKY_URL != ''
    
    def test_darksky_api_key_present(self):
        assert settings.DARKSKY_API_KEY != ''
    
    def test_request_locations_present(self):
        assert len(REQUEST_LOCATIONS) != 0
    
    def test_http_messages_present(self):
        assert len(list(HTTP_MESSAGES.keys())) != 0
    
    def test_index_view(self):
        path = reverse('index')
        assert resolve(path).view_name == 'index'
    
    def test_index_view_success(self):
        resp = requests.get('http://127.0.0.1:8000/')
        assert resp.status_code == 200
    
    def test_weather_view(self):
        path = reverse('weather')
        assert resolve(path).view_name == 'weather'
    
    def test_weather_api_missing_params(self):
        resp = requests.get('http://127.0.0.1:8000/weather/')
        assert resp.status_code == 400

    def test_weather_api_incomplete_params(self):
       resp = requests.get('http://127.0.0.1:8000/weather/?current_location=-33.927407,18.415747')
       assert resp.status_code == 400
    
    def test_weather_api_success(self):
        resp = requests.get('http://127.0.0.1:8000/weather/?current_location=-33.927407,18.415747&booking_location=-32.927407,19.415747')
        assert resp.status_code == 200
