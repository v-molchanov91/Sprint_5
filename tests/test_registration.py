import pytest
from Sprint_5.locators import MainPage, RegistrationPage, LoginPage
from Sprint_5.data import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration:

    def test_regisration_new_user(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 5)

        driver.find_element(*MainPage.LOGIN_REG_BTN).click()

        wait.until(EC.visibility_of_element_located(LoginPage.NO_ACC_BTN))
        driver.find_element(*LoginPage.NO_ACC_BTN).click()

        email = generate_random_email()
        driver.find_element(*LoginPage.INPUT_EMAIL).send_keys(email)
        driver.find_element(*LoginPage.INPUT_PASSWORD).send_keys(USER_PASSWORD)
        driver.find_element(*RegistrationPage.REPEAT_PASSWORD).send_keys(USER_PASSWORD)
        driver.find_element(*RegistrationPage.ADDED_ACC).click()

        wait.until(EC.visibility_of_element_located(MainPage.AVATAR_LOGO))

        assert driver.find_element(*MainPage.AVATAR_LOGO).is_displayed()
        assert driver.find_element(*MainPage.USER_NAME).is_displayed()

    def test_regisration_failed_email(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 5)

        driver.find_element(*MainPage.LOGIN_REG_BTN).click()

        wait.until(EC.visibility_of_element_located(LoginPage.NO_ACC_BTN))
        driver.find_element(*LoginPage.NO_ACC_BTN).click()
        wait.until(EC.visibility_of_element_located(LoginPage.INPUT_EMAIL))
        driver.find_element(*LoginPage.INPUT_EMAIL).send_keys("Regina.mail.ru")
        driver.find_element(*RegistrationPage.ADDED_ACC).click()
        wait.until(EC.visibility_of_element_located(RegistrationPage.EMAIL_ERROR))

        assert driver.find_element(*RegistrationPage.EMAIL_ERROR)

    def test_regisration_existing_user(self, driver, existing_user):
        email, password = existing_user

        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 5)

        driver.find_element(*MainPage.LOGIN_REG_BTN).click()
        wait.until(EC.visibility_of_element_located(LoginPage.NO_ACC_BTN))
        driver.find_element(*LoginPage.NO_ACC_BTN).click()

        driver.find_element(*LoginPage.INPUT_EMAIL).send_keys(email)
        driver.find_element(*LoginPage.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*RegistrationPage.REPEAT_PASSWORD).send_keys(password)
        driver.find_element(*RegistrationPage.ADDED_ACC).click()
        wait.until(EC.visibility_of_element_located(RegistrationPage.EMAIL_ERROR))

        assert driver.find_element(*RegistrationPage.EMAIL_ERROR)
