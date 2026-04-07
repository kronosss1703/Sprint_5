from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators

#1
class TestConstructor:
    
    def test_switch_to_sauces_tab(self, driver, wait):
        wait.until(EC.visibility_of_element_located(MainPageLocators.BUNS_TAB))
        wait.until(EC.element_to_be_clickable(MainPageLocators.SAUCES_TAB)).click()
        active_tab = wait.until(EC.visibility_of_element_located(MainPageLocators.ACTIVE_TAB))
        assert "Соусы" in active_tab.text or "Соус" in active_tab.text
    
    def test_switch_to_fillings_tab(self, driver, wait):
        wait.until(EC.visibility_of_element_located(MainPageLocators.BUNS_TAB))
        wait.until(EC.element_to_be_clickable(MainPageLocators.FILLINGS_TAB)).click()
        active_tab = wait.until(EC.visibility_of_element_located(MainPageLocators.ACTIVE_TAB))
        assert "Начинки" in active_tab.text or "Начинка" in active_tab.text
    
    def test_switch_to_buns_tab(self, driver, wait):
        wait.until(EC.visibility_of_element_located(MainPageLocators.BUNS_TAB))
        wait.until(EC.element_to_be_clickable(MainPageLocators.SAUCES_TAB)).click()
        wait.until(EC.element_to_be_clickable(MainPageLocators.FILLINGS_TAB)).click()
        wait.until(EC.element_to_be_clickable(MainPageLocators.BUNS_TAB)).click()
        active_tab = wait.until(EC.visibility_of_element_located(MainPageLocators.ACTIVE_TAB))
        assert "Булки" in active_tab.text or "Булка" in active_tab.text"# develop branch" 
"# " 
