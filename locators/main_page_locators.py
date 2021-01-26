from selenium.webdriver.common.by import By


class MainPageLocators(object):
    btn_login = (By.XPATH, "//div[@class='dln-toolbar-unlogged-buttons dln-toolbar__unlogged']/a[contains(text(), 'Zaloguj się')]")