import unittest
from selenium import webdriver
from BasePage import BasePage
import json
def json_setup():
    json_file = open('Json_Setup.json', 'r')
    data = json.load(json_file)
    return data

class TestSignUp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        data =json_setup()
        self.driver.get(data['url'])
        # self.sign_up_page = BasePage(self.driver)
    def test_sign_in(self):
        BasePage.sign_page(self)
        BasePage.assert_name(self)

    def test_chosse(self):
        BasePage.choose(self)
    def test_send(self):
        data =json_setup()
        self.driver.get(data['url2'])
        BasePage.send(self)

    def tearDown(self):
        self.driver.quit()
