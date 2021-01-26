from selenium.webdriver.common.by import By

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        self.locators = MainPageLocators
        self.driver = driver
        super(MainPage, self).__init__(driver)

    def click_login_button(self):
        self.wait_element(*self.locators.btn_login)
        self.driver.find_element(*self.locators.btn_login).click()
