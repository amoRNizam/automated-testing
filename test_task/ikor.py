import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class TestPriceUa(unittest.TestCase):
	driver = None
	def setUp(self):
		self.driver = webdriver.Chrome()
#		self.driver.set_window_size(1920,1080)
		self.driver.maximize_window()
		self.driver.implicitly_wait(60)
	def test_filter(self):
		#Зайти на yandex.ru
		self.driver.get("http://yandex.ru")
		#В разделе Маркет выбираю Сотовые телефоны
		self.driver.find_element_by_link_text(u"Маркет").click()
		#hover = self.driver.find_element_by_link_text(u"Электроника")
		hover = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/noindex/ul/li[1]/a")
		ActionChains(self.driver).move_to_element(hover).perform()
		time.sleep(2)
		self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/noindex/ul/li[1]/div/div/a[1]").click()
		#Захожу в росширенный поиск
#		self.driver.find_element_by_css_selector(r'.black').click()
		#Задаю параметры поиска
		price = self.driver.find_element_by_name("Цена до") #Найдем элемент "цена до..."
		self.driver.execute_script("arguments[0].scrollIntoView();", price) # Скролинг до эелемента
		self.driver.find_element_by_name("Цена до").send_keys(u"20000") # Установим значение цены
		diagonally = self.driver.find_element_by_xpath("//*[@id='search-prepack']/div/div/div[2]/div/div[1]/div[9]/fieldset/ul/li[2]/div/label/div")
		self.driver.execute_script("arguments[0].scrollIntoView();", diagonally)  # Скролинг до эелемента
		self.driver.find_element_by_xpath("//*[@id='search-prepack']/div/div/div[2]/div/div[1]/div[9]/fieldset/ul/li[2]/div/label/div").click()
		manufacturer = self.driver.find_element_by_xpath("//*[@id='search-prepack']/div/div/div[2]/div/div[1]/div[3]/fieldset")
		self.driver.execute_script("arguments[0].scrollIntoView();", manufacturer)
		self.driver.find_element_by_xpath("//*[@id='search-prepack']/div/div/div[2]/div/div[1]/div[3]/fieldset/ul/li[1]/div/a/label/div").click()
		self.driver.find_element_by_xpath("//*[@id='search-prepack']/div/div/div[2]/div/div[1]/div[3]/fieldset/ul/li[2]/div/a/label/div").click()
		self.driver.find_element_by_xpath("//*[@id='search-prepack']/div/div/div[2]/div/div[1]/div[3]/fieldset/ul/li[5]/div/a/label/div").click()
		self.driver.find_element_by_xpath("//*[@id='search-prepack']/div/div/div[2]/div/div[1]/div[3]/fieldset/ul/li[10]/div/a/label/div").click()
		self.driver.find_element_by_xpath("//*[@id='search-prepack']/div/div/div[2]/div/div[1]/div[3]/fieldset/ul/li[11]/div/a/label/div").click()
		# Проверка, что на странице 10 элементов
		time.sleep(3)
		self.assertEqual(len(self.driver.find_elements_by_class_name("n-snippet-cell2")), 5)
		# Запоминаю первый телефон в списке
		first = self.driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/div/div[1]/div[1]").get_attribute("data-id")
		print(first)
		# Изменяю сортировку на другую(популярность или новизна)
		self.driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[7]").click()
		time.sleep(3)
		# Список телефонов уже с новой сортировкой
		items = self.driver.find_elements_by_class_name("n-snippet-cell2")
		#Поиск ранее запомненного телефона
		for list in items:
			if list.get_attribute("data-id")!=first:
				continue
			list.click()
			break
		else:
			print("Не найден элемент")
			#self.driver.find_element_by_css_selector('.b-pager__next').click()
		#Выводим значение оценки
		rating = self.driver.find_element_by_class_name("rating__value").text
		print(rating)
#			self.driver.find_element_by_css_selector('.b-pager__next').click()

	def tearDown(self):
		self.driver.close()

#if __name__ == "__main__" :
#	unittest.main()
if __name__ == "__main__":
#	with open("C:/test.log", "w") as logf:
	unittest.TextTestRunner(verbosity=2, stream=logf).run(suite())

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
