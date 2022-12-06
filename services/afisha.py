import requests
import json
from datetime import date, timedelta


def load_city():
    url = 'https://mapi.kassa.rambler.ru/api/v21/cities'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.2.807 Yowser/2.5 Safari/537.36',
        'x-application-key': '7399d50b-698a-4d86-a851-a5c1b1714dfc',
    }
    response = requests.get(url, headers=headers)
    city = response.json()
    city_code = dict()
    for item in city:
        city_code[item['name']] = item['id']

    with open("city.json", "w", encoding='utf8') as file:
        json.dump(city_code, file)


def get_afisha(city, day):
    if day == 'today':
        current_date = date.today()
    elif day == 'tomorrow':
        current_date = date.today() + timedelta(days=1)

    url = f'https://mapi.kassa.rambler.ru/api/v21/creations/concert?limit=5&onDate={current_date}'
    with open("city.json", encoding='utf8') as file:
        data = json.load(file)
    city_id = data[city]

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.2.807 Yowser/2.5 Safari/537.36',
        'x-application-key': '7399d50b-698a-4d86-a851-a5c1b1714dfc',
        'x-cityid': f'{city_id}',
    }
    response = requests.get(url, headers=headers)

    afisha = response.json().get('creations', False)
    if afisha:
        afisha_list = list()
        for item in afisha:
            afisha_list.append(
                {'name': item['name'],
                 'price': item['minSessionPrice'],
                 'link': item['siteLink']}
            )
        return afisha_list
    else:
        return False
