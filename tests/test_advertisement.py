import pytest
from Sprint_5.locators import MainPage, LoginPage, AdvertisementPage, ProfilePage
from Sprint_5.data import *
from Sprint_5.helpers import safe_click
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestAdvertisement:

    def test_added_advertisement_unregistered_user(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 5)

        driver.find_element(*MainPage.CREATE_ADVERTISEMENT).click()
        title = wait.until(EC.visibility_of_element_located(MainPage.MODAL_TITLE)).text

        assert "Чтобы разместить объявление, авторизуйтесь" in title

    def test_added_advertisement_registered_user(self, driver, existing_user):
        email, password = existing_user
        driver.delete_all_cookies()
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 50)

        driver.find_element(*MainPage.LOGIN_REG_BTN).click()
        wait.until(EC.visibility_of_element_located(LoginPage.OPEN_BTN))
        driver.find_element(*LoginPage.INPUT_EMAIL).send_keys(email)
        driver.find_element(*LoginPage.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*LoginPage.OPEN_BTN).click()
        wait.until(EC.element_to_be_clickable(MainPage.CREATE_ADVERTISEMENT))
        safe_click(driver, MainPage.CREATE_ADVERTISEMENT)

        wait.until(EC.visibility_of_element_located(AdvertisementPage.NAME_INPUT))
        driver.find_element(*AdvertisementPage.NAME_INPUT).send_keys(NAME_PRODUCT)
        driver.find_element(*AdvertisementPage.PRODUCT_DESCRIPTION).send_keys(
            ABOUT_PRODUCT
        )
        driver.find_element(*AdvertisementPage.PRICE_INPUT).send_keys(
            str(PRICE_PRODUCT)
        )

        driver.find_element(*AdvertisementPage.CATEGORY_DROPDOWN).click()
        driver.find_element(*AdvertisementPage.CATEGORY_ITEM(CATEGORY)).click()
        driver.find_element(*AdvertisementPage.CITY_DROPDOWN).click()
        driver.find_element(*AdvertisementPage.CITY_ITEM(CITY)).click()
        driver.find_element(*AdvertisementPage.CONDITION_RADIOBUTTON_USED).click()
        driver.find_element(*AdvertisementPage.PUBLISH_BTN).click()
        driver.refresh()
        wait.until(EC.element_to_be_clickable(MainPage.AVATAR_LOGO)).click()
        wait.until(EC.visibility_of_element_located(ProfilePage.MY_ADS_SECTION))
        wait.until(EC.visibility_of_element_located(ProfilePage.NAME_ADS))
        wait.until(EC.visibility_of_element_located(ProfilePage.PRICE_ADS))
        ad_name = driver.find_element(*ProfilePage.NAME_ADS).text
        ad_price = driver.find_element(*ProfilePage.PRICE_ADS).text

        assert ad_name == NAME_PRODUCT
        assert str(PRICE_PRODUCT) in ad_price
