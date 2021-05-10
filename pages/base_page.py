from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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

    def is_not_element_present(self, by, selector, timeout=4):
        try:
            WebDriverWait(self._driver, timeout).until(
                EC.presence_of_element_located((by, selector))
            )
        except TimeoutException:
            return True
        return False

    def is_element_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(driver=self._driver, timeout=timeout, poll_frequency=1, ignored_exceptions=TimeoutException) \
                .until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
