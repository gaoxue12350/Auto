import shelve
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    driver: WebDriver
    base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def __init__(self, driver: WebDriver = None):
        if driver == None:
            # options = Options()
            # options.debugger_address = '127.0.0.1:9222'
            # self.driver = webdriver.Chrome(options=options)
            # self.driver.get(self.base_url)
            # cookies=self.driver.get_cookies()
            # self.driver = webdriver.Remote('http://127.0.0.1:5001/wd/hub')
            self.driver = webdriver.Firefox()
            self.driver.get(self.base_url)
            db=shelve.open('../page/cookie')
            # db['cookie']=cookies
            cookies=db['cookie']
            # cookies=c
            db.close()
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
            # self.driver.get(self.base_url)
            # db['cookie']=cookies
            # db.close()
            # self.driver = webdriver.Remote('http://127.0.0.1:5001/wd/hub')
            self.driver.implicitly_wait(10)
            # self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        else:
            self.driver = driver

        # if self.base_url !='':
        #     self.driver.get(self.base_url)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def wait_for_click(self, locator, timeout=10):
        element: WebElement = WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator))
        return element
