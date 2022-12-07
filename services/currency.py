from utils.async_requests import request

import json
import asyncio
import datetime


def get_datetime():
    dt_now = datetime.datetime.now()
    dt_now_utc = datetime.datetime.utcnow()
    time_zone = ':'.join(str(dt_now-dt_now_utc).split(':')[:2])
    date = str(dt_now).split('.')[0].split(' ')
    time_zone = time_zone if len(time_zone) == 5 else f'0{time_zone}'
    return f'{date[0]}T{date[1]}+{time_zone}'


async def get_currency():

    url = 'https://alfabank.ru/api/v1/scrooge/currencies/alfa-rates'
    params = {'currencyCode.in': 'USD,EUR,CNY,GBP,CHF,CZK,TRY',
              'rateType.in': 'rateCass,makeCash',
              'lastActualForDate.eq': 'true',
              'clientType.eq': 'standardCC',
              'date.lte': get_datetime()}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.2.807 Yowser/2.5 Safari/537.36'
    }

    response = await request(url, headers, params)

    data = json.loads(response)['data']
    currency = list()
    for item in data:
        currency_code = item['currencyCode']
        price_sell = item['rateByClientType'][0]['ratesByType'][0]['lastActualRate']['sell']['originalValue']
        currency.append(
            {'currency_code': currency_code,
             'price': price_sell}
        )
    return currency
