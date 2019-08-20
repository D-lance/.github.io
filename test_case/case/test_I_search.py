__author__ = 'dingxinhui'
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from function.search.homepage_search import search


class test_search(unittest.TestCase):

    def setUp(self):

        self.imgs = []

    def tearDown(self):
        pass

    def test_search(self):
        u""" 我的 搜索"""
        b = search("衣服")
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