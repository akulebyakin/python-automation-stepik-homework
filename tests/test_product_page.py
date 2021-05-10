from pages.product_page import ProductPage


class TestMainPage:
    def test_guest_can_add_product_to_basket(self, driver):
        # url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(driver, url)
        page.open()
        page.add_to_basket()
        page.should_be_message_product_successfully_added_to_basket()
        page.should_be_basket_price_equals_to_product_price()
