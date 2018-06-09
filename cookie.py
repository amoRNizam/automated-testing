import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")  # инициализирую вебдрайвер
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://yandex.ru/")
# вхход в почту
elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[1]/div/a[1]")
elem.click()
# ищу поля логин-пароль
elem = driver.find_element_by_name("login")
elem.send_keys("asme25235n2004@yandex.ru")
elem = driver.find_element_by_name("passwd")
elem.send_keys("1423418525510984qw")
# кнопка авторизации
elem = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div/div/div/div/div/form/div[4]/button[1]/span/span")
elem.click()
# cookies dump
pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
# закрываю браузер  - куки в браузере не сохраняются
driver.close()
# открываю браузер заново
#driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver = webdriver.Chrome()
# загружаю куки из дампа
cookies = pickle.load(open("cookies.pkl", "rb"))
print(cookies)  # смотрю что я загрузил из дампа
driver.delete_all_cookies()  # выпилю старые прежде чем загрузить новые
for cookie in cookies:
    driver.add_cookie(cookie)

# открываю страничку для которой делал дамп куки
driver.get("https://yandex.ru/")