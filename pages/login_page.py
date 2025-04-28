from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert("login" in self.browser.current_url), "неверная ссылка"

    def should_be_login_form(self):
        assert(self.browser.find_element(*LoginPageLocators.LOGIN_FORM)), "не найдена форма логина"
    def should_be_register_form(self):
        assert(self.browser.find_element(*LoginPageLocators.REGISTER_FORM)), "не найдена форма регистрации"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()