from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from web.podemo2.page.add_member_page import AddMemberPage
from web.podemo2.page.base_page import BasePage
from web.podemo2.page.contact_page import ContactPage

class MainPage(BasePage):
    # def __init__(self):
    #     options=Options()
    #     options.debugger_address='127.0.0.1:9222'
    #     self.driver=webdriver.Chrome(options=options)
    #     # self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

    def goto_addmember1(self):
        self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        return AddMemberPage(self.driver)

    def goto_contact(self):
        sleep(2)
        locator = self.find(By.XPATH, '//*[@id="menu_contacts"]/span').click()
        # element=self.wait_for_click(locator)
        # element.click()
        return ContactPage(self.driver)

    def quit(self):
        self.driver.quit()