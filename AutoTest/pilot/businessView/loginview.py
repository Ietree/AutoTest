import logging
from pilot.common.desired_caps import appium_desired
from pilot.common.common_fun import Common, By
from selenium.common.exceptions import NoSuchElementException


class LoginView(Common):
    # 登录界面元素
    username_type = (By.ID, 'com.tal.kaoyan:id/login_email_edittext')
    password_type = (By.ID, 'com.tal.kaoyan:id/login_password_edittext')
    loginBtn = (By.ID, 'com.tal.kaoyan:id/login_login_btn')

    # 个人中心元素
    username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')
    button_myself = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')

    # 个人中心下线警告提醒确定按钮
    commitBtn = (By.ID, 'com.tal.kaoyan:id/tip_commit')

    # 退出操作相关元素
    settingBtn = (By.ID, 'com.tal.kaoyan:id/myapptitle_RightButtonWraper')
    logoutBtn = (By.ID, 'com.tal.kaoyan:id/setting_logout_text')
    tip_commit = (By.ID, 'com.tal.kaoyan:id/tip_commit')

    def login_action(self, username, password):
        self.check_updateBtn()
        self.check_skipBtn()

        logging.info('============login_action==============')
        logging.info('username is:%s' % username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info('password is:%s' % password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info('click loginBtn')
        self.driver.find_element(*self.loginBtn).click()
        logging.info('login finished!')

    def check_account_alert(self):
        '''检测账户登录后是否有账户下线提示'''
        logging.info('====check_account_alert======')
        try:
            element = self.driver.find_element(*self.commitBtn)
        except NoSuchElementException:
            pass
        else:
            logging.info('click commitBtn')
            element.click()

    def check_loginStatus(self):
        logging.info('==========check_loginStatus===========')
        self.check_market_ad()
        self.check_account_alert()

        try:
            self.driver.find_element(*self.button_myself).click()
            self.driver.find_element(*self.username)
        except NoSuchElementException:
            logging.error('login Fail!')
            self.getScreenShot('login Fail')
            return False
        else:
            logging.info('login success!')
            l.logout_action()
            return True

    def logout_action(self):
        logging.info('=========logout_action==========')
        self.driver.find_element(*self.settingBtn).click()
        self.driver.find_element(*self.logoutBtn).click()
        self.driver.find_element(*self.tip_commit).click()


if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    l.login_action('自学网2018', 'zxw2018')
    l.check_loginStatus()
