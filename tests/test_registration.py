from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators, AuthPageLocators
from data_generators import generate_unique_email, generate_password, generate_short_password, generate_name


class TestRegistration:
    
    def test_successful_registration(self, driver, wait):
        email = generate_unique_email()
        password = generate_password()
        name = generate_name()
        
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AuthPageLocators.REGISTER_LINK)).click()
        wait.until(EC.visibility_of_element_located(AuthPageLocators.NAME_INPUT)).send_keys(name)
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthPageLocators.REGISTER_BUTTON).click()
        
        login_button = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(AuthPageLocators.LOGIN_BUTTON)
        )
        assert login_button.is_displayed()
    
    def test_registration_short_password_error(self, driver, wait):
        email = generate_unique_email()
        short_password = generate_short_password()
        name = generate_name()
        
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AuthPageLocators.REGISTER_LINK)).click()
        wait.until(EC.visibility_of_element_located(AuthPageLocators.NAME_INPUT)).send_keys(name)
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(short_password)
        driver.find_element(*AuthPageLocators.REGISTER_BUTTON).click()
        
        error = wait.until(EC.visibility_of_element_located(AuthPageLocators.INCORRECT_PASSWORD_ERROR))
        assert error.is_displayed()