from vkbottle import Keyboard


choose_city_menu = (
    Keyboard(one_time=False, inline=False)
    .schema(
        [
            [{"label": "Да", "type": "text", 'payload': {'cmd': 'yes'}}],
            [{"label": "Нет, указать другой", "type": "text", 'payload': {'cmd': 'no'}}],
        ]
    )
    .get_json()
)