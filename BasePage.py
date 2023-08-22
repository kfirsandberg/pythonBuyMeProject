import time
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class Buy_me_site():
    def __init__(self, driver):
        self.driver = driver
    def sign_page(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.CLASS_NAME, value='notSigned').click()
        self.driver.find_element(By.XPATH, '//span[@aria-label="להרשמה"]').click()
        self.driver.find_element(By.ID, 'ember1921').send_keys('כפיר')
        self.driver.find_element(By.ID, 'ember1928').send_keys('kfir@gmail.com')
        self.driver.find_element(By.ID, 'valPass').send_keys('Kfir1234')
        self.driver.find_element(By.ID, 'ember1938').send_keys('Kfir1234')
        self.driver.find_element(By.CLASS_NAME, 'fill').click()
        self.driver.find_element(By.ID, 'ember1942').click()
    def assert_name(self):
        element = self.driver.find_element(By.ID, value="ember1917")
        name_text = element.get_attribute('value')
        assert name_text == 'כפיר'
    def choose_gift(self):
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
    def send_info(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,value="//input[@class='ember-view ember-text-field']").send_keys('kfir')
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,'selected-text'))).click()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,
                                               '//li[@class="ember-view bm-select-option"]'))).click()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(
            (By.CLASS_NAME,'textarea-clear-all'))).click()
        self.driver.find_element(By.CLASS_NAME,value="parsley-success").send_keys('מזל  טוב שותף')
        image_path = '/Users/kfirzand/Downloads/macabbi-haifa.jpeg'
        self.driver.find_element(By.XPATH, value='//input[@type="file"]').send_keys(image_path)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[@class='label']").click()
        icon_list = self.driver.find_elements(By.CLASS_NAME, value='method-icon')
        icon_list[0].click()
        self.driver.find_element(By.ID,value='email').send_keys('kfir@gmail.com')
        self.driver.find_element(By.XPATH,value="//input[@placeholder='שם שולח המתנה']").send_keys('kfir')
        element2 = self.driver.find_element(By.XPATH,value="//input[@placeholder='שם שולח המתנה']")
        name = element2.get_attribute('value')
        assert name == 'kfir'

    def dots(self):
        x= self.driver.find_element(By.XPATH,value="//div[@class='bounce1']")
        print(x.size['width'])


