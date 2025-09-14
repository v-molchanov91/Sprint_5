import random
import string


BASE_URL = "https://qa-desk.stand.praktikum-services.ru"
USER_PASSWORD = "StrongPassword123"
NAME_PRODUCT = "Горе от ума"
PRICE_PRODUCT = 598
ABOUT_PRODUCT = "Комедия в стихах русского поэта и драматурга Александра Сергеевича Грибоедова, его наиболее известное произведение"
CITY = random.choice(
    [
        "Москва",
        "Санкт-Петербург",
        "Новосибирск",
        "Екатеринбург",
        "Нижний Новгород",
        "Казань",
    ]
)
CATEGORY = "Книги"


def generate_random_email() -> str:
    prefix = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = "".join(random.choices(string.ascii_lowercase, k=5))
    return f"{prefix}@{domain}.com"
