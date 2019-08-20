# from config.do_unlock import do_unlock

__author__ = 'dingxinhui'
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# function/test_a_login.py
# 业务功能脚本（用例脚本可调用此处的功能脚本）

from encapsulation.encapsulation import UIHandle
from config.login_config import *
from config.config_01 import *
from picture.report_picture import *
from constant.desired_caps_1 import *
from appium import webdriver


def login(mobile, code):

    # 调用desired_caps的app配置项
    driver = webdriver.Remote('http://localhost:4723/wd/hub', config())

    # 调用encapsulation的定义方法
    ui_handle = UIHandle(driver)
    # driver.implicitly_wait(30)
    # 判断是否是安装后第一次启动，第一次启动是总是"允许"
    # ui_handle.Allow(driver, 3)
    ui_handle.Click("登录", "短信登录")
    ui_handle.Input("登录", "输入手机号码", mobile)
    # 激活验证码
    sendCode()
    ui_handle.Input("登录", "输入短信验证码", code)
    ui_handle.Click("登录", "登录按钮")
    # time.sleep(5)
    text = driver.find_element_by_id("com.ggj.gmj:id/tabMian_tab_indexImg").text
    print(text)
    ui_handle.is_text_in_element(("登录", "首页"), "首页dasds")
    #
    # # 断言登录成功后是否存在首页字符的控件
    # ui_handle.is_text_in_element("登录", "首页", "首页1")


    # 调用登录方法
    # login_config(driver)

    # 定义查找到id的文本值
    # name = driver.find_element_by_xpath("//*[@text='首页' and contains(@resource-id,'tab')]").text

    # driver.find_element_by_xpath("//*[@text='体重管理']").click()
    # 定义截图方法
    img = get_screenshot(driver)
    ui_handle.quit()
    # 定义数组a，包含name和img
    a = [img]
    return a
