import pytest
from Sprint_5.locators import MainPage, LoginPage
from Sprint_5.data import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLoginlogout:

    def test_login(self, driver, existing_user):
        email, password = existing_user
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 5)

        driver.find_element(*MainPage.LOGIN_REG_BTN).click()
        wait.until(EC.visibility_of_element_located(LoginPage.OPEN_BTN))
        driver.find_element(*LoginPage.INPUT_EMAIL).send_keys(email)
        driver.find_element(*LoginPage.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*LoginPage.OPEN_BTN).click()

        wait.until(EC.visibility_of_element_located(MainPage.AVATAR_LOGO))

        assert driver.find_element(*MainPage.AVATAR_LOGO).is_displayed()
        assert driver.find_element(*MainPage.USER_NAME).is_displayed()

    def test_logout(self, driver, existing_user):
        email, password = existing_user
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 5)

        driver.find_element(*MainPage.LOGIN_REG_BTN).click()
        wait.until(EC.visibility_of_element_located(LoginPage.OPEN_BTN))
        driver.find_element(*LoginPage.INPUT_EMAIL).send_keys(email)
        driver.find_element(*LoginPage.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*LoginPage.OPEN_BTN).click()

        wait.until(EC.visibility_of_element_located(MainPage.AVATAR_LOGO))

        driver.find_element(*MainPage.LOGOUT_BTN).click()
        wait.until(EC.visibility_of_element_located(MainPage.LOGIN_REG_BTN))

        assert driver.find_element(*MainPage.LOGIN_REG_BTN).is_displayed()
