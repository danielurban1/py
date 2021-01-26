from selenium.webdriver.common.by import By

from locators.services_page_locators import ServicesPageLocators
from pages.base_page import BasePage


class ServicesPage(BasePage):

    def __init__(self, driver):
        self.services_locators = ServicesPageLocators
        self.driver = driver
        super(ServicesPage, self).__init__(driver)

    def get_articles_hrefs(self):
        self.wait_element(*self.services_locators.lbl_articles)
        articles = self.driver.find_elements(*self.services_locators.lbl_articles)
        articles_hrefs_list = []
        for article in articles:
            print(article.get_attribute("href"))
            articles_hrefs_list.append(article.get_attribute("href"))
        return articles_hrefs_list
