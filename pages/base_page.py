from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, _driver, _url, _timeout=10):
        self.driver = _driver
        self.driver.implicitly_wait(_timeout)
        self.url = _url

    def open(self):
        self.driver.get(self.url)

    def is_element_presented(self, by, selector):
        try:
            self.driver.find_element(by, selector)
        except NoSuchElementException:
            return False
        return True
