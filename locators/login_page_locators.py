from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    input_email = (By.ID, "user-form-login-email")
    input_password = (By.ID, "user-form-login-password")
    btn_login = (By.XPATH, "//input[@value='Zaloguj się']")

