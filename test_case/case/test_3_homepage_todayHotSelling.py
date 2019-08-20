__author__ = 'dingxinhui'
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from function.homepage.todayHotSelling import *



class test_todayHotSelling(unittest.TestCase):

    def setUp(self):

        self.imgs = []

    def tearDown(self):
        pass

    def test_todayHotSelling(self):
        u""" 首页 - 今日热卖 """
        # page = test_a_login("tpacs001","2wsx1qaZ","123456")
        b = todayHotSelling()
        # b[1]，数组b中的第二个参数，即img
        self.imgs.append(b[0])
        # return True


        # b[0]，数组b中的第一个参数，即name
        # self.assertEqual(b[0], '首页')


if __name__ == "__main__":
    unittest.main()