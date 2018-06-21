import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys
#*****************
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class TestBuySitilink(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_buy(self):
        #Определим ожидание:
        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        #Перейти по ссылке:
        self.driver.get("https://www.citilink.ru")

        #Навести указатель на меню:
        try:
            computers = self.driver.find_element_by_xpath("//*[@id='layout']/div[1]/div/menu[1]/li[2]")
        except Exception:
            print(sys.exc_info()[1])
#            raise
#            e = sys.exc_info()[1]
#            print(e.args[0])

        actions = ActionChains(self.driver)
        actions.move_to_element(computers).perform()

        #Кликнуть на раздел с видеокартами:
        try:
            graphicsCard = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                  "//*[@id='layout']/div[1]/div/menu[1]/li[2]/div/div[9]/div/a")))
            actions.move_to_element(graphicsCard).click().perform()
        except Exception:
            print(sys.exc_info()[1])

        #Установить параметры фильтра:
        try:
            priceMax = self.driver.find_element_by_name("price_max")
        except Exception:
            print(sys.exc_info()[1])
        time.sleep(3)
#        self.driver.execute_script("arguments[0].scrollIntoView();", priceMax)
#        actions.move_to_element(priceMax).send_keys(u"35000").perform()
        priceMax.send_keys(keys.Backspace)
#        priceMax.click()
#        time.sleep(4)
        priceMax.send_keys(u"35000")


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest(verbosity = 2)
