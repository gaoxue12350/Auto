from frame1.base_page import BasePage
from frame1.market import Market


class Main(BasePage):
    def goto_market(self):
        # 制造假的弹窗
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        # self.find(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        self.parse_yaml("../../auto/frame1/main.yaml", "goto_market")
        return Market(self.driver)