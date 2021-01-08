from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from web.podemo2.page.base_page import BasePage


class AddMemberPage(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self.driver=driver

    def add_member(self, username, accout, phoneNum):
        # sleep(2)
        self.find(By.ID, 'username').send_keys(username)
        self.find(By.ID, 'memberAdd_acctid').send_keys(accout)
        self.find(By.ID, 'memberAdd_phone').send_keys(phoneNum)
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        # checkbox复选框
        checkbox = (By.CSS_SELECTOR, '.ww_checkbox')
        self.wait_for_click(checkbox)
        return True

    def get_Member(self, value):
        # 获取联系人
        # contactlist=self.finds(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
        # titlelist=[element.get_attribute('title') for element in contactlist]
        # print(titlelist)
        total_list = []
        while True:
            contactlist = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            titlelist = [element.get_attribute('title') for element in contactlist]
            # print(titlelist)
            if value in titlelist:
                return True
            total_list = total_list + titlelist
            sleep(2)
            result: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
            num, total = result.split('/', 1)
            if int(num) == int(total):
                return False
            else:
                sleep(2)
                self.find(By.CSS_SELECTOR, '.ww_commonImg_PageNavArrowRightNormal').click()
        return total_list
