__author__ = 'dingxinhui'
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from function.login.login import *
from encapsulation.encapsulation import *
from selenium import webdriver

""" 登录 """


class test_login(unittest.TestCase):

    def setUp(self):

        self.imgs = []

    def tearDown(self):
        pass

    def test_login(self):
        u""" 登录 """
        b = login("17557286170", "1107")
        # b[1]，数组b中的第二个参数，即img
        self.imgs.append(b[0])
        # return True
        # b[0]，数组b中的第一个参数，即name
        # self.assertEqual(b[0], '首页')


if __name__ == "__main__":
    unittest.main()