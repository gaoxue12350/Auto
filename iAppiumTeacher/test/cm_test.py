import os
import time
import unittest

import yaml
from appium import webdriver

timeout = 30
poll = 2


def get_config():
    ASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = ASE_DIR + '/iAppium_python.yml'
    with open(path, encoding='gbk') as f:
        data = yaml.safe_load(f)
    print(data)
    return data

class IAppium(unittest.TestCase):

    def setUp(self):
        data = get_config()
        desired_caps = {}
        desired_caps['platformName'] = data['desired_caps']['platformName']
        desired_caps['udid'] = data['desired_caps']['udid']
        desired_caps['deviceName'] = data['desired_caps']['deviceName']
        desired_caps['appPackage'] = data['desired_caps']['appPackage']
        desired_caps['appActivity'] = data['desired_caps']['appActivity']
        desired_caps['automationName'] = data['desired_caps']['automationName']
        desired_caps['noReset'] = data['desired_caps']['noReset']
        desired_caps['app'] = f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/app/ContactManager.apk'
        appium_server_url = data['appium_server_url']['url']
        print(desired_caps)
        print(appium_server_url)
        self.driver = webdriver.Remote(appium_server_url, desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_contact(self):
        """  """

        # Workaround for version issue
        self._click_confirm_ok_btn()

        self._click_add_contact_btn()
        self._input_contact_name('A san')
        self._input_email('asan@example.com')
        self._click_save_btn()

        # Workarount for version issue
        self._click_confirm_ok_btn()
        time.sleep(2)

    def _click_add_contact_btn(self):
        elem = self._find_elem_by_xpath('//android.widget.Button[contains(@resource-id,"addContactButton")]')
        print(f'Click add contact button')
        elem.click()

    def _input_contact_name(self, txt_name):
        elem = self._find_elem_by_xpath('//android.widget.EditText[contains(@resource-id, "contactNameEditText")]')
        print(f'Input contact name {txt_name}')
        elem.send_keys(txt_name)

    def _input_email(self, txt_email):
        elem = self._find_elem_by_xpath('//android.widget.EditText[contains(@resource-id, "contactEmailEditText")]')
        print(f'Input email {txt_email}')
        elem.send_keys(txt_email)

    def _click_save_btn(self):
        elem = self._find_elem_by_xpath('//android.widget.Button[contains(@resource-id, "contactSaveButton")]')
        print('Click the save button')
        elem.click()

    def _click_confirm_ok_btn(self):
        elem = self._find_elem_by_xpath('//android.widget.Button[contains(@resource-id, "android:id/button1")]',
                                        time_out=3, raise_exception=False)
        if elem is not None:
            print('Click the ok button on confirm dialog')
            elem.click()
        else:
            print('No confirm dialog found')

    def _find_elem_by_xpath(self, elem_xpath, time_out=timeout, raise_exception=True):
        start = time.time()
        elem = None
        while time.time() - start < time_out and elem is None:
            time.sleep(poll)
            try:
                elem = self.driver.find_element_by_xpath(elem_xpath)
            except Exception:
                print('by pass the element not found')

        if elem is None and raise_exception:
            raise LookupError(f'The element which xpath is {elem_xpath} could not be found')

        return elem
