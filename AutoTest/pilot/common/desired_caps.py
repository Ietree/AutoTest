#!/usr/bin/python3
# encoding:utf-8
import logging
from appium import webdriver
import yaml


def appium_desired():
    """
    初始化Appium环境参数
    :return: 返回driver对象
    """
    with open('../config/desired_caps.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    desired_caps = {}
    desired_caps["platformName"] = data["platformName"]
    desired_caps["platformVersion"] = data["platformVersion"]
    desired_caps["deviceName"] = data["deviceName"]
    # desired_caps["app"] = data["app"]
    desired_caps["udid"] = data["udid"]
    desired_caps["appPackage"] = data["appPackage"]
    desired_caps["appActivity"] = data["appActivity"]
    desired_caps["noReset"] = data["noReset"]
    desired_caps["unicodeKeyboard"] = data["unicodeKeyboard"]
    desired_caps["resetKeyboard"] = data["resetKeyboard"]
    desired_caps["automationName"] = data["automationName"]
    logging.info('start run app...')
    driver = webdriver.Remote("http://" + str(data["ip"]) + ":" + str(data["port"]) + "/wd/hub", desired_caps)
    driver.implicitly_wait(5)
    return driver


if __name__ == "__main__":
    appium_desired()
