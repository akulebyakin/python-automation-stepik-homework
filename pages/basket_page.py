from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        product_list = self._driver.find_elements(*BasketPageLocators.PRODUCT_LIST)
        assert len(product_list) == 0, \
            f"There is {product_list} product(s) in basket product list. But the basket should be empty"

    def should_be_message_that_basket_is_empty(self, expected_message=""):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), \
            f"There is no message that the basket is empty, but should be"
        if len(expected_message) > 0:
            current_message = self._driver.find_element(*BasketPageLocators.MESSAGE_EMPTY_BASKET).text
            assert expected_message in current_message, \
                f"Empty message should be '{expected_message}' but actual is '{current_message}'"
