#!/usr/bin/python3
# encoding:utf-8
import os


class MonkeyScript:
    def push_script_to_phone(self):
        cmd = "adb push Pilot.txt /sdcard"
        os.popen(cmd)

    def exec_script(self):
        # 日志保存地址
        logs_location = "MonkeyScript.txt"
        cmd = "adb shell monkey -f /sdcard/Pilot.txt -v 1 > %s" % logs_location
        os.popen(cmd)


if __name__ == "__main__":
    monkeyScript = MonkeyScript()
    monkeyScript.push_script_to_phone()
    monkeyScript.exec_script()
