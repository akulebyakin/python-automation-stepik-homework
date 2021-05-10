import pytest

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


class TestMainPage:

    @pytest.mark.parametrize('url', page_urls)
    def test_guest_can_add_product_to_basket(self, driver, url):
        page = ProductPage(driver, url)
        page.open()
        page.should_not_be_success_message()
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
