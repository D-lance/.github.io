__author__ = 'dingxinhui'
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from encapsulation.encapsulation import UIHandle
from picture.report_picture import *
from constant.desired_caps_1 import *
import os


"""
搜索
"""


def search(name):
    # 调用desired_caps的app配置项
    driver = webdriver.Remote('http://localhost:4723/wd/hub', config())

    # 传入driver对象
    ui_handle = UIHandle(driver)
    ui_handle.Click("搜索", "首页搜索")
    ui_handle.Input("搜索", "搜索页面搜索", name)
    ui_handle.Click("搜索", "搜索页面搜索")
    # 切换成搜狗输入法
    os.popen("adb shell ime set com.sohu.inputmethod.sogou/.SogouIME")
    # 点击搜索按钮
    driver.press_keycode(66)

    # name = driver.find_element_by_xpath('//*[@text="新增服务号"]').text
    # 定义截图方法
    img = get_screenshot(driver)

    ui_handle.quit()
    # 定义数组a，包含name和img
    a = [img]
    return a
