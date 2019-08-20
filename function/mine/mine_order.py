__author__ = 'dingxinhui'
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from encapsulation.encapsulation import UIHandle
from picture.report_picture import *
from constant.desired_caps_1 import *

"""遍历我的页面"""


def order():
    # 调用desired_caps的app配置项
    driver = webdriver.Remote('http://localhost:4723/wd/hub', config())

    # 传入driver对象
    ui_handle = UIHandle(driver)

    ui_handle.Click('我的', '我的')
    ui_handle.Swipe(500, 300, 500, 800)
    ui_handle.Click('我的', '我的订单')
    ui_handle.Click('我的', '我的订单返回')
    ui_handle.Click('我的', '代付款')
    ui_handle.Click('我的', '我的订单返回')
    ui_handle.Click('我的', '待发货')
    ui_handle.Click('我的', '我的订单返回')
    ui_handle.Click('我的', '待收款')
    ui_handle.Click('我的', '我的订单返回')
    ui_handle.Click('我的', '交易完成')
    ui_handle.Click('我的', '我的订单返回')
    ui_handle.Click('我的', '退款货')
    ui_handle.Click('我的', '我的订单返回')

    # name = driver.find_element_by_xpath('//*[@text="新增服务号"]').text
    # 定义截图方法
    img = get_screenshot(driver)

    ui_handle.quit()
    # 定义数组a，包含name和img
    a = [img]
    return a
