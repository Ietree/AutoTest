#!/usr/bin/python3
# encoding:utf-8

import os
import time
import csv


# 控制类
class Controller(object):
    def __init__(self, count):
        # 定义测试的次数
        self.counter = count
        # 定义收集数据的数组
        self.all_data = [("timestamp", "power")]

    def test_process(self):
        """
        单次测试过程
        """
        # 获取手机当前电量
        result = os.popen("adb shell dumpsys battery | findstr level")
        power = result.readlines()[0].split(": ")[1].strip()

        # 获取当前时间
        current_time = self.get_current_time()
        # 将获取到的数据存到数组中
        self.all_data.append((current_time, power))

    def get_current_time(self):
        """
        获取当前时间戳
        :return: 返回当前时间戳
        """
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return current_time

    def run(self):
        """
        多次执行
        """
        # 设置手机进入非充电状态
        os.popen("adb shell dumpsys battery set status 1")
        while self.counter > 0:
            self.test_process()
            self.counter = self.counter - 1
            # 每5秒钟采集一次数据
            time.sleep(5)

    def save_data_to_csv(self):
        """
        将数据存入CSV文件中
        """
        with open("Power.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(self.all_data)


if __name__ == "__main__":
    controller = Controller(5)
    controller.run()
    controller.save_data_to_csv()
