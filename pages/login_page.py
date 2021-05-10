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
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented on the page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented on the page"

    def register_new_user(self, email, password):
        # Define elements
        email_input = self._driver.find_element(*LoginPageLocators.EMAIL_INPUT)
        password_input = self._driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        repeat_password_input = self._driver.find_element(*LoginPageLocators.REPEAT_PASSWORD_INPUT)
        button_register = self._driver.find_element(*LoginPageLocators.BUTTON_REGISTER)

        # Enter login and password
        email_input.send_keys(email)
        password_input.send_keys(password)
        repeat_password_input.send_keys(password)

        # Submit registration
        button_register.click()
