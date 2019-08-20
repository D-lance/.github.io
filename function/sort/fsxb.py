__author__ = 'dingxinhui'
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# function/test_a_login.py
# 业务功能脚本（用例脚本可调用此处的功能脚本）

from encapsulation.encapsulation import UIHandle
from picture.report_picture import *
from constant.desired_caps_1 import *

"""分类 - 服饰箱包"""


def fsxb():
    # 调用desired_caps的app配置项
    driver = webdriver.Remote('http://localhost:4723/wd/hub', config())

    # 传入driver对象
    ui_handle = UIHandle(driver)

    ui_handle.Click('分类', '分类分类')
    ui_handle.Click('分类', '服饰箱包')
    ui_handle.Click('分类', '服饰箱包-女装')
    ui_handle.Click('分类', '服饰箱包-男装')
    ui_handle.Click('分类', '服饰箱包-返回')

    # name = driver.find_element_by_xpath('//*[@text="家庭圈"]').text
    # 定义截图方法
    img = get_screenshot(driver)

    ui_handle.quit()
    # 定义数组a，包含name和img
    a = [img]
    return a
