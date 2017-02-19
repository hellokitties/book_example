import unittest
from selenium import webdriver


class SearchTests(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to the application home page
        cls.driver.get("http://demo.magentocommerce.com/")

    def test_search_by_category(self):
        self.driver.find_element_by_class_name("search").click() #открываем поле для поиска
        self.search_field=self.driver.find_element_by_id('edit-keys')
        self.search_field.clear()
        # enter search keyword and submit
        self.search_field.send_keys("phones")
        self.search_field.submit()
        # get all the anchor elements which have product names displayed
        # currently on result page using find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath("//div[@class='result-title']/a")
        self.assertEqual(20, len(products)) #проверяем что по запросу найдено 20 элеметов

    def test_search_by_name(self):
        self.driver.find_element_by_class_name("search").click()
        self.search_field = self.driver.find_element_by_id('edit-keys')
        self.search_field.clear()
        # enter search keyword and submit
        self.search_field.send_keys("Coastal Salt & Soul")
        self.search_field.submit()
        # get all the anchor elements which have product names displayed
        # currently on result page using find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath("//div[@class='result-title']/a")
        self.assertEqual(1, len(products))

    @classmethod
    def tearDown(cls):      # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()