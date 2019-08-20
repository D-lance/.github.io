__author__ = 'dingxinhui'
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from encapsulation.encapsulation import UIHandle
from picture.report_picture import *
from constant.desired_caps_1 import *

"""遍历我的页面"""


def services():
    # 调用desired_caps的app配置项
    driver = webdriver.Remote('http://localhost:4723/wd/hub', config())

    # 传入driver对象
    ui_handle = UIHandle(driver)

    ui_handle.Click('我的', '我的')

    ui_handle.Swipe(500, 1500, 500, 700)
    ui_handle.Click('我的', '签到领钱')
    ui_handle.Click('我的', '签到领钱返回')
    ui_handle.Click('我的', '充值中心')
    ui_handle.Click('我的', '充值中心返回')
    ui_handle.Click('我的', '收货地址')
    ui_handle.Click('我的', '收货地址返回')
    ui_handle.Click('我的', '帮助与客服')
    ui_handle.Click('我的', '帮助与客服返回')
    ui_handle.Click('我的', '售后规则')
    ui_handle.Click('我的', '售后规则返回')
    ui_handle.Click('我的', '扫一扫')
    ui_handle.Allow(driver, 3)
    ui_handle.Click('我的', '扫一扫返回')
    ui_handle.Click('我的', '系统设置')
    ui_handle.Click('我的', '系统设置返回')


    # name = driver.find_element_by_xpath('//*[@text="新增服务号"]').text
    # 定义截图方法
    img = get_screenshot(driver)

    ui_handle.quit()
    # 定义数组a，包含name和img
    a = [img]
    return a
