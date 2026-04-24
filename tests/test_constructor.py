from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators

class TestConstructor:
    def test_switch_to_sauces_tab(self, driver, wait):
        wait.until(EC.element_to_be_clickable(MainPageLocators.SAUCES_TAB)).click()
        active_tab = wait.until(EC.visibility_of_element_located(MainPageLocators.ACTIVE_TAB))
        assert "Соусы" in active_tab.text

    def test_switch_to_fillings_tab(self, driver, wait):
        wait.until(EC.element_to_be_clickable(MainPageLocators.FILLINGS_TAB)).click()
        active_tab = wait.until(EC.visibility_of_element_located(MainPageLocators.ACTIVE_TAB))
        assert "Начинки" in active_tab.text

    def test_switch_to_buns_tab(self, driver, wait):
        wait.until(EC.element_to_be_clickable(MainPageLocators.SAUCES_TAB)).click()
        wait.until(EC.visibility_of_element_located(MainPageLocators.ACTIVE_TAB))
        buns_tab = wait.until(EC.presence_of_element_located(MainPageLocators.BUNS_TAB))
        driver.execute_script("arguments[0].click();", buns_tab)
        active_tab = wait.until(EC.visibility_of_element_located(MainPageLocators.ACTIVE_TAB))
        assert "Булки" in active_tab.text