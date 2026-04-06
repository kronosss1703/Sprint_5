import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthPageLocators
from data_generators import generate_unique_email, generate_password, generate_name


class TestLogin:
    
    @pytest.fixture(autouse=True)
    def create_test_user(self, driver, wait):
        self.test_email = generate_unique_email("user", "test", "5")
        self.test_password = generate_password()
        self.test_name = generate_name()
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AuthPageLocators.REGISTER_LINK)).click()
        wait.until(EC.visibility_of_element_located(AuthPageLocators.NAME_INPUT)).send_keys(self.test_name)
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(self.test_email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(self.test_password)
        driver.find_element(*AuthPageLocators.REGISTER_BUTTON).click()
        wait.until(EC.visibility_of_element_located(AuthPageLocators.LOGIN_BUTTON))
        driver.get("https://stellarburgers.education-services.ru/")
        yield
    
    def test_login_by_button_on_main(self, driver, wait):
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAIN)).click()
        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT)).send_keys(self.test_email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(self.test_password)
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        order_button = wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert order_button.is_displayed()
    
    def test_login_by_personal_account_button(self, driver, wait):
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT)).send_keys(self.test_email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(self.test_password)
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)).is_displayed()
    
    def test_login_from_registration_form(self, driver, wait):
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AuthPageLocators.REGISTER_LINK)).click()
        wait.until(EC.element_to_be_clickable(AuthPageLocators.LOGIN_LINK)).click()
        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT)).send_keys(self.test_email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(self.test_password)
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        
        assert wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)).is_displayed()
    
    def test_login_from_password_recovery_form(self, driver, wait):
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AuthPageLocators.RECOVER_PASSWORD_LINK)).click()
        wait.until(EC.element_to_be_clickable(AuthPageLocators.LOGIN_LINK)).click()
        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT)).send_keys(self.test_email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(self.test_password)
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        
        assert wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)).is_displayed()"# develop branch" 
