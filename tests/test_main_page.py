from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestMainPage:
    def test_guest_can_go_to_login_page(self, driver):
        url = "http://selenium1py.pythonanywhere.com/"
        main_page = MainPage(driver, url)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(driver, driver.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, driver):
        url = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(driver, url)
        page.open()
        page.should_be_login_link()
