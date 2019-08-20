# coding=utf-8

# 此用例用于多条case调试

import unittest

from test_case.case.test_I_search import test_search
from test_case.case.test_1_login import test_login



# 构造测试集
suite = unittest.TestSuite()
suite.addTest(test_login("test_login"))
# suite.addTest(test_mine("test_mine"))
# suite.addTest(test_message("test_message"))
# suite.addTest(test_search("test_search"))



# suite.addTest(Case_02("test_homepage"))
# suite.addTest(Case_03("test_homepage"))
# suite.addTest(Case_04("test_classification"))
# suite.addTest(test_honeycomb("test_honeycomb"))


#suite.addTest(shiyongzhongxin("test_syzx"))

if __name__=='__main__':
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
