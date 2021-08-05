
from Data.ExcelLib import read_locators
from Library. Selelnium_Wrapper import SeleniumWrapper
from Library.Customwait import wait_

class LoginPage(SeleniumWrapper):
    login_Objects= read_locators("loginPage")

    def __init__(self, driver):
        super().__init__(driver)

    def click_login_link(self):
        login_locator = LoginPage.login_Objects['lnk_login']
        self.click_element(login_locator)

    def enter_mail(self, email):
        mail_addrs = LoginPage.login_Objects['txt_mail']
        self.enter_text(mail_addrs, value=email)

    def click_continue(self):
        continue_locator = LoginPage.login_Objects['btn_continue']
        self.click_element(continue_locator)

    def enter_pwd(self, password):
        mail_pwd = LoginPage.login_Objects['txt_pwd']
        self.enter_text(mail_pwd, value=password)

    def click_login(self):
        btn_continue = LoginPage.login_Objects['btn_login']
        self.click_element(btn_continue)

