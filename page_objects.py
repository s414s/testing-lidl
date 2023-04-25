# page_objects.py
from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def accept_cookies(self):
        cookies_button = self.driver.find_element(By.CSS_SELECTOR, ".cookie-alert-extended-button")
        cookies_button.click()

    def search(self, search_text):
        searchbar = self.driver.find_element(By.ID, "mainsearch-input")
        searchbar.send_keys(search_text)
        search_button = self.driver.find_element(By.CSS_SELECTOR, ".search-bar-container-button button")
        search_button.click()


class JardinPage:

    def __init__(self, driver):
        self.driver = driver

    def get_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, ".product-grid-box-tile")

    def add_first_element_to_basket(self):
        first_element_button = self.driver.find_elements(By.CSS_SELECTOR, ".product-grid-box-tile .frontpage-product-teaser__addtocart")
        first_element_button[0].click()


class BasketPage:

    def __init__(self, driver):
        self.driver = driver

    def get_elements_in_basket_table(self):
        return self.driver.find_elements(By.CSS_SELECTOR, ".basket tbody tr td")
