import time

from pages.main_page import MainPage


def test_guest_can_go_to_login_page(driver):
    url = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(driver, url)
    page.open()
    page.go_to_login_page()
    time.sleep(10)
