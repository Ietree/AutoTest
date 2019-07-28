#!/usr/bin/python3
import os
import time
import csv


class App(object):
    def __init__(self):
        self.content = ""
        self.start_time = 0

    def launch_app(self):
        """
        启动App
        """
        start_cmd = "adb shell am start -W -n dji.go.v5/com.dji.component.application.activity.DJILauncherActivity"
        self.content = os.popen(start_cmd)

    def stop_app(self):
        """
        杀掉App
        """
        stop_cmd = "adb shell input keyevent 3"
        os.popen(stop_cmd)

    def get_launched_time(self):
        """
        获取启动时间
        :return: 启动时间
        """
        for line in self.content.readlines():
            if "ThisTime" in line:
                self.start_time = line.split(":")[1]
                break
        return self.start_time


# 控制类
class Controller(object):
    def __init__(self, count):
        self.app = App()
        self.counter = count
        self.all_data = [("timestamp", "elapsed_time")]

    def test_process(self):
        """
        单次测试过程
        """
        self.app.launch_app()
        time.sleep(5)
        elpased_time = self.app.get_launched_time().strip()
        self.app.stop_app()
        time.sleep(3)
        current_time = self.get_current_time()
        self.all_data.append((current_time, elpased_time))

    def get_current_time(self):
        """
        获取当前时间戳
        :return: 返回当前时间戳
        """
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return current_time

    def run(self):
        """
        多次执行测试过程
        """
        while self.counter > 0:
            self.test_process()
            self.counter = self.counter - 1

    def save_data_to_csv(self):
        """
        将数据存入CSV文件中
        """
        # csv_file = open("HotLaunchTime.csv", "w")
        # writer = csv.writer(csv_file)
        # writer.writerows(self.all_data)
        # csv_file.close()
        with open("HotLaunchTime.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(self.all_data)


if __name__ == "__main__":
    controller = Controller(10)
    controller.run()
    controller.save_data_to_csv()
