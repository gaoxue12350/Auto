from web.podemo2.page.base_page import BasePage
from web.podemo2.page.main_page import MainPage


class TestWX:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.quit()

    # def test_addMember1(self):
    #     username = 'aaai'
    #     accout = 'aaaai'
    #     phoneNum = '139000000013'
    #     addmember = self.main.goto_addmember1()
    #     addmember.add_member(username, accout, phoneNum)
    #     assert username in addmember.get_Member(username)

    def test_addMember(self):
        username = 'zc4pet45po'
        accout = 'zc54e45t'
        phoneNum = '13774556463'
        addmember = self.main.goto_contact().goto_addMember2()
        addmember.add_member(username, accout, phoneNum)
        assert addmember.get_Member(username)

    def test_addMember_1(self):
        username = 'zc4pet45p'
        accout = 'zc54e45'
        phoneNum = '13774556433'
        addmember = self.main.goto_contact().goto_addMember2()
        addmember.add_member(username, accout, phoneNum)
        assert addmember.get_Member(username)

    def test_addMember_2(self):
        username = 'zc4pet45per'
        accout = 'zc54e4df5'
        phoneNum = '13774556436'
        addmember = self.main.goto_contact().goto_addMember2()
        addmember.add_member(username, accout, phoneNum)
        assert addmember.get_Member(username)

    def test_addMember_3(self):
        username = 'zc4pper'
        accout = 'zcdf5'
        phoneNum = '13774656436'
        addmember = self.main.goto_contact().goto_addMember2()
        addmember.add_member(username, accout, phoneNum)
        assert addmember.get_Member(username)

    def test_addMember_4(self):
        username = 'zc4wsdper'
        accout = 'zcdfgf5'
        phoneNum = '13474656436'
        addmember = self.main.goto_contact().goto_addMember2()
        addmember.add_member(username, accout, phoneNum)
        assert addmember.get_Member(username)