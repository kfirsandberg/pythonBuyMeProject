from selenium.webdriver.common.by import By
from Basepage2 import BasePage
class def_sign(BasePage):
    def sign_page(self):
        self.driver.implicitly_wait(10)
        self.click_element(By.CLASS_NAME, value='notSigned')
        self.click_element(By.CLASS_NAME, 'notSigned')
        self.click_element(By.XPATH, '//span[@aria-label="להרשמה"]')
        self.enter_text(By.ID, 'ember1921').send_keys('כפיר')
        self.enter_text(By.ID, 'ember1928').send_keys('kfir@gmail.com')
        self.enter_text(By.ID, 'valPass').send_keys('Kfir1234')
        self.enter_text(By.ID, 'ember1938').send_keys('Kfir1234')
        self.click_element(By.CLASS_NAME, 'fill').click()
        self.click_element(By.ID, 'ember1942').click()


    def assert_name(self):
        element = self.driver.find_element(By.ID, value="ember1917")
        name_text = element.get_attribute('value')
        assert name_text == 'כפיר'