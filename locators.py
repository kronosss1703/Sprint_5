from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0Xq")
    
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")
    
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")
    
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")
    
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")


class AuthPageLocators:
    
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    
    PASSWORD_INPUT = (By.NAME, "Пароль")
    
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    
    RECOVER_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    
    INCORRECT_PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")


class AccountPageLocators:
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")