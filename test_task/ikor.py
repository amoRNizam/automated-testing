import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
class TestPriceUa(unittest.TestCase):
	driver = None
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.set_window_size(1920,1080)
		self.driver.implicitly_wait(60)
	def test_filter(self):
		#Зайти на yandex.ru
		self.driver.get("http://yandex.ru")
		#В разделе Маркет выбираю Сотовые телефоны
		self.driver.find_element_by_link_text(u"Маркет").click()
		hover = self.driver.find_element_by_link_text(u"Электроника")
		# hover = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/noindex/ul/li[1]")
		ActionChains(self.driver).move_to_element(hover).perform()
		self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/noindex/ul/li[1]/div/div/a[1]").click()
		#Захожу в росширенный поиск
		self.driver.find_element_by_css_selector(r'.black').click()	
		#Задаю параметры поиска
		self.driver.find_element_by_id("f2142558003-1").send_keys('20000')
		self.driver.find_element_by_css_selector('#f2142557926 span').click()
		self.driver.find_element_by_id("f2142557926-1").send_keys('3')
		self.driver.find_element_by_css_selector('#f1801946-1871375').click()
		self.driver.find_element_by_css_selector('#f1801946-1871447').click()
		self.driver.find_element_by_css_selector('#f1801946-1871499').click()
		self.driver.find_element_by_css_selector('#f1801946-1871151').click()
		self.driver.find_element_by_css_selector('#f1801946-11756910').click()
		self.driver.find_element_by_css_selector(r'.b-gurufilters_submit-button').click()
		#Проверка, что на странице 10 элементов
		self.assertEqual(len(self.driver.find_elements_by_class_name('b-offers__info')), 10)
		#Запоминаю первый телефон в списке
		first = self.driver.find_element_by_css_selector('.results>tbody>tr>td>form>div>:first-child>div.b-offers__desc>h3>a').get_attribute('id')
		print(first)
		#Изменяю сортировку на другую(популярность или новизна)
		self.driver.find_element_by_xpath("html/body/div[3]/table/tbody/tr[2]/td[2]/div/ul[2]/li[4]/a").click()
		#Список телефонов уже с новой сортировкой
		items = self.driver.find_elements_by_xpath("//div[@class='b-offers b-offers_type_guru'] /div[@class='b-offers__desc'] /h3 /a")
		#Поиск ранее запомненного телефона
		for list in items:
			if list.get_attribute('id')!=first: 
				continue
			list.click()
			break
		else:	
			self.driver.find_element_by_css_selector('.b-pager__next').click()
	#def tearDown(self):
		#self.driver.close()
if __name__ == "__main__" :
	unittest.main()

# Задание
#1. Открыть браузер и развернуть на весь экран.
#2. Зайти на yandex.ru.
#3. В разделе маркет выбрать Сотовые телефоны.
#4. Зайти в расширенный поиск.
#5. Задать параметр поиска до 20000 рублей и Диагональ экрана от 3 дюймов.
#6. Выбрать не менее 5 любых производителей, среди популярных.
#7. Нажать кнопку Подобрать.
#8. Проверить, что элементов на странице 10.
#9. Запомнить первый элемент в списке.
#10. Изменить Сортировку на другую (популярность или новизна).
#11. Найти и нажать по имени запомненного объекта.
#12. Вывести цифровое значение его оценки.
#13. Закрыть браузер.
#"""
