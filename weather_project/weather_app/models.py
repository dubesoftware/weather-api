import datetime

from django.db import models
from django.utils import timezone


class WeatherRequest(models.Model):
    date = models.DateTimeField(default=timezone.now)
    request_id = models.IntegerField()
    request_location = models.CharField(max_length=50)
    type_icon = models.CharField(verbose_name='type (icon)', max_length=50)
    description = models.CharField(max_length=100)
    temperature = models.FloatField()
    wind_speed = models.FloatField()
    wind_bearing = models.FloatField()
    wind_gust = models.FloatField()
    rain_prob = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    verbose_name_plural = 'weather requests'

    def __str__(self):
        return f'Request ID: {self.request_id}, Location Type: {self.request_location}, Latitude: {self.latitude}, Longitude: {self.longitude}, Date: {self.date}'
