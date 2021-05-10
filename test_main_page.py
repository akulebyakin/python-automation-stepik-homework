import time

from pages.main_page import MainPage


class TestMainPage:
    def test_guest_can_go_to_login_page(self, driver):
        url = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(driver, url)
        page.open()
        page.go_to_login_page()
        time.sleep(10)

    def test_guest_should_see_login_link(self, driver):
        url = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(driver, url)
        page.open()
        page.should_be_login_link()
