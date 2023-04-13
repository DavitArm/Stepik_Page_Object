import math
from selenium.common import TimeoutException, NoSuchElementException, NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div .basket-mini>span>a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasePage:
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, locator, time=15):
        WebDriverWait(self.browser, time).until(ec.presence_of_element_located(locator))

    def is_not_element_present(self, locator, time=5):
        try:
            WebDriverWait(self.browser, time).until(ec.presence_of_element_located(locator))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self,locator, time=4):
        try:
            WebDriverWait(self.browser, time).until_not(ec.presence_of_element_located(locator))
        except TimeoutException:
            return False

        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def go_to_login_page(self):
        link = self.find_presence_of_element_located(BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.find_element_to_be_clickable(BasePageLocators.LOGIN_LINK), \
            "Login link is not presented"

    def go_to_basket_page(self):
        basket = self.find_presence_of_element_located(BasePageLocators.BASKET_LINK)
        basket.click()

    def should_be_authorized_user(self):
        assert self.find_element_to_be_clickable(BasePageLocators.USER_ICON), \
            "User icon is not presented, probably unauthorised user"

    def find_element_to_be_clickable(self, locator, time=5):
        return WebDriverWait(self.browser, time).until(ec.element_to_be_clickable(locator),
                                                       message=f"Not find {locator}")

    def find_presence_of_element_located(self, locator, time=5):
        return WebDriverWait(self.browser, time).until(ec.presence_of_element_located(locator),
                                                       message=f"Not find {locator}")
