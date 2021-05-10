import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, driver):
        main_page = MainPage(driver, MAIN_PAGE_URL)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(driver, driver.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, driver):
        page = MainPage(driver, MAIN_PAGE_URL)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(driver):
    # Guest goes to main page
    main_page = MainPage(driver, MAIN_PAGE_URL)
    main_page.open()

    # Guest goes to basket by clicking header button
    main_page.go_to_basket_page()
    basket_page = BasketPage(driver, driver.current_url)

    # Verify that the basket is empty
    basket_page.should_be_empty()

    # Verify that there is a text that the basket is empty
    basket_page.should_be_message_that_basket_is_empty()
