import pickle
import selenium.webdriver

driver = selenium.webdriver.Chrome()
driver.get("http://192.168.17.240/")

driver.find_element_by_xpath(u"//img[@alt='Цемент']").click()
driver.find_element_by_css_selector("img.jshop_img").click()
driver.find_element_by_css_selector("input.button").click()
driver.find_element_by_css_selector("input.button").click()
driver.find_element_by_css_selector("span").click()
# Сохраним куки
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
driver.quit()
# а затем добавить их обратно:

driver = selenium.webdriver.Chrome()
driver.get("http://192.168.17.240/")
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)