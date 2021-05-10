from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import BasePageLocators


class BasePage:
    def __init__(self, driver, url, timeout=10):
        # Init private fields
        self._driver = driver
        self._driver.implicitly_wait(timeout)
        self._url = url

    def open(self):
        self._driver.get(self._url)

    def is_element_present(self, by, selector, timeout=4):
        try:
            WebDriverWait(self._driver, timeout).until(
                EC.presence_of_element_located((by, selector))
            )
        except (TimeoutException, NoSuchElementException):
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

    def go_to_login_page(self):
        login_link = self._driver.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self):
        basket_page_link = self._driver.find_element(*BasePageLocators.BASKET_PAGE_LINK)
        basket_page_link.click()

    def change_language(self, language):
        language_select = Select(self._driver.find_element(*BasePageLocators.SELECT_LANGUAGE))
        language_select.select_by_value(language)
        button_change_language = self._driver.find_element(*BasePageLocators.BUTTON_CHANGE_LANGUAGE)
        button_change_language.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented, probably unauthorised user"
