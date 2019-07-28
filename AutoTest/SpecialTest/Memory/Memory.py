#!/usr/bin/python3
# encoding:utf-8

import csv


# 控制类
class Controller(object):
    def __init__(self):
        # 定义收集数据的数组
        self.all_data = [("id", "VIRT", "RES")]

    # 分析数据
    def analyze_data(self):
        content = self.read_file()
        i = 0
        for line in content:
            if "dji.go.v5" in line:
                print(line)
                line = "#".join(line.split())
                virt = line.split("#")[5]
                res = line.split("#")[6]

                # 将获取到的数据存到数组中
                self.all_data.append((i, virt, res))
                i = i + 1

    # 数据的存储
    def save_data_to_csv(self):
        """
        将数据存入CSV文件中
        """
        with open("meminfo.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(self.all_data)

    # 读取数据文件
    def read_file(self):
        mfile = open("meminfo", "r")
        content = mfile.readlines()
        mfile.close()
        return content


if __name__ == "__main__":
    controller = Controller()
    controller.analyze_data()
    controller.save_data_to_csv()
