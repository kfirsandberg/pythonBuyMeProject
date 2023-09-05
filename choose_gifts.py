from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from Basepage2 import BasePage
from selenium.webdriver.support import expected_conditions as EC
class def_choose(BasePage):
    def choose_gift(self):
        self.driver.set_page_load_timeout(10)
        self.driver.implicitly_wait(10)
        self.click_element(By.XPATH, '//span[@title="סכום"]')
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'ember1075'))).click()
        self.click_element(By.XPATH, '//span[@title="אזור"]')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'ember1110'))).click()
        self.click_element(By.XPATH, '//span[@title="קטגוריה"]')
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'ember1172'))).click()
        self.click_element(By.ID, value='ember1199')

        self.driver.set_page_load_timeout(10)
        time.sleep(1)
        assert self.driver.current_url == 'https://buyme.co.il/search?budget=1&category=419&region=11'
        self.click_element(By.LINK_TEXT, value='BUYME CHEF - מגוון מסעדות שף')
        self.enter_text(By.XPATH, value="//input[@data-parsley-max='1500']").send_keys('100')
        self.driver.find_element(By.XPATH, value="//input[@data-parsley-max='1500']").send_keys(Keys.ENTER)