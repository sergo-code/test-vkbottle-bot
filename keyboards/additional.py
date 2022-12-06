from vkbottle import Keyboard


weather_menu = (
    Keyboard(one_time=False, inline=False)
    .schema(
        [
            [{"label": "Главное меню", "type": "text", "color": "positive", "payload": {"cmd": "main"}}],
            [{"label": "Сегодня", "type": "text", "payload": {"cmd": "weather_today"}}],
            [{"label": "Завтра", "type": "text", "payload": {"cmd": "weather_tomorrow"}}],
        ]
    )
    .get_json()
)

poster_menu = (
    Keyboard(one_time=False, inline=False)
    .schema(
        [
            [{"label": "Главное меню", "type": "text", "color": "positive", "payload": {"cmd": "main"}}],
            [{"label": "Сегодня", "type": "text", "payload": {"cmd": "afisha_today"}}],
            [{"label": "Завтра", "type": "text", "payload": {"cmd": "afisha_tomorrow"}}],
        ]
    )
    .get_json()
)
