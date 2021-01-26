from locators.for_teacher_locators import ForTeacherLocators
from pages.base_page import BasePage


class ForTeacherPage(BasePage):

    def __init__(self, driver):
        self.for_teacher_locators = ForTeacherLocators
        self.driver = driver
        super(ForTeacherPage, self).__init__(driver)

    def click_my_account(self):
        self.wait_element(*self.for_teacher_locators.btn_my_account)
        self.driver.find_element(*self.for_teacher_locators.btn_my_account).click()

    def get_logger_user_email(self):
        self.wait_element(*self.for_teacher_locators.lbl_user_email)
        return self.driver.find_element(*self.for_teacher_locators.lbl_user_email).text

