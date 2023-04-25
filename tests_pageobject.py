import unittest
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from page_objects import HomePage, JardinPage, BasketPage

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.driver = webdriver.Firefox(executable_path=r'geckodriver.exe', options=options)

    def test_search_in_num_elements(self):
        driver = self.driver
        jardin_page = JardinPage(driver)
        driver.get("https://www.lidl.es/es/jardin/c3721")

        time.sleep(2)

        home_page = HomePage(driver)
        home_page.accept_cookies()

        time.sleep(1)

        elements = jardin_page.get_elements()
        num_elements = len(elements)
        num_elements_expected = 68
        self.assertEqual(num_elements, num_elements_expected, f"El número de divs no coincide. Esperado: {num_elements_expected}, Obtenido: {num_elements}")
        print(f"El número de elementos es: {num_elements}")

    def test_search_bar(self):
        driver = self.driver
        driver.get("https://www.lidl.es/")

        time.sleep(3)

        home_page = HomePage(driver)
        home_page.accept_cookies()
        time.sleep(1)

        home_page.search("sarten")

        time.sleep(3)

        title = driver.title
        expected_title = "Resultado de búsqueda | Lidl"

        self.assertEqual(title, expected_title, f"El título no coincide. Esperado: {expected_title}, Obtenido: {title}")
  
    def test_add_product_to_basket(self):
        driver = self.driver
        jardin_page = JardinPage(driver)
        driver.get("https://www.lidl.es/es/jardin/c3721")

        time.sleep(3)

        home_page = HomePage(driver)
        home_page.accept_cookies()

        jardin_page.add_first_element_to_basket()

        time.sleep(1)

        # Comprobar que hay un elemento en la cesta
        basket_page = BasketPage(driver)
        driver.get("https://www.lidl.es/es/basket/contents")
        elements_in_basket_table = basket_page.get_elements_in_basket_table()
        num_fields = len(elements_in_basket_table)
        expected_num_fields = 3
        self.assertEqual(num_fields, expected_num_fields, f"El número de campos no coincide. Esperado: {expected_num_fields}, Obtenido: {num_fields}")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
