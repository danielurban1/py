import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from pages.for_teacher_page import ForTeacherPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.services_page import ServicesPage
from utils.files_creator import FilesCreator


class BaseTest(unittest.TestCase):

    def setUp(self):
        path = "C://Users//urban//PycharmProjects//pythonSelenium//drivers//chromedriver.exe"
        options = Options()
        # options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox')  # # Bypass OS security model
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument("--start-maximized")
        # options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(path, options=options)

    def test(self):
        login = "StudentNE@wp.pl"
        password = "NowaEra2019"

        self.driver.get("https://www.dlanauczyciela.pl")
        main_page = MainPage(self.driver)
        main_page.click_login_button()

        login_page = LoginPage(self.driver)
        login_page.fill_email(login)
        login_page.fill_password(password)
        login_page.click_login_button()

        teacher_page = ForTeacherPage(self.driver)
        teacher_page.click_my_account()
        actual_email = teacher_page.get_logger_user_email()
        self.assertEqual(login, actual_email)

        self.driver.get("https://moja.nowaera.pl")

        services_page = ServicesPage(self.driver)
        articles_links = services_page.get_articles_hrefs()
        #articles_links = self.driver.find_elements(By.XPATH, "//a[@_ngcontent-c9]")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()



