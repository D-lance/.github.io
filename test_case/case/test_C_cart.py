__author__ = 'dingxinhui'
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from function.cart.cart import *


class test_cart(unittest.TestCase):

    def setUp(self):

        self.imgs = []

    def tearDown(self):
        pass

    def test_cart(self):
        u""" 遍历购物车页面 """

        # page = test_a_login("tpacs001","2wsx1qaZ","123456")
        b = cart()
        # b[0]，数组b中的第二个参数，即img
        self.imgs.append(b[0])
        # return True

        '''
        # b[1]，数组b中的第一个参数，即name
        self.assertEqual(b[1], '家庭圈')
        return True

        '''


if __name__ == "__main__":
    unittest.main()