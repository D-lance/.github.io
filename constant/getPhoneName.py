import os
import re

"""
返回多个Device列表，单个设备时多出一个空格，比较时判断读出的device是否在它里面
"""


def getPhoneName():
    udid = os.popen('adb devices').read()
    print(udid)
    # 通过正则表达式获取到每一个设备udid，strip去掉udid前后的空格、换行
    # for item in re.findall(r"\n.*\t", udid):
    for item in re.findall(r"\n.*\t", udid):
        _udid = str(item.strip())
        deviceName = os.popen('adb -s {} shell getprop ro.product.model'.format(_udid)).read()
        # print(deviceName)
        return deviceName


"""
返回一个Device，比较时判断读出的device是否相等
"""


def getDeviceId():
    # 读取设备 id
    driverId = os.popen('adb devices').read()
    print(driverId)
    readDeviceId = list(os.popen('adb devices').readlines())
    # print(readDeviceId)
    if driverId is None:
        print("请接入设备或者设备不识别")
    else:
        # 正则表达式匹配出 id 信息
        deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
        # print(deviceId)
        return deviceId


print(getPhoneName())
phoneName = 'PRA-AL00'
if phoneName in getPhoneName():
    print("设备匹配正常")
else:
    print("设备匹配错误")

"""
print(len(name1))
print(len(getPhoneName()))
name = 'HMKNW17929029793'

if getDeviceId() == name:
    print("设备匹配政策")
else:
    print("设备匹配错误")
print(getDeviceId())
"""


