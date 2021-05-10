from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        expected_url = "login"
        current_url = self._driver.current_url
        assert expected_url in current_url, \
            f"Current url is not correct. Should contain {expected_url}, but current url is {current_url}"

    def should_be_login_form(self):
        assert self.is_element_presented(*LoginPageLocators.LOGIN_FORM), "Login form is not presented on the page"

    def should_be_register_form(self):
        assert self.is_element_presented(*LoginPageLocators.REGISTER_FORM), "Register form is not presented on the page"
