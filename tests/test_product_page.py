import time

import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

page_urls = (
    "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    # pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    #              marks=pytest.mark.xfail),
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
)


class TestLoginFromProductPage:
    def test_guest_should_see_login_link_on_product_page(self, driver):
        url = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(driver, url)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, driver):
        url = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(driver, url)
        product_page.open()
        product_page.go_to_login_page()
        login_page = LoginPage(driver, driver.current_url)
        login_page.should_be_login_page()


class TestAddToBasketFromProductPage:
    @pytest.mark.need_review
    @pytest.mark.parametrize('url', page_urls)
    def test_guest_can_add_product_to_basket(self, driver, url):
        page = ProductPage(driver, url)
        page.open()
        page.add_to_basket()
        page.should_be_message_product_successfully_added_to_basket()
        page.should_be_basket_price_equals_to_product_price()

    @pytest.mark.xfail(reason="Lesson 4-3, step 6. This test should fail")
    @pytest.mark.parametrize('url', page_urls)
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, driver, url):
        page = ProductPage(driver, url)
        page.open()
        page.add_to_basket()
        page.should_not_be_success_message()

    @pytest.mark.parametrize('url', page_urls)
    def test_guest_cant_see_success_message(self, driver, url):
        page = ProductPage(driver, url)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail(reason="Lesson 4-3, step 6. This test should fail")
    @pytest.mark.parametrize('url', page_urls)
    def test_message_disappeared_after_adding_product_to_basket(self, driver, url):
        page = ProductPage(driver, url)
        page.open()
        page.add_to_basket()
        page.should_be_success_message_disappeared()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, driver):
        # Guest goes to product page
        url = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(driver, url)
        product_page.open()

        # Guest goes to basket by clicking header button
        product_page.go_to_basket_page()
        basket_page = BasketPage(driver, driver.current_url)

        # Verify that the basket is empty
        basket_page.should_be_empty()

        # Verify that there is a text that the basket is empty
        basket_page.should_be_message_that_basket_is_empty()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        # Go to login page
        login_page_url = "http://selenium1py.pythonanywhere.com/accounts/login/"
        login_page = LoginPage(driver, login_page_url)
        login_page.open()

        # Register new user
        email = str(time.time()) + "@fakemail.org"
        password = "supercalifragilisticexpialidocious"
        login_page.register_new_user(email, password)

        # Verify that user's been logged in
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, driver):
        url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(driver, url)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, driver):
        url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(driver, url)
        page.open()
        page.should_not_be_success_message()
        page.add_to_basket()
        page.should_be_message_product_successfully_added_to_basket()
        page.should_be_basket_price_equals_to_product_price()
