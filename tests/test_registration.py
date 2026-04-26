from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import AuthPageLocators
from urls import Urls
from data_generators import generate_unique_email, generate_short_password, generate_name

class TestRegistration:
    def test_successful_registration(self, driver, wait):
        email = generate_unique_email()
        password = "test123"
        name = generate_name()
        driver.get(Urls.REGISTER_URL)
        wait.until(EC.visibility_of_element_located(AuthPageLocators.NAME_INPUT)).send_keys(name)
        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthPageLocators.REGISTER_BUTTON).click()
        login_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(AuthPageLocators.LOGIN_BUTTON)
        )
        assert login_button.is_displayed()

    def test_registration_short_password_error(self, driver, wait):
        email = generate_unique_email()
        short_password = generate_short_password()
        name = generate_name()
        driver.get(Urls.REGISTER_URL)
        wait.until(EC.visibility_of_element_located(AuthPageLocators.NAME_INPUT)).send_keys(name)
        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(short_password)
        driver.find_element(*AuthPageLocators.REGISTER_BUTTON).click()
        error = wait.until(EC.visibility_of_element_located(AuthPageLocators.INCORRECT_PASSWORD_ERROR))
        assert error.is_displayed()