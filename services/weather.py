import json

from utils.async_requests import request


headers = {'X-Gismeteo-Token': '61f2622da85fe2.06084651',
           'Accept-Encoding': 'deflate, gzip'}


async def get_city_id(city):
    url = 'https://api.gismeteo.net/v2/search/cities'
    params = {
        'lang': 'ru',
        'query': city
    }
    response = await request(url, headers=headers, params=params)
    return json.loads(response)['response']['items'][0]['id']


async def get_weather(city, day):
    city_id = await get_city_id(city)
    url = f'https://api.gismeteo.net/v2/weather/forecast/{city_id}'
    params = {
        'lang': 'ru',
        'days': '1' if day == 'today' else '2'
    }
    response = await request(url, headers=headers, params=params)
    weather = list()
    response = json.loads(response)

    if day == 'today':
        for i in range(8):
            weather.append(
                {'time': response['response'][i]['date']['local'].split(' ')[1][:-3],
                 'description': response['response'][i]['description']['full'],
                 'temperature': response['response'][i]['temperature']['air']['C']}
            )
        return weather
    else:
        for i in range(8, 16):
            weather.append(
                {'time': response['response'][i]['date']['local'].split(' ')[1][:-3],
                 'description': response['response'][i]['description']['full'],
                 'temperature': response['response'][i]['temperature']['air']['C']}
            )
        return weather
