import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys
# *****************
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class TestFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.set_script_timeout(10)
    def test_buy(self):
        # Определим ожидание:
        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        # 1.    ***Перейти по ссылке:
        self.driver.get("https://market.yandex.ru/")

        # 1.1   ***Навести указатель на меню с электроникой:
        try:
            electronics = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/noindex/ul/li[1]/a")
            actions = ActionChains(self.driver)
            actions.move_to_element(electronics).perform()
        except Exception:
            print(sys.exc_info()[1])
            self.fail("step №1")

        # 2.    ***Кликнуть на раздел с телефонами:
        try:
            phone = wait.until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/noindex/ul/li[1]/div/div/a[1]")))
            actions.move_to_element(phone).click().perform()
        except Exception:
            print(sys.exc_info()[1])
            self.fail("step №2")

        # 3.    ***Установить параметры фильтра:
        # 3.1   ***Цена:
        try:
            priceMax = wait.until(EC.element_to_be_clickable((By.NAME, "Цена до")))
            priceMax.send_keys(u"55000")
        except Exception:
            print(sys.exc_info()[1])
            self.fail("step №3.1")

        # 3.2   ***Производитель
        try:
            element = self.driver.find_element_by_class_name("ShXb4FpS5R")
            self.driver.execute_script("arguments[0].scrollIntoView();", element)  # Скролим до выбора производителей

            Asus = self.driver.find_element_by_xpath(
                "//*[@id='search-prepack']/div/div/div[2]/div/div[1]/div[5]/fieldset/ul/li[2]/div/a/label").click()
            LG = self.driver.find_element_by_xpath(
                "//*[@id='search-prepack']/div/div/div[2]/div/div[1]/div[5]/fieldset/ul/li[6]/div/a/label").click()
            Samsung = self.driver.find_element_by_xpath(
                "//*[@id='search-prepack']/div/div/div[2]/div/div[1]/div[5]/fieldset/ul/li[10]/div/a/label").click()
        except Exception:
            print(sys.exc_info()[1])
            self.fail("step №3.2")

        # 3.3   ***Диагональ экрана
        try:
            diagonally = self.driver.find_element_by_xpath(
                "//*[@id='search-prepack']/div/div/div[2]/div/div[1]/div[6]/fieldset/legend")
            self.driver.execute_script("arguments[0].scrollIntoView();", diagonally)  # Скролим до выбора диагонали

            dia4 = self.driver.find_element_by_xpath(
                "//*[@id='search-prepack']/div/div/div[2]/div/div[1]/div[11]/fieldset/ul/li[3]/div/label").click()
        except Exception:
            print(sys.exc_info()[1])
            self.fail("step №3.3")
        time.sleep(3)  # к сожаленью этот метод

        # 4.    ***Проверить, что на странице 8 элементов
        self.assertEqual(len(self.driver.find_elements_by_class_name("n-snippet-cell2")), 8)

        # 5.    ***Записать первый элемент в списке
        try:
            first = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH, "/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/div/div[1]/div[1]"))) \
                .get_attribute("data-id")
#            print(first)
        except Exception:
            print(sys.exc_info()[1])
            self.fail("step №5")
        time.sleep(3)
        # 6.    ***Сортировать по новизне:
        try:
            most_recent = self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[7]/a")
            self.driver.execute_script("arguments[0].scrollIntoView();", most_recent)  # Скролим до выбора сортировки
            most_recent.click()
        except Exception:
            print(sys.exc_info()[1])
            self.fail("step №6")
        time.sleep(3)

        # 7.    ***Найти и кликнуть на ранее записанный товар:
        items = self.driver.find_elements_by_class_name("n-snippet-cell2")
        # Поиск ранее запомненного телефона
        try:
            for list in items:
                if list.get_attribute('data-id') != first:
                    continue
                self.driver.execute_script("arguments[0].scrollIntoView();", list) # Скролим до выбора сортировки
#                print(list.get_attribute("data-id"))
                list.click()
                print("pass")
                break
        except Exception:
            print(sys.exc_info()[1])
            self.fail("step №7")

    def tearDown(self):
        self.driver.get_screenshot_as_file("ya123.png")  # Сделаем скриншот страницы
#        log = self.driver.get_log()
#        print(log)
        self.driver.close()


if __name__ == '__main__':
    unittest(verbosity=2)
