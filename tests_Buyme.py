import unittest
from selenium import webdriver
from BasePage import Buy_me_site
import allure
from allure_commons.types import AttachmentType
import json
def json_setup():
    with open("Json_Setup.json")as json_file:
       data = json.load(json_file)
    return data
def screenshot(self):
    allure.attach(name="nosuchlementScreenshot",
                  body=self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
class TestSignUp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        data =json_setup()
        self.driver.get(data['url'])
    def test_sign_in(self):
        try:
            Buy_me_site.sign_page(self)
            Buy_me_site.assert_name(self)
        except :
            screenshot(self)
    def test_chosse_gift(self):
        try:
            Buy_me_site.choose_gift(self)
        except :
            screenshot(self)
    def test_send_info(self):
        try:
            data =json_setup()
            self.driver.get(data['url2'])
            Buy_me_site.send_info(self)
        except :
            screenshot(self)
    def tearDown(self):
        self.driver.quit()