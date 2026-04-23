from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_BUTTON_MAIN = (By.CSS_SELECTOR, "button.button_button__33qZ")
    PERSONAL_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "a[href='/account']")
    CONSTRUCTOR_BUTTON = (By.CSS_SELECTOR, "a[href='/']")
    ORDER_BUTTON = (By.CSS_SELECTOR, "button.button_button__33qZ")
    LOGO = (By.CSS_SELECTOR, "div.AppHeader_header__logo")
    BUNS_TAB = (By.CSS_SELECTOR, "div.tab_tab__1SPyG:nth-child(1)")
    SAUCES_TAB = (By.CSS_SELECTOR, "div.tab_tab__1SPyG:nth-child(2)")
    FILLINGS_TAB = (By.CSS_SELECTOR, "div.tab_tab__1SPyG:nth-child(3)")
    ACTIVE_TAB = (By.CSS_SELECTOR, "div.tab_tab_type_current__2BEPc")

class AuthPageLocators:
    NAME_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='Пароль']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button.button_button__33qZ")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.button_button__33qZ")
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']")
    REGISTER_LINK = (By.CSS_SELECTOR, "a[href='/register']")
    RECOVER_PASSWORD_LINK = (By.CSS_SELECTOR, "a[href='/forgot-password']")
    INCORRECT_PASSWORD_ERROR = (By.CSS_SELECTOR, "p.input__error")

class AccountPageLocators:
    PROFILE_LINK = (By.CSS_SELECTOR, "a[href='/account/profile']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "button.Account_button__14Yp3")