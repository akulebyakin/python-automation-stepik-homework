from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.driver.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_presented(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"
