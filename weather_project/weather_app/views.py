import random, traceback

from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

from .services import HTTP_MESSAGES, REQUEST_LOCATIONS, WeatherAPI


def index(request):
    return JsonResponse({
        'message': HTTP_MESSAGES.get('index_view', 'Hello world.')
    })

def weather(request):
    weather_api = WeatherAPI()
    request_id = random.randint(0, 100000)

    def fetch_api_data(location, request_id):
        resp = {}
        location_name = location + '_location'
        location_data = request.GET.get(location_name)
        resp[location_name] = weather_api.get_weather_data(location_data.split(','))
        resp[location_name]['request_id'] = request_id
        resp[location_name]['request_location'] = ' '.join(location_name.split('_')).capitalize()
        return resp
    try:
        resp = [fetch_api_data(location, request_id) for location in REQUEST_LOCATIONS]
        weather_api.save_weather_request(resp)
        return JsonResponse(resp, safe=False)
    except (AttributeError, IndexError, KeyError) as e:
        return JsonResponse({
            'message': HTTP_MESSAGES.get('not_successful').format(e),
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'message': HTTP_MESSAGES.get('not_successful').format(e),
        }, status=500)
