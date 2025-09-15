import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Sprint_5.data import BASE_URL, USER_PASSWORD
from Sprint_5.helpers import generate_random_email
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Sprint_5.locators import MainPage, RegistrationPage, LoginPage
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service())
    driver.maximize_window()
    yield driver

    driver.quit()


@pytest.fixture
def existing_user(driver):
    wait = WebDriverWait(driver, 5)
    email = generate_random_email()

    driver.get(BASE_URL)
    driver.find_element(*MainPage.LOGIN_REG_BTN).click()
    no_acc_btn = wait.until(EC.element_to_be_clickable(LoginPage.NO_ACC_BTN))
    no_acc_btn.click()
    wait.until(EC.visibility_of_element_located(LoginPage.INPUT_EMAIL))
    driver.find_element(*LoginPage.INPUT_EMAIL).send_keys(email)
    driver.find_element(*LoginPage.INPUT_PASSWORD).send_keys(USER_PASSWORD)
    driver.find_element(*RegistrationPage.REPEAT_PASSWORD).send_keys(USER_PASSWORD)
    driver.find_element(*RegistrationPage.ADDED_ACC).click()

    wait.until(EC.visibility_of_element_located(MainPage.AVATAR_LOGO))
    driver.find_element(*MainPage.LOGOUT_BTN).click()
    wait.until(EC.visibility_of_element_located(MainPage.LOGIN_REG_BTN))

    return email, USER_PASSWORD
