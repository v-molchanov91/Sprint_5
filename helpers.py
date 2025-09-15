from selenium.common.exceptions import StaleElementReferenceException
import time
import random
import string


def generate_random_email():
    username = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = "example.com"
    return f"{username}@{domain}"


def safe_click(driver, by_locator, timeout=10):
    end_time = time.time() + timeout
    while True:
        try:
            element = driver.find_element(*by_locator)
            element.click()
            return
        except StaleElementReferenceException:
            if time.time() > end_time:
                raise TimeoutException("Element is still stale after retries")
            time.sleep(0.1)
