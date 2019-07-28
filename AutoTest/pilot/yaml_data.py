#!/usr/bin/python3
# encoding:utf-8
from appium import webdriver
import yaml

file = open("config/desired_caps.yaml", encoding="utf-8")
data = yaml.load(file, Loader=yaml.FullLoader)

desired_caps = {}
# 使用的手机操作系统
desired_caps["platformName"] = data["platformName"]
# 手机操作系统的版本
desired_caps["platformVersion"] = data["platformVersion"]
# 使用的手机或模拟器类型
desired_caps["deviceName"] = data["deviceName"]
# 本地绝对路径_或_远程 http URL 所指向的一个安装包（.ipa,.apk,或 .zip 文件）。Appium 将其安装到合适的设备上
# desired_caps["app"] = data["app"]
# 连接真机的唯一设备号
desired_caps["udid"] = data["udid"]
# 运行的 Android 应用的包名
desired_caps["appPackage"] = data["appPackage"]
# Activity 的名字是指从你的包中所要启动的 Android acticity。他通常需要再前面添加. （例如 使用 .MainActivity 代替 MainActivity）
desired_caps["appActivity"] = data["appActivity"]
# 在当前 session 下不会重置应用的状态。默认值为 false
desired_caps["noReset"] = data["noReset"]
# 使用 Unicode 输入法。 默认值为 false，输入中文时需要设置
desired_caps["unicodeKeyboard"] = data["unicodeKeyboard"]
# 在设定了unicodeKeyboard关键字的Unicode测试结束后，重置输入法到原有状态。如果单独使用，将会被忽略。默认值为 false
desired_caps["resetKeyboard"] = data["resetKeyboard"]
# Appium 1.6.3开始支持识别Toast内容，主要是基于UiAutomator2
desired_caps["automationName"] = data["automationName"]
# 启动连接Appium Server
driver = webdriver.Remote("http://" + str(data["ip"]) + ":" + str(data["port"]) + "/wd/hub", desired_caps)
# 等待5秒钟
driver.implicitly_wait(5000)

driver.find_element_by_id("dji.go.v5:id/main_page_ui_device_disconnect_state_button").click()
