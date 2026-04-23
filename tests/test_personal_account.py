from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthPageLocators, AccountPageLocators
from data_generators import generate_unique_email, generate_password, generate_name

class TestPersonalAccount:
    def setup_method(self):
        self.test_email = generate_unique_email()
        self.test_password = generate_password()
        self.test_name = generate_name()

    def register_and_login(self, driver, wait):
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AuthPageLocators.REGISTER_LINK)).click()
        wait.until(EC.visibility_of_element_located(AuthPageLocators.NAME_INPUT)).send_keys(self.test_name)
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(self.test_email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(self.test_password)
        driver.find_element(*AuthPageLocators.REGISTER_BUTTON).click()
        wait.until(EC.visibility_of_element_located(AuthPageLocators.LOGIN_BUTTON))
        driver.get("https://stellarburgers.education-services.ru/")
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT)).send_keys(self.test_email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(self.test_password)
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))

    def test_go_to_personal_account(self, driver, wait):
        self.register_and_login(driver, wait)
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        assert wait.until(EC.visibility_of_element_located(AccountPageLocators.PROFILE_LINK)).is_displayed()

    def test_logout_from_account(self, driver, wait):
        self.register_and_login(driver, wait)
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)).click()
        assert wait.until(EC.visibility_of_element_located(AuthPageLocators.LOGIN_BUTTON)).is_displayed()

    def test_go_to_constructor_from_personal_account(self, driver, wait):
        self.register_and_login(driver, wait)
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)).click()
        assert wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)).is_displayed()

    def test_go_to_constructor_by_logo(self, driver, wait):
        self.register_and_login(driver, wait)
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGO)).click()
        assert wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)).is_displayed()