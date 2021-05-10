import math

from selenium.common.exceptions import NoAlertPresentException

from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button_add_to_basket = self._driver.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()
        if "promo" in self._url:
            self.solve_quiz_and_get_code()

    def solve_quiz_and_get_code(self):
        alert = self._driver.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self._driver.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_message_product_successfully_added_to_basket(self):
        product_name = self.get_product_name()
        message_product_name = self._driver.find_element(*ProductPageLocators.SUCCESSFUL_MESSAGE_PRODUCT_NAME).text
        assert message_product_name == product_name, \
            f"Product name in successful message should be '{product_name}' but actual is: '{message_product_name}' "

    def should_be_basket_price_equals_to_product_price(self):
        product_price = self.get_product_price()
        message_product_price = self._driver.find_element(*ProductPageLocators.INFO_MESSAGE_PRODUCT_PRICE).text
        assert message_product_price == product_price, \
            f"Product price in successful message should be '{product_price}' but actual is: '{message_product_price}' "

    def get_product_name(self):
        return self._driver.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def get_product_price(self):
        return self._driver.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESSFUL_MESSAGE), \
            f"Success message is presented, but should not be"

    def should_be_success_message_disappeared(self):
        assert self.is_element_disappeared(*ProductPageLocators.SUCCESSFUL_MESSAGE), \
            f"Success message is presented, but should be disappeared"
