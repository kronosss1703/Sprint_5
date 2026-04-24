import pytest
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from urls import Urls
from locators import AuthPageLocators
from selenium.webdriver.support import expected_conditions as EC

def generate_unique_email():
    return f"test_{int(time.time() * 1000)}_{random.randint(10000, 99999)}@test.ru"

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 15)

@pytest.fixture
def test_user(driver, wait):
    email = generate_unique_email()
    password = "test123"
    name = f"User_{random.randint(1000, 9999)}"
    
    driver.get(Urls.REGISTER_URL)
    wait.until(EC.visibility_of_element_located(AuthPageLocators.NAME_INPUT)).send_keys(name)
    driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*AuthPageLocators.REGISTER_BUTTON).click()
    
    time.sleep(3)
    
    yield {"email": email, "password": password, "name": name}
    
    driver.get(Urls.BASE_URL)