# Мазин Р.Н. проект auto.mail.ru Не работает блок "Поделиться в соц. сетях" в отзывах.
# Номер баг-репорта №4638
import unittest
import sys, time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *


class Test4638(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_main(self):
        # Определим ожидание;
        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        # 1.    ***Перейти по ссылке "https://auto.mail.ru";
        self.driver.get("https://auto.mail.ru/")

        # 2.   ***Из главного меню перейти в раздел отзывов;
        try:
            comment = self.driver.find_element_by_name("clb15581074").click()
        except Exception:
            print(sys.exc_info()[1])

         # 3.   ***Перейти в первый отзыв в списке отзывов;
        try:
            first = self.driver.find_element_by_class_name("review__title").click()
        except Exception:
            print(sys.exc_info()[1])

        # 4.   ***Прокрутить страницу вниз до блока "Поделиться в соц. сетях";
        Social_media_block = self.driver.find_element_by_class_name("car__social")

        actions = ActionChains(self.driver)
        actions.move_to_element(Social_media_block).perform()

        # 5.   ***Нажать на иконку соц. сети "ВКонтакте".
        l = len(self.driver.window_handles) #Узнаем текущее количество окон
        vk = self.driver.find_element_by_class_name("share__pin_vk").click()
        # Проверяем, что появилось всплывающее окно.
        time.sleep(5)
        bsd = self.driver.window_handles
        self.assertEqual(len(bsd), l)
        print("Список окон: ", bsd)