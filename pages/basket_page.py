from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BasketPageLocators():
    EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_SUMMARY = (By.CSS_SELECTOR, '.basket_summary')


class BasketPage(BasePage):

    def basket_should_be_empty(self):
        assert self.find_presence_of_element_located(BasketPageLocators.EMPTY_MESSAGE), "Basket not empty"
