import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
#from selenium.webdriver.chrome.options import Options

kar = str(random.randint(1,2000)) # сгенерируем случайное число

class PythonTest(unittest.TestCase):

    def setUp(self):
#        options = Options()
#        options.add_argument('--headless')
#        self.driver = webdriver.Chrome(executable_path='/home/user/drivers/chromedriver')
#        self.driver.maximize_window()
#        self.driver.implicitly_wait(10)
        self.driver = webdriver.Chrome() #chrome_options=options)

    def test_search_in_yandex(self):
        driver = self.driver
        driver.get("http://www.yandex.ru")
        self.assertIn("Яндекс", driver.title)
        elem = driver.find_element_by_id("text")
        elem.send_keys("pycon")
        assert "No results found." not in driver.page_source
        elem.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.get_screenshot_as_file('C:/'+kar+'.png')
        self.driver.close()
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(PythonTest)

if __name__ == "__main__":
    unittest.main()