from selenium.webdriver.common.by import By


class BasePageLocators(object):
    btn_understand = (By.XPATH, "//button[@class = 'cookie-approve']")