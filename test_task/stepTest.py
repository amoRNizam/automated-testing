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
        # 1. Перейти по ссылке:
        self.driver.get("https://market.yandex.ru/")

        # Навести указатель на меню:
        try:
            computers = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/noindex/ul/li[2]/a")
        except Exception:
            print(sys.exc_info()[1])
            self.fail("file not found")

        actions = ActionChains(self.driver)
        actions.move_to_element(computers).perform()

        # 2.Кликнуть на раздел с компьютерами:
        try:
            notebook = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                              "/html/body/div[1]/div/div[2]/noindex/ul/li[2]/div/div/a[1]")))
            actions.move_to_element(notebook).click().perform()
        except Exception:
            print(sys.exc_info()[1])
            self.fail("There are no element")

        # 3.Установить параметры фильтра:
        # 3.1 Цена*******
        try:
            priceMax = wait.until(EC.element_to_be_clickable((By.NAME, "Цена до")))
            priceMax.send_keys(u"55000")
        except Exception:
            print(sys.exc_info()[1])
            self.fail("There are no element")
        # 3.2 Производитель*******
        try:
            element = self.driver.find_element_by_xpath(
                "//*[@id='search-prepack']/div/div/div[2]/div/div[1]/div[3]/fieldset/legend")
            self.driver.execute_script("arguments[0].scrollIntoView();", element) #Скролим до выбора производителей

            Acer = self.driver.find_element_by_xpath(
                "//*[@id='search-prepack']/div/div/div[2]/div/div[1]/div[3]/fieldset/ul/li[1]/div/a/label").click()
            Apple = self.driver.find_element_by_xpath(
                "//*[@id='search-prepack']/div/div/div[2]/div/div[1]/div[3]/fieldset/ul/li[3]/div/a/label").click()
            Asus = self.driver.find_element_by_xpath(
                "//*[@id='search-prepack']/div/div/div[2]/div/div[1]/div[3]/fieldset/ul/li[4]/div/a/label").click()
        except NoSuchElementException:
            self.fail("There are no element")
        # 3.3 Диагональ экрана
        try:
            element = self.driver.find_element_by_xpath(
                "//*[@id='search-prepack']/div/div/div[2]/div/div[1]/div[6]/fieldset/legend")
            self.driver.execute_script("arguments[0].scrollIntoView();", element) #Скролим до выбора диагонали

            Acer = self.driver.find_element_by_xpath(
                "//*[@id='search-prepack']/div/div/div[2]/div/div[1]/div[6]/fieldset/ul/li[1]/div/label").click()
        except NoSuchElementException:
            self.fail("There are no element")

        # 4. Проверка, что на странице 13 элементов
        self.assertEqual(len(self.driver.find_elements_by_class_name("n-snippet-card2")), 13)

        # 5. Запомним первый элемент в списке
        try:
            first = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                           "/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/div/div[1]/div[1]")))\
                .get_attribute("data-id")
            print(first)
        except NoSuchElementException:
            self.fail("There are no element")
#        actions.move_to_element(Acer).click().perform()
 #       actions.move_to_element(Apple).click().perform()
#        actions.move_to_element(Asus).click().perform()
#        self.driver.execute_script("arguments[0].scrollIntoView();", priceMax)
#        actions.move_to_element(priceMax).send_keys(u"35000").perform()


    def tearDown(self):
        self.driver.get_screenshot_as_file("ya123.png")  # Сделаем скриншот страницы
        self.driver.close()

if __name__ == '__main__':
    unittest(verbosity = 2)
