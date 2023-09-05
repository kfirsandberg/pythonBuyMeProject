from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Basepage2 import BasePage
class def_send(BasePage):
    def send_info(self):
        self.driver.implicitly_wait(10)
        self.enter_text(By.XPATH, value="//input[@class='ember-view ember-text-field']").send_keys('kfir')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'selected-text'))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                               '//li[@class="ember-view bm-select-option"]'))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.CLASS_NAME, 'textarea-clear-all'))).click()
        self.enter_text(By.CLASS_NAME, value="parsley-success").send_keys('מזל  טוב שותף')
        image_path = '/Users/kfirzand/Downloads/macabbi-haifa.jpeg'
        self.driver.find_element(By.XPATH, value='//input[@type="file"]').send_keys(image_path)
        time.sleep(2)
        self.click_element(By.XPATH, "//span[@class='label']")
        icon_list = self.driver.find_elements(By.CLASS_NAME, value='method-icon')
        icon_list[0].click()
        self.enter_text(By.ID, value='email').send_keys('kfir@gmail.com')
        self.enter_text(By.XPATH, value="//input[@placeholder='שם שולח המתנה']").send_keys('kfir')
        element2 = self.driver.find_element(By.XPATH, value="//input[@placeholder='שם שולח המתנה']")
        name = element2.get_attribute('value')
        assert name == 'kfir'
