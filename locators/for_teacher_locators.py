from selenium.webdriver.common.by import By


class ForTeacherLocators(object):
    btn_my_account = (By.XPATH, "//span[@class = 'ne-toolbar-menu-item__link']//*[contains(text(), 'Moje konto')]")
    lbl_user_email = (By.XPATH, "//div[@class = 'dln-toolbar-user-profile__user-email']")