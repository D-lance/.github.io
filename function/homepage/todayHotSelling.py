__author__ = 'dingxinhui'
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# function/test_a_login.py

from encapsulation.encapsulation import UIHandle
from config.login_config import *
from config.config_01 import *
from picture.report_picture import *
from constant.desired_caps_1 import *

""" 首页-今日热卖 """


def todayHotSelling():
    # 调用desired_caps的app配置项
    driver = webdriver.Remote('http://localhost:4723/wd/hub', config())

    # 传入driver对象
    ui_handle = UIHandle(driver)
    # driver.implicitly_wait(30)

    ui_handle.Click('首页-今日热卖', '滚动栏')
    ui_handle.Click('首页-今日热卖', '滚动栏返回')
    ui_handle.Click('首页-今日热卖', '签到领钱')
    ui_handle.Click('首页-今日热卖', '签到页面返回')
    ui_handle.Click('首页-今日热卖', '热卖榜单')
    ui_handle.Click('首页-今日热卖', '热卖榜单返回')
    ui_handle.Click('首页-今日热卖', '升级会员')
    ui_handle.Click('首页-今日热卖', '升级会员返回')
    ui_handle.Click('首页-今日热卖', '新人专享')
    ui_handle.Click('首页-今日热卖', '新人专享返回')
    ui_handle.Click('首页-今日热卖', '增值服务')
    ui_handle.Click('首页-今日热卖', '增值服务页面返回')
    ui_handle.Swipe(500, 1500, 500, 400)
    ui_handle.Click('首页-今日热卖', '正在疯抢')
    ui_handle.Click('首页-今日热卖', '商品详情页返回')


    # 定义截图方法
    img = get_screenshot(driver)

    ui_handle.quit()
    # 定义数组a，包含name和img
    a = [img]
    return a
