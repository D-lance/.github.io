__author__ = 'dingxinhui'
# !/usr/bin/env python
# -*-coding:utf-8-*-
from appium import webdriver
import os


def config():
    PATH = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)), x)
    desired_caps = {}
    desired_caps['app'] = PATH('zhihuiebao.apk')
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.0'
    desired_caps['deviceName'] = 'HMKNW17929029793'
    desired_caps['appPackage'] = 'com.jianbao.doctor'
    desired_caps['appActivity'] = '.activity.SplashActivity'
    desired_caps["newCommandTimeout"] = 600
    desired_caps['noSign'] = True
    desired_caps['noReset'] = True
    desired_caps["unicodeKeyboard"] = True
    desired_caps["resetKeyBoard"] = True
    # desired_caps["automationName"] = 'uiautomator2'
    return desired_caps
    # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    #
    # return driver