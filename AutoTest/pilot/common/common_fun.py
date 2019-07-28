from selenium.common.exceptions import NoSuchElementException
from pilot.baseView.baseview import BaseView
from pilot.common.desired_caps import appium_desired
import logging.config
import os
import time
import csv


class Common(BaseView):
    """
    封装公共方法类
    """

    def get_screenSize(self):
        """
        获取屏幕尺寸
        :return:
        """
        x = self.get_window_size()['width']
        y = self.get_window_size()['height']
        return (x, y)

    def swipeLeft(self):
        logging.info('swipeLeft')
        l = self.get_screenSize()
        y1 = int(l[1] * 0.5)
        x1 = int(l[0] * 0.95)
        x2 = int(l[0] * 0.25)
        self.swipe(x1, y1, x2, y1, 1000)

    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self, module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (module, time)

        logging.info('get %s screenshot' % module)
        self.driver.get_screenshot_as_file(image_file)

    def check_market_ad(self):
        """检测登录或者注册之后的界面浮窗广告"""
        logging.info('=======check_market_ad=============')
        try:
            element = self.driver.find_element(*self.wemedia_cacel)
        except NoSuchElementException:
            pass
        else:
            logging.info('close market ad')
            element.click()

    def get_csv_data(self, csv_file, line):
        """
        获取csv文件指定行的数据
        :param csv_file: csv文件路径
        :param line: 数据行数
        :return:
        """
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row


if __name__ == '__main__':
    driver = appium_desired()
    # c=Common(driver)
    # c.check_updateBtn()
    # # c.check_skipBtn()
    # c.swipeLef()
    # c.swipeLef()
    # c.getScreenShot("startApp")
