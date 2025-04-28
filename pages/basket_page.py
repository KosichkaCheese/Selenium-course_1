from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket is not empty, but should be"

    def should_have_empty_basket_message(self):
        try:
            message = WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located(BasketPageLocators.EMPTY_BASKET_MESSAGE)
            )
            assert "Ваша корзина пуста" in message.text
        except TimeoutException:
            pytest.fail("Empty basket message didn't appear within 5 seconds")