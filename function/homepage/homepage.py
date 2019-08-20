__author__ = 'dingxinhui'
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from encapsulation.encapsulation import UIHandle
from picture.report_picture import *
from constant.desired_caps_1 import *

"""遍历首页页面分栏"""


def homepage():
    # 调用desired_caps的app配置项
    driver = webdriver.Remote('http://localhost:4723/wd/hub', config())

    # 传入driver对象
    ui_handle = UIHandle(driver)
    ui_handle.Click('首页', '会员PLUS')
    ui_handle.Click('首页', '会员plus')
    ui_handle.Click('首页', '美妆个护')
    ui_handle.Click('首页', '全球美食')
    ui_handle.Click('首页', '家居百货')
    ui_handle.Click('首页', '轻奢名品')
    ui_handle.Click('首页', '全球母婴')
    ui_handle.Click('首页', '滋补保健')
    ui_handle.Click('首页', '服饰鞋包')
    ui_handle.Click('首页', '旅游出行')
    ui_handle.Click('首页', '贵必赔')

    # name = driver.find_element_by_xpath('//*[@text="新增服务号"]').text
    # 定义截图方法
    img = get_screenshot(driver)

    ui_handle.quit()
    # 定义数组a，包含name和img
    a = [img]
    return a
