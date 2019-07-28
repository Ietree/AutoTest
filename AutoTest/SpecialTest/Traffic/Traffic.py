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
        self.all_data = [("timestamp", "traffic")]

    def test_process(self):
        """
        单次测试过程
        """
        # 获取App的进程ID
        result = os.popen("adb shell ps | findstr dji.go.v5")
        pid = result.readlines()[0].split(" ")[7]

        # 获取进程ID使用的流量
        traffic = os.popen("adb shell cat /proc/" + pid + "/net/dev | findstr wlan0")
        # 下行流量
        receive = ""
        # 上行流量
        transmit = ""
        for line in traffic:
            if "wlan0" in line:
                line = "#".join(line.split())
                receive = line.split("#")[1]
                transmit = line.split("#")[9]
        # 计算所有流量之和
        all_traffic = int(receive) + int(transmit)
        # 流量按照KB计算
        all_traffic = all_traffic / 1024
        current_time = self.get_current_time()
        self.all_data.append((current_time, all_traffic))

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
        while self.counter > 0:
            self.test_process()
            self.counter = self.counter - 1
            # 每5秒钟采集一次数据
            time.sleep(5)

    def save_data_to_csv(self):
        """
        将数据存入CSV文件中
        """
        with open("Traffic.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(self.all_data)


if __name__ == "__main__":
    controller = Controller(5)
    controller.run()
    controller.save_data_to_csv()
