import aiohttp


async def request(url, headers=None, params=None):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params) as response:
            response = await response.text()
            return response
