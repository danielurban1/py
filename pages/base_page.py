from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.main_page_locators = MainPageLocators

    def accept_cookies_policy(self):
        self.wait_element(*self.main_page_locators.btn_login)
        self.driver.find_element(*self.main_page_locators.btn_login).click()

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))
        except Exception:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
