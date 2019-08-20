__author__ = 'dingxinhui'
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from encapsulation.encapsulation import UIHandle
from picture.report_picture import *
from constant.desired_caps_1 import *

"""遍历我的页面 足迹一栏"""


def footPrint():
    # 调用desired_caps的app配置项
    driver = webdriver.Remote('http://localhost:4723/wd/hub', config())

    # 传入driver对象
    ui_handle = UIHandle(driver)

    ui_handle.Click('我的', '我的')
    ui_handle.Swipe(500, 300, 500, 800)
    ui_handle.Click('我的', '足迹')
    ui_handle.Click('我的', '足迹返回')
    ui_handle.Click('我的', '领券中心')
    ui_handle.Click('我的', '领券中心返回')
    ui_handle.Click('我的', '优惠券')
    ui_handle.Click('我的', '优惠券返回')

    # name = driver.find_element_by_xpath('//*[@text="新增服务号"]').text
    # 定义截图方法
    img = get_screenshot(driver)

    ui_handle.quit()
    # 定义数组a，包含name和img
    a = [img]
    return a
