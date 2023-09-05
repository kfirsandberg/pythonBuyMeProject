import sign_page
import send_infos
import choose_gifts
class Buy_me_site():
    def __init__(self, driver):
        self.driver = driver

    def sign_page(self):
        sign_page.def_sign.sign_page(self)
    def assert_name(self):
        sign_page.def_sign.assert_name(self)

    def choose_gift(self):
        choose_gifts.def_choose.choose_gift(self)

    def send_info(self):
        send_infos.def_send.send_info(self)
