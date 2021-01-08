from frame1.base_page import BasePage


class Search(BasePage):
    def search(self):
        self.parse_yaml("../../auto/frame1/search.yaml", "search")
        return True