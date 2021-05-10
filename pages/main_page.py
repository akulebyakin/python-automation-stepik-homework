from pages.base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self._driver.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        return LoginPage(driver=self._driver, url=self._driver.current_url)

    def should_be_login_link(self):
        assert self.is_element_presented(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
