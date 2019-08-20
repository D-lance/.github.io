
from config.sendCode import sendCode

__author__ = 'dingxinhui'
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# coding:utf-8
import time


def login_config(driver):

    driver.find_element_by_xpath("//*[@text='短信验证码登录']").click()
    # 用户名
    driver.find_element_by_xpath("//*[@text='请输入手机号']").send_keys("xxx")
    time.sleep(2)
    # 发送短信
    sendCode()
    # 密码
    # driver.find_element_by_xpath("//*[@text='请输入短信验证码']").clear()
    driver.find_element_by_xpath("//*[@text='请输入短信验证码']").send_keys("xxx")
    time.sleep(2)
    # driver.back()
    # 登录
    driver.find_element_by_xpath("//*[@text='登录']").click()
    time.sleep(5)
