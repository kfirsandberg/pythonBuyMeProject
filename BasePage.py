import time
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

class BasePage():
    def __init__(self, driver):
        self.driver = driver
    def screenshot(self,name):
        allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)
        self.my_screenshots += 1
    def sign_page(self):
        try:
            self.driver.implicitly_wait(10)
            self.driver.find_element(By.CLASS_NAME, value='notSigned').click()
            self.driver.find_element(By.XPATH, '//span[@aria-label="להרשמה"]').click()
            self.driver.find_element(By.ID, 'ember1921').send_keys('כפיר')
            self.driver.find_element(By.ID, 'ember1928').send_keys('kfir@gmail.com')
            self.driver.find_element(By.ID, 'valPass').send_keys('Kfir1234')
            self.driver.find_element(By.ID, 'ember1938').send_keys('Kfir1234')
            self.driver.find_element(By.CLASS_NAME, 'fill').click()
            self.driver.find_element(By.ID, 'ember1942').click()
        except NoSuchElementException:
            self.screenshot(f"Element_not_found{self.my_screenshots}")

    def assert_name(self):
        element = self.driver.find_element(By.ID, value="ember1917")
        name_text = element.get_attribute('value')
        assert name_text == 'כפיר'
    def choose(self):
        try:
            self.driver.set_page_load_timeout(10)
            self.driver.implicitly_wait(10)
            self.driver.find_element(By.XPATH, '//span[@title="סכום"]').click()
            time.sleep(1)
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,'ember1075'))).click()
            self.driver.find_element(By.XPATH, '//span[@title="אזור"]').click()
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,'ember1110'))).click()
            self.driver.find_element(By.XPATH, '//span[@title="קטגוריה"]').click()
            time.sleep(1)
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,'ember1172'))).click()
            self.driver.find_element(By.ID,value='ember1199').click()
            self.driver.set_page_load_timeout(10)
            time.sleep(1)
            assert self.driver.current_url == 'https://buyme.co.il/search?budget=1&category=419&region=11'
            self.driver.find_element(By.LINK_TEXT,value='BUYME CHEF - מגוון מסעדות שף').click()
            self.driver.find_element(By.XPATH ,value="//input[@data-parsley-max='1500']").send_keys('100')
            self.driver.find_element(By.XPATH ,value="//input[@data-parsley-max='1500']").send_keys(Keys.ENTER)
        except NoSuchElementException:
            self.screenshot(f"Element_not_found{self.my_screenshots}")

    def send(self):
        try:
            self.driver.implicitly_wait(10)
            self.driver.find_element(By.XPATH,value="//input[@class='ember-view ember-text-field']").send_keys('kfir')
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,'selected-text'))).click()
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                  '//li[@class="ember-view bm-select-option"]'))).click()
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,'textarea-clear-all'))).click()
            self.driver.find_element(By.CLASS_NAME,value="parsley-success").send_keys('מזל  טוב שותף')
            image_path = '/Users/kfirzand/Downloads/macabbi-haifa.jpeg'
            self.driver.find_element(By.XPATH, value='//input[@type="file"]').send_keys(image_path)
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//span[@class='label']").click()
            icon_list = self.driver.find_elements(By.CLASS_NAME, value='method-icon')
            icon_list[1].click()
            self.driver.find_element(By.ID,value='email').send_keys('kfir@gmail.com')
            self.driver.find_element(By.XPATH,value="//input[@placeholder='שם שולח המתנה']").send_keys('kfir')
            element2 = self.driver.find_element(By.XPATH,value="//input[@placeholder='שם שולח המתנה']")
            name = element2.get_attribute('value')
            assert name == 'kfir'
        except NoSuchElementException:
            self.screenshot(f"Element_not_found{self.my_screenshots}")
