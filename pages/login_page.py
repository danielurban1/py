import time

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        self.login_page_locators = LoginPageLocators
        self.driver = driver
        super(LoginPage, self).__init__(driver)

    def fill_email(self, email):
        self.wait_element(*self.login_page_locators.input_email)
        self.driver.find_element(*self.login_page_locators.input_email).send_keys(email)

    def fill_password(self, password):
        self.wait_element(*self.login_page_locators.input_password)
        self.driver.find_element(*self.login_page_locators.input_password).send_keys(password)

    def click_login_button(self):
        self.wait_element(*self.login_page_locators.btn_login)
        element = self.driver.find_element(*self.login_page_locators.btn_login)
        self.driver.execute_script("arguments[0].click();", element)

