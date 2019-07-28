#!/usr/bin/python3
# encoding:utf-8
import os


class MonkeyTest(object):

    def __init__(self, package, cmd):
        self.package = package
        self.cmd = cmd

    def monkey_run(self):
        os.popen(self.cmd)


if __name__ == "__main__":
    """
    adb shell monkey 
    -p com.dji.industry.pilot 运行程序的包名称
    --pct-touch 40 在屏幕某处按下并抬起的操作（ACTION_DOWN、ACTION_UP）
    --pct-motion 25 在屏幕某处的按下、随机移动、抬起的操作，即直线滑动操作（ACTION_DOWN、ACTION_MOVE、ACTION_UP）
    --pct-pinchzoom 5 在屏幕上的两处同时按下，并同时移动，最后同时抬起的操作，即智能机上的放大缩小手势操作
    --pct-rotation 5 模拟的Android手机的横屏和竖屏切换
    --pct-appswitch 10 最大限度上覆盖被测包中全部Activity的一种方法
    --pct-syskeys 5 点击系统保留使用的按键的操作，如点击Home键、返回键、音量调节键等
    -s 1666 重复执行之前的伪随机操作
    --throttle 400 设置间隔 如果你希望在每一个指令之间加上固定的间隔时间(毫秒)
    --ignore-crashes monkey在应用程序崩溃后继续发送事件
    --ignore-timeouts monkey在任何超时错误发生后继续发送事件
    --ignore-security-exceptions monkey在应用程序权限错误发生后继续发送事件
    -v -v 输出日志等级
    2000 执行次数
    1>d:\monkey.log 正常日志输出
    2>d:\error.log 错误日志输出
    """
    # 运行程序的包名称
    package = "com.dji.industry.pilot"
    # Monkey运行次数
    frequency = 10000
    # 每个随机动作之间的间隔时间(毫秒)
    interval = 400
    # adb shell monkey -v 100 1>d:\monkey.log  2>d:\error.log
    # 日志保存地址
    logs_location = "Logs/Monkey_Logs.log"
    # 日志保存地址
    error_logs_location = "Logs/Error_Logs.log"
    cmd = "adb shell monkey -p %s --pct-touch 40 --pct-motion 25 --pct-pinchzoom 5 --pct-rotation 5 --pct-appswitch 10 --pct-syskeys 5 -s 1666 --throttle %d --ignore-crashes --ignore-timeouts --ignore-security-exceptions -v -v %d 1>%s 2>%s"%(package, interval, frequency, logs_location, error_logs_location)
    monkey_test = MonkeyTest(package, cmd)
    monkey_test.monkey_run()
