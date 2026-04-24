from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthPageLocators
from urls import Urls

class TestLogin:
    def test_login_by_button_on_main(self, driver, wait, test_user):
        driver.get(Urls.BASE_URL)
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAIN)).click()
        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT)).send_keys(test_user["email"])
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(test_user["password"])
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)).is_displayed()

    def test_login_by_personal_account_button(self, driver, wait, test_user):
        driver.get(Urls.BASE_URL)
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT)).send_keys(test_user["email"])
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(test_user["password"])
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)).is_displayed()

    def test_login_from_registration_form(self, driver, wait, test_user):
        driver.get(Urls.REGISTER_URL)
        wait.until(EC.element_to_be_clickable(AuthPageLocators.LOGIN_LINK)).click()
        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT)).send_keys(test_user["email"])
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(test_user["password"])
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)).is_displayed()

    def test_login_from_password_recovery_form(self, driver, wait, test_user):
        driver.get(Urls.FORGOT_PASSWORD_URL)
        wait.until(EC.element_to_be_clickable(AuthPageLocators.LOGIN_LINK)).click()
        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT)).send_keys(test_user["email"])
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(test_user["password"])
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)).is_displayed()

    def test_incorrect_password_error(self, driver, wait, test_user):
        driver.get(Urls.BASE_URL)
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAIN)).click()
        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT)).send_keys(test_user["email"])
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys("wrong")
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        error = wait.until(EC.visibility_of_element_located(AuthPageLocators.INCORRECT_PASSWORD_ERROR))
        assert error.is_displayed()