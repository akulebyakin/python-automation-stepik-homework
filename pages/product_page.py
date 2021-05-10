import math

from selenium.common.exceptions import NoAlertPresentException  # в начале файла

from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        button_add_to_basket = self._driver.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()
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
        product_name = self._driver.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        self.is_element_presented(*ProductPageLocators.SUCCESSFUL_MESSAGES)
        assert self.is_successful_messages_contain_text(product_name), \
            f"Successful messages don't contain product name '{product_name}' "

    def should_be_basket_price_equals_to_product_price(self):
        product_price = self._driver.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert self.is_info_messages_contain_text(product_price), \
            f"Info messages don't contain product price '{product_price}' "

    def is_successful_messages_contain_text(self, text):
        successful_messages_elements = self._driver.find_elements(*ProductPageLocators.SUCCESSFUL_MESSAGES)
        return any(text in message for message in [element.text for element in successful_messages_elements])

    def is_info_messages_contain_text(self, text):
        successful_messages_elements = self._driver.find_elements(*ProductPageLocators.INFO_MESSAGES)
        return any(text in message for message in [element.text for element in successful_messages_elements])
