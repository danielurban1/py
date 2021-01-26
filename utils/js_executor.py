class JSExecutor(object):

    @staticmethod
    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

