from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver, url, timeout=10):
        self._driver = driver
        self._driver.implicitly_wait(timeout)
        self._url = url

    def open(self):
        self._driver.get(self._url)

    def is_element_presented(self, by, selector):
        try:
            self._driver.find_element(by, selector)
        except NoSuchElementException:
            return False
        return True
