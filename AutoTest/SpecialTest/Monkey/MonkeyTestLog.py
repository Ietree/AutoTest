#!/usr/bin/python3
# encoding:utf-8


import os
import time


class MonkeyTestLog(object):

    def __init__(self):
        """ init """

    # monkey命令，packageName包名，interval间隔时间单位ms ，frequency执行次数
    def monkey_app(self, packageName, interval, frequency):
        try:
            os.popen(
                "adb shell monkey -p %s --throttle %s --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --monitor-native-crashes -v -v -v %s >/monkeyLog\monkeyScreenLog.log" % (
                    packageName, interval, frequency), 'w')

        except Exception as e:
            print(e)


    # 导出日志
    def copy_error_log(self):
        try:
            anr = "E:\\monkeyLog\\anr"
            if not os.path.isdir(anr):
                os.makedirs(anr)
            dontpanic = "E:\\monkeyLog\\dontpanic"
            if not os.path.isdir(dontpanic):
                os.makedirs(dontpanic)
            tombstones = "E:\\monkeyLog\\tombstones"
            if not os.path.isdir(tombstones):
                os.makedirs(tombstones)
            bug_reports = "E:\\monkeyLog\\bugreports"
            if not os.path.isdir(bug_reports):
                os.makedirs(bug_reports)
            os.popen("adb pull /data/anr  E://monkeyLog//anr", 'r')
            os.popen("adb pull /data/dontpanic  E://monkeyLog//dontpanic", 'r')
            os.popen("adb pull /data/tombstones  E://monkeyLog//tombstones", 'r')
            os.popen("adb pull /data/data/com.android.shell/files/bugreports  E://monkeyLog//bugreports", 'r')
        except Exception as e:
            print(e)


if __name__ == "__main__":
    packageName = "dji.go.v5"
    myApp = MonkeyTestLog()
    myApp.monkey_app(packageName, 500, 100)
    # 判断是否执行完成，执行完成后导出日志
    for i in range(1, 1000000):
        monkey_log = open("E:/monkeyLog/monkeyScreenLog.log", "w+")
        try:
            temp = monkey_log.read()
        finally:
            monkey_log.close()
        if temp.count("Monkey finished") > 0:
            myApp.copy_error_log()
            break
        else:
            time.sleep(2)
