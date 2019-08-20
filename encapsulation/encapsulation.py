__author__ = 'dingxinhui'
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# encapsulation/encapsulation.py

from encapsulation.image import image
# 封装部分维护在此
import os, yaml, time
from log.log import Logger
from selenium.webdriver.support.wait import WebDriverWait
from picture.picture import insert_img
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image, ImageDraw

f = open(os.path.abspath('./config/element_data.yml'), encoding='utf-8')

element_data = yaml.load(f)


class UIHandle:
    logger = Logger()

    # 构造方法，用来接收driver对象
    @classmethod
    def __init__(cls, driver):
        cls.driver = driver

    # 输入地址
    @classmethod
    def get(cls, url):
        cls.logger.loginfo(url)
        cls.driver.get(url)

    # 关闭驱动
    @classmethod
    def quit(cls):
        cls.driver.quit()

    # element对象（还可加入try，截图等。。。）
    @classmethod
    def element(cls, page, element):
        # 加入日志
        cls.logger.loginfo(page)
        # 加入隐性等待
        # 此处便可以传入config_o1中的dict定位参数
        try:
            # el = WebDriverWait(cls.driver, 30).until(EC.presence_of_element_located(locat_config[page][element]))

            # 此配置为读取yaml文件
            el = WebDriverWait(cls.driver, 30).until(EC.presence_of_element_located(element_data[page][element]))
            print("页面‘" + page + "’和元素‘" + element + "’ was found")
            #  加入日志
            cls.logger.loginfo(page + 'OK')
            return el
        except Exception as e:
            print("元素没有找到" + e)
            return insert_img(cls.driver, '找不到元素.png')
        cls.logger.loginfo(page + 'OK')
        return el

    # send_keys方法
    @classmethod
    def Input(cls, page, element, msg):
        el = cls.element(page, element)
        image(el, element, cls)
        el.send_keys(msg)
        time.sleep(1)

    # click方法
    @classmethod
    def Click(cls, page, element):
        el = cls.element(page, element)
        image(el, element, cls)
        el.click()
        time.sleep(1)

    # clear方法
    @classmethod
    def Clear(cls, page, element):
        el = cls.element(page, element)
        image(el, element, cls)
        el.clear()
        time.sleep(2)

    # 滑动方法
    @classmethod
    def Swipe(cls, st, sy, ex, ey):
        """
        滑动
        分别为:起始点x,y。结束点x,y。与滑动速度。滑动默认800
        """
        return cls.driver.swipe(st, sy, ex, ey, duration=1000)
        time.sleep(2)

    # 总是允许
    @classmethod
    def Allow(cls, driver, number=5):

        """
        function:权限弹窗-始终允许
        args:
        1.传driver
        2.number，判断弹窗次数，默认给5次
        其它：
        WebDriverWait里面0.5s判断一次是否有弹窗，1s超时

        """

        for i in range(number):
            loc = ("xpath", "//*[@text='始终允许']")
            try:
                # e = WebDriverWait(driver, 3, 0.5).until(EC.presence_of_element_located(loc))
                e = WebDriverWait(driver, 3).until(EC.presence_of_element_located(loc))

                e.click()
            except Exception as e:
                print(e)
                pass

    @classmethod
    def isElementExist(cls, page, element):
        try:
            cls.element(page, element)
            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def is_text_in_element(cls, locator, text_):
        """返回bool值       text"""
        locator = (cls.page, cls.element)
        try:
            result = WebDriverWait(cls.driver, 30).until(
                EC.text_to_be_present_in_element(locator, text_))
            return result
        except Exception as e:
            print(e)
            return False

    @classmethod
    def setUp(cls):
        cls.imgs = []
        cls.addCleanup(cls.cleanup)
