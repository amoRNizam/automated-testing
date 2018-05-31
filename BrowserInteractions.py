from selenium import webdriver
import unittest

class BrowserInteractions(unittest.TestCase):

    def test(self):
        baseUrl = "https://192.168.17.240/cement.html"
        driver = webdriver.Chrome()

        # Window Maximize
        driver.maximize_window()
        # Open the Url
        driver.get(baseUrl)
        # Get Title
        title = driver.title
        print("Title of the web page is: " + title)
        # Get Current Url
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)
        # Browser Refresh
        driver.refresh()
        print("Browser Refreshed 1st time")
        driver.get(driver.current_url)
        print("Browser Refreshed 2nd time")
        # Open another Url
        driver.get("https://192.168.17.240/partneram/lichnyj-kabinet/login.html")
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)
        # Browser Back
        driver.back()
        print("Go one step back in browser history")
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)
        # Browser Forward
        driver.forward()
        print("Go one step forward in browser history")
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)
        # Get Page Source
#        pageSource = driver.page_source
#        print(pageSource)
        # Browser Close / Quit
        # driver.close()
        driver.quit()

ff = BrowserInteractions()
ff.test()