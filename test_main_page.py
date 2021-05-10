from pages.main_page import MainPage


class TestMainPage:
    def test_guest_can_go_to_login_page(self, driver):
        url = "http://selenium1py.pythonanywhere.com/"
        main_page = MainPage(driver, url)
        main_page.open()
        login_page = main_page.go_to_login_page()
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, driver):
        url = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(driver, url)
        page.open()
        page.should_be_login_link()
