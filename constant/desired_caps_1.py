__author__ = 'dingxinhui'
# !/usr/bin/env python
# -*-coding:utf-8-*-
from appium import webdriver

def config():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    # desired_caps['platformVersion'] = '7.1.2'
    # desired_caps['deviceName'] = '3cbccec'
    desired_caps['platformVersion'] = '8.0.0'
    desired_caps['deviceName'] = 'xxx'
    desired_caps['appPackage'] = 'xxx'
    desired_caps['appActivity'] = '.ui.activity.index.SplashActivity'
    desired_caps["newCommandTimeout"] = 600
    desired_caps['noReset'] = True
    # desired_caps["unicodeKeyboard"] = True
    # desired_caps["resetKeyBoard"] = True
    desired_caps['noSign'] = True
    desired_caps["automationName"] = 'uiautomator2'
    return desired_caps
    # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    #
    # return driver