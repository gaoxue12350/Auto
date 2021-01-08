from frame1.base_page import BasePage
from frame1.search import Search


class Market(BasePage):
    def goto_search(self):
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        self.parse_yaml("../../auto/frame1/market.yaml", "goto_search")
        return Search(self.driver)