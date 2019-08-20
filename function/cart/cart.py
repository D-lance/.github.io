__author__ = 'dingxinhui'
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from encapsulation.encapsulation import UIHandle
from picture.report_picture import *
from constant.desired_caps_1 import *

"""遍历购物车页面"""


def cart():
    # 调用desired_caps的app配置项
    driver = webdriver.Remote('http://localhost:4723/wd/hub', config())

    # 传入driver对象
    ui_handle = UIHandle(driver)
    ui_handle.Click('购物车', '进入购物车页')
    ui_handle.Click('购物车', '领券')
    ui_handle.Click('购物车', '领券返回')
    # 购物车为空分享提示将商品加入到购物车
    ui_handle.Click('购物车', '分享')
    # 购物车为空时才显示"去逛逛"，点击去逛逛后，页面进入首页
    ui_handle.Click('购物车', '去逛逛')
    ui_handle.Click('购物车', '进入购物车页')
    ui_handle.Click('购物车', '为您推荐')
    ui_handle.Click('购物车', '推荐商品详情页返回')



    # name = driver.find_element_by_xpath('//*[@text="新增服务号"]').text
    # 定义截图方法
    img = get_screenshot(driver)

    ui_handle.quit()
    # 定义数组a，包含name和img
    a = [img]
    return a
