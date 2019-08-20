from constant.getPhoneName import getPhoneName

__author__ = 'dingxinhui'
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from encapsulation.encapsulation import UIHandle
from picture.report_picture import *
from constant.desired_caps_1 import *

"""遍历我的页面 足迹一栏"""


def message():
    # 调用desired_caps的app配置项
    driver = webdriver.Remote('http://localhost:4723/wd/hub', config())

    # 传入driver对象
    ui_handle = UIHandle(driver)

    ui_handle.Click("消息", "首页消息")
    ui_handle.Click("消息", "查看奖励消息")
    ui_handle.Click("消息", "消息返回")
    ui_handle.Click("消息", "查看店铺访问消息")
    ui_handle.Click("消息", "消息返回")
    ui_handle.Click("消息", "查看系统消息")
    ui_handle.Click("消息", "消息返回")
    ui_handle.Click("消息", "查看客服消息")
    ui_handle.Click("消息", "客服消息返回")
    ui_handle.Click("消息", "查看物流消息")
    ui_handle.Click("消息", "消息返回")


    # name = driver.find_element_by_xpath('//*[@text="新增服务号"]').text
    # 定义截图方法
    img = get_screenshot(driver)

    ui_handle.quit()
    # 定义数组a，包含name和img
    a = [img]
    return a
