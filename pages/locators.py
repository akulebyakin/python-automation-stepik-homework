from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESSFUL_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")
    SUCCESSFUL_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alert-success:first-child > div.alertinner > strong")
    INFO_MESSAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, "div.alert-info > div.alertinner > p > strong")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > p.price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, "div.basket-mini")
