from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys


class FullBuy(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_osnownoi(self):
        driver = self.driver
        driver.get("http://192.168.17.240")
        self.assertIn("Ассоциация Менеджеров",driver.title)
        elem = driver.find_element_by_xpath("//*[@id='container_bg']/div[6]/div[1]/div[3]/div/table/tbody/tr[1]/td[7]/table/tbody/tr[1]/td/a").click()
        elem = driver.find_element_by_xpath("//*[@id='container_bg']/div[6]/div[1]/div[3]/table/tbody/tr[1]/td[1]/table/tbody/tr/td/div[1]/div[1]/a").click()
#        elem = driver.find_element_by_xpath("//*[@id='fly']/input").click()
#        elem = driver.find_element_by_xpath("//*[@id='fly']/input").click()

#        driver.implicitly_wait(10)
        elem = driver.find_element_by_id("quantity").clear()
        elem = driver.find_element_by_id("quantity").send_keys("10")#.send_keys(Keys.RETURN)
        elem = driver.find_element_by_id("quantity").send_keys(Keys.ENTER)
        elem = driver.find_element_by_id("cart123").click()
        self.driver.get_screenshot_as_file('C:/cart.png')
#        pageSource = driver.page_source
#        print(pageSource)



#    def tearDown(self):
#        self.driver.get_screenshot_as_file('C:/'+kar+'.png')
#        self.driver.close()
#        unittest.TextTestRunner(verbosity=2).run(FullBuy)
#        runner = unittest.TextTestRunner(verbosity=2)
#        runner.run(FullBuy)


if __name__ == "__main__":
    unittest.main()
