from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthPageLocators, AccountPageLocators
from urls import Urls

class TestPersonalAccount:
    def test_go_to_personal_account(self, driver, wait, test_user):
        driver.get(Urls.BASE_URL)
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT)).send_keys(test_user["email"])
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(test_user["password"])
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        assert wait.until(EC.visibility_of_element_located(AccountPageLocators.PROFILE_LINK)).is_displayed()

    def test_logout_from_account(self, driver, wait, test_user):
        driver.get(Urls.BASE_URL)
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT)).send_keys(test_user["email"])
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(test_user["password"])
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)).click()
        assert wait.until(EC.visibility_of_element_located(AuthPageLocators.LOGIN_BUTTON)).is_displayed()

    def test_go_to_constructor_from_personal_account(self, driver, wait, test_user):
        driver.get(Urls.BASE_URL)
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT)).send_keys(test_user["email"])
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(test_user["password"])
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)).click()
        assert wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)).is_displayed()

    def test_go_to_constructor_by_logo(self, driver, wait, test_user):
        driver.get(Urls.BASE_URL)
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT)).send_keys(test_user["email"])
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(test_user["password"])
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGO)).click()
        assert wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)).is_displayed()