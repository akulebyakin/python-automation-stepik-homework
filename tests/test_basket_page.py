import pytest

from pages.basket_page import BasketPage

languages_data = (
    # ("ar", "سلة التسوق فارغة"),
    # ("ca", "La seva cistella està buida."),
    ("cs", "Váš košík je prázdný."),
    ("da", "Din indkøbskurv er tom."),
    ("de", "Ihr Warenkorb ist leer."),
    ("en", "Your basket is empty."),
    ("el", "Το καλάθι σας είναι άδειο."),
    ("es", "Tu carrito esta vacío."),
    ("fi", "Korisi on tyhjä"),
    ("fr", "Votre panier est vide."),
    ("it", "Il tuo carrello è vuoto."),
    ("ko", "장바구니가 비었습니다."),
    ("nl", "Je winkelmand is leeg"),
    ("pl", "Twój koszyk jest pusty."),
    ("pt", "O carrinho está vazio."),
    ("pt-br", "Sua cesta está vazia."),
    ("ro", "Cosul tau este gol."),
    ("ru", "Ваша корзина пуста"),
    ("sk", "Váš košík je prázdny"),
    ("uk", "Ваш кошик пустий."),
    ("zh-cn", "Your basket is empty.")
)


class TestBasketPage:
    # @pytest.mark.parametrize('language, expected_message', languages_data.keys(), languages_data.values())
    # def test_empty_basket_text(self, driver, language, expected_message):
    @pytest.mark.parametrize('languages', languages_data)
    def test_empty_basket_text(self, driver, languages):
        url = "http://selenium1py.pythonanywhere.com/basket/"
        language, expected_message = languages
        basket_page = BasketPage(driver, url)
        basket_page.open()
        basket_page.change_language(language)
        basket_page.should_be_message_that_basket_is_empty(expected_message)
