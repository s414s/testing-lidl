import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.options import Options


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.driver = webdriver.Firefox(executable_path=r'geckodriver.exe', options=options)

    def test_search_in_num_elements(self):
        driver = self.driver
        driver.get("https://www.lidl.es/es/jardin/c3721")

        time.sleep(2)
        
        cookies_button = driver.find_element(By.CSS_SELECTOR, ".cookie-alert-extended-button")
        cookies_button.click()

        time.sleep(1)
        
        elements = driver.find_elements(By.CSS_SELECTOR, ".product-grid-box-tile")
        num_elements = len(elements)
        num_elements_expected = 68
        self.assertEqual(num_elements, num_elements_expected, f"El número de divs no coincide. Esperado: {num_elements_expected}, Obtenido: {num_elements}")
        print(f"El número de elementos es: {num_elements}")

    def test_search_bar(self):
        driver = self.driver
        driver.get("https://www.lidl.es/")

        time.sleep(3)

        cookies_button = driver.find_element(By.CSS_SELECTOR, ".cookie-alert-extended-button")
        cookies_button.click()

        time.sleep(1)

        searchbar = driver.find_element(By.ID, "mainsearch-input")
        searchbar.send_keys("sarten")
        search_button = driver.find_element(By.CSS_SELECTOR, ".search-bar-container-button button")
        search_button.click()

        time.sleep(3)

        title = driver.title
        expected_title = "Resultado de búsqueda | Lidl"

        self.assertEqual(title, expected_title, f"El título no coincide. Esperado: {expected_title}, Obtenido: {title}")

    def test_add_product_to_basket(self):
        driver = self.driver
        driver.get("https://www.lidl.es/es/jardin/c3721")

        time.sleep(3)

        cookies_button = driver.find_element(By.CSS_SELECTOR, ".cookie-alert-extended-button")
        cookies_button.click()

        first_element_button = driver.find_elements(By.CSS_SELECTOR, ".product-grid-box-tile .frontpage-product-teaser__addtocart")
        first_element_button[0].click()

        time.sleep(1)

        # comprobar que hay un elemento en la cesta
        driver.get("https://www.lidl.es/es/basket/contents")
        elements_in_basket_table = driver.find_elements(By.CSS_SELECTOR, ".basket tbody tr td")
        num_fields = len(elements_in_basket_table)
        expected_num_fields = 3
        self.assertEqual(num_fields, expected_num_fields, f"El título no coincide. Esperado: {expected_num_fields}, Obtenido: {num_fields}")

    def tearDown(self):
        self.driver.close()
        #self.driver.quit()

if __name__ == "__main__":
    unittest.main()
