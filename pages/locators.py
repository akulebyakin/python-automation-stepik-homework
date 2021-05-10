from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    SELECT_LANGUAGE = (By.CSS_SELECTOR, "select[name='language']")
    BUTTON_CHANGE_LANGUAGE = (By.CSS_SELECTOR, "form#language_selector > button[type='submit']")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_PAGE_LINK = (By.CSS_SELECTOR, "div.basket-mini a.btn")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input#id_registration-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input#id_registration-password1")
    REPEAT_PASSWORD_INPUT = (By.CSS_SELECTOR, "input#id_registration-password2")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESSFUL_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")
    SUCCESSFUL_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alert-success:first-child > div.alertinner > strong")
    INFO_MESSAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, "div.alert-info > div.alertinner > p > strong")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > p.price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, "div.basket-mini")


class BasketPageLocators:
    PRODUCT_LIST = (By.CSS_SELECTOR, "div.basket-items > div.row")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "div.content > div#content_inner")
