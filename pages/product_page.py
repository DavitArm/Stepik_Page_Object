from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPageLocators:
    ADD_TO_BASKET = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    TOTAL_BASKET_PRICE = (By.CSS_SELECTOR, "div .alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div .alert-success")
    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']//h1")
    BASKET_PRODUCT_NAME = (By.XPATH, "(//div[@class='alertinner ']/strong)[1]")
    BASKET_PAGE = (By.XPATH, "//a[@class='btn btn-default']")


class ProductPage(BasePage):

    def add_to_basket(self):
        add_to_basket = self.find_element_to_be_clickable(ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def success_message(self):
        assert self.find_presence_of_element_located(ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_disappeared(self):
        assert self.is_disappeared(ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is disappeared, but should not be"

    def right_item_in_basket(self):
        product_name = self.find_presence_of_element_located(ProductPageLocators.PRODUCT_NAME)
        basket_product_name = self.find_presence_of_element_located(ProductPageLocators.BASKET_PRODUCT_NAME)
        assert product_name.text == basket_product_name.text

    def equals_price_item_and_basket(self):
        item_price = self.find_presence_of_element_located(ProductPageLocators.PRODUCT_PRICE)
        basket_price = self.find_presence_of_element_located(ProductPageLocators.TOTAL_BASKET_PRICE)
        assert item_price.text == basket_price.text

    def get_product_name(self):
        return self.browser.find_element(ProductPageLocators.PRODUCT_NAME)

    def get_product_price(self):
        return self.browser.find_element(ProductPageLocators.PRODUCT_PRICE)
