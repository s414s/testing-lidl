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

        
        elements = driver.find_elements(By.CSS_SELECTOR, ".product-grid-box-tile")
        num_elements = len(elements)
        num_elements_expected = 68
        self.assertEqual(num_elements, num_elements_expected, f"El número de divs no coincide. Esperado: {num_elements_expected}, Obtenido: {num_elements}")
        print(f"El número de elementos es: {num_elements}")


    def tearDown(self):
        self.driver.close()
        #self.driver.quit()

if __name__ == "__main__":
    unittest.main()
