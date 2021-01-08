from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from web.podemo2.page.add_member_page import AddMemberPage
from web.podemo2.page.base_page import BasePage


class ContactPage(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self.driver=driver

    def goto_addMember2(self):
        # 点击添加成员
        # self.driver.find_element(By.CSS_SELECTOR,'.js_has_member>div:nth-child(1) .js_add_member').click()
        locator = (By.CSS_SELECTOR, '.js_has_member>div>a:nth-child(2)')

        # self.wait_for_click(locator).click()
        def wait_for_next(x: WebDriver):
            try:
                x.find_element(*locator).click()
                return x.find_element(By.ID, 'username')
            except:
                return False

        # 判断是否跳转到添加成员页面
        WebDriverWait(self.driver, 20).until(wait_for_next)
        return AddMemberPage(self.driver)
