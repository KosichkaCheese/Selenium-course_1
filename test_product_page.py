import pytest
from .pages.product_page import ProductPage
from .pages import LoginPage, BasketPage
import time


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function")
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        self.page = LoginPage(browser, link)
        self.page.open()

        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        self.page.register_new_user(email, password)
        self.page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, setup):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        productPage = ProductPage(browser, link)
        productPage.open()
        productPage.add_to_basket()
        productPage.should_be_product_added_to_basket()
        productPage.should_match_basket_total()

    @pytest.mark.need_review
    def test_quest_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        productPage = ProductPage(browser, link)
        productPage.open()
        productPage.add_to_basket()
        productPage.should_be_product_added_to_basket()
        productPage.should_match_basket_total()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_not_be_success_message()

    def test_user_cant_see_success_message(self, browser, setup):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        productPage = ProductPage(browser, link)
        productPage.open()
        productPage.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_disappear_success_message()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()

        page.go_to_basket_page()

        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket()
        basket_page.should_have_empty_basket_message()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, link)

        product_page.open()
        product_page.go_to_login_page()

        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()