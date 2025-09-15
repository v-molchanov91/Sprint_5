from selenium.webdriver.common.by import By
from Sprint_5.data import CATEGORY, CITY


class MainPage:
    LOGIN_REG_BTN = (By.XPATH, ".//button[text()='Вход и регистрация']")
    AVATAR_LOGO = (By.XPATH, ".//button[@class='circleSmall']")
    USER_NAME = (By.XPATH, "//h3[@class='profileText name']")
    LOGOUT_BTN = (By.XPATH, "//button[text()='Выйти']")
    CREATE_ADVERTISEMENT = (By.XPATH, ".//button[text()='Разместить объявление']")
    MODAL_TITLE = (By.XPATH, ".//h1[@class='h1']")


class RegistrationPage:
    REPEAT_PASSWORD = (By.XPATH, ".//input[@name='submitPassword']")
    ADDED_ACC = (By.XPATH, ".//button[text()='Создать аккаунт']")
    HAVE_ACC_BTN = (By.XPATH, ".//button[text()='Уже есть аккаунт']")
    EMAIL_ERROR = (By.XPATH, ".//span[text()='Ошибка']")


class LoginPage:
    LOGIN_LABEL = (By.XPATH, "//h1[text()='Войти']")
    INPUT_EMAIL = (By.XPATH, ".//input[@name='email']")
    INPUT_PASSWORD = (By.XPATH, ".//input[@name='password']")
    NO_ACC_BTN = (By.XPATH, ".//button[text()='Нет аккаунта']")
    OPEN_BTN = (By.XPATH, ".//button[text()='Войти']")


class AdvertisementPage:
    NAME_INPUT = (By.XPATH, ".//input[@name='name']")
    PRODUCT_DESCRIPTION = (By.XPATH, ".//textarea")
    PRICE_INPUT = (By.XPATH, ".//input[@name='price']")
    CATEGORY_DROPDOWN = (
        By.XPATH,
        ".//input[@name='category']/following-sibling::button",
    )
    CATEGORY_ITEM = lambda category: (By.XPATH, f".//button/span[text()='{CATEGORY}']")
    CITY_DROPDOWN = (By.XPATH, ".//input[@name='city']//following-sibling::button")
    CITY_ITEM = lambda city: (By.XPATH, f".//button/span[text()='{CITY}']")
    CONDITION_RADIOBUTTON_USED = (By.XPATH, ".//div/label[text()='Б/У']")
    PUBLISH_BTN = (By.XPATH, ".//button[text()='Опубликовать']")


class ProfilePage:
    MY_ADS_SECTION = (By.XPATH, ".//h1[text()='Мои объявления']")
    NAME_ADS = (By.XPATH, ".//div[@class='about']/h2")
    PRICE_ADS = (By.XPATH, ".//div[@class='price']/h2")
