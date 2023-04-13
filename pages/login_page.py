from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class LoginPageLocators:

    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.XPATH, "//button[@name='registration_submit']")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert 'login' in current_url

    def should_be_login_form(self):
        assert self.find_presence_of_element_located(LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.find_presence_of_element_located(LoginPageLocators.REGISTER_FORM)

    def register_new_user(self, email, password):
        email_input = self.find_element_to_be_clickable(LoginPageLocators.EMAIL)
        email_input.click()
        email_input.send_keys(email)
        password_input = self.find_element_to_be_clickable(LoginPageLocators.PASSWORD)
        password_input.click()
        password_input.send_keys(password)
        confirm_password = self.find_element_to_be_clickable(LoginPageLocators.CONFIRM_PASSWORD)
        confirm_password.click()
        confirm_password.send_keys(password)
        register = self.find_element_to_be_clickable(LoginPageLocators.REGISTER_BUTTON)
        register.click()
