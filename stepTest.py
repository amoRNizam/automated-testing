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
        self.driver.get("https://market.yandex.ru/")

        #Навести указатель на меню:
        try:
            computers = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/noindex/ul/li[2]/a")
        except Exception:
            print(sys.exc_info()[1])
#            raise
#            e = sys.exc_info()[1]
#            print(e.args[0])

        actions = ActionChains(self.driver)
        actions.move_to_element(computers).perform()

        #Кликнуть на раздел с компьютерами:
        try:
            notebook = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                  "/html/body/div[1]/div/div[2]/noindex/ul/li[2]/div/div/a[1]")))
            actions.move_to_element(notebook).click().perform()
        except Exception:
            print(sys.exc_info()[1])

        #Установить параметры фильтра:
        #Цена*******
        try:
            priceMax = wait.until(EC.element_to_be_clickable((By.NAME, "Цена до")))
#            actions.move_to_element(priceMax).send_keys(u"35000").perform()
            priceMax.send_keys(u"55000")
        except Exception:
            print(sys.exc_info()[1])
        #Производитель*******
        Acer = self.driver.find_element_by_id("7893318_267101")
        Apple = self.driver.find_element_by_id("7893318_153043")
        Asus = self.driver.find_element_by_id("7893318_152863")
        self.driver.execute_script("arguments[0].scrollIntoView();", Acer)
        try:
            Acer = wait.until(EC.element_to_be_clickable((By.ID, "7893318_267101")))
            actions.move_to_element(Acer).click().perform()
            Apple = self.driver.find_element_by_id("7893318_153043").click()
            Asus = self.driver.find_element_by_id("7893318_152863").click()

#            manufacturer = wait.until(EC.element_to_be_clickable((By.ID, Acer)))
        except Exception:
            print(sys.exc_info()[1])

#        actions.move_to_element(Acer).click().perform()
 #       actions.move_to_element(Apple).click().perform()
#        actions.move_to_element(Asus).click().perform()
#        self.driver.execute_script("arguments[0].scrollIntoView();", priceMax)
#        actions.move_to_element(priceMax).send_keys(u"35000").perform()

        time.sleep(5)

    def tearDown(self):
        self.driver.get_screenshot_as_file("ya123.png")  # Сделаем скриншот страницы
        self.driver.close()

if __name__ == '__main__':
    unittest(verbosity = 2)
