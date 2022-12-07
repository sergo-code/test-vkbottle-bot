import json

from utils.async_requests import request


headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/106.0.0.0 YaBrowser/22.11.2.807 Yowser/2.5 Safari/537.36'
        }


async def get_city_alias(city):
    url = 'https://catalog.api.2gis.com/2.0/region/search'
    params = {
            'key': 'rurbbn3446',
            'q': city,
            'fields': 'items.uri_code'
    }

    response = await request(url, headers=headers, params=params)
    response = json.loads(response)
    return response['result']['items'][0]['uri_code']


async def get_traffic(city):
    city = await get_city_alias(city)
    url = f'https://jam.api.2gis.com/{city}/meta/score/0/'
    response = await request(url, headers=headers)
    return response
