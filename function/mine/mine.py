__author__ = 'dingxinhui'
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from encapsulation.encapsulation import UIHandle
from picture.report_picture import *
from constant.desired_caps_1 import *
from constant.getPhoneName import getPhoneName

"""遍历我的页面"""


def mine():
    # 调用desired_caps的app配置项
    driver = webdriver.Remote('http://localhost:4723/wd/hub', config())

    # 传入driver对象
    ui_handle = UIHandle(driver)

    ui_handle.Click('我的', '我的')
    ui_handle.Swipe(500, 300, 500, 800)
    ui_handle.Click('我的', '消息')
    ui_handle.Click('我的', '消息页返回')
    ui_handle.Click('我的', '个人资料')
    ui_handle.Click('我的', '个人资料返回')
    ui_handle.Click('我的', '脉宝尊享会员')
    driverName = 'PRA-AL00'
    if getPhoneName() == driverName:
        driver.tap([(822, 532), (1000, 532)], 100)
    else:
        print("请确定接入的手机是否为 'PRA-AL00' ")

    ui_handle.Swipe(500, 300, 500, 800)
    ui_handle.Click('我的', '脉宝尊享会员页面返回')
    ui_handle.Click('我的', '我的收益')
    ui_handle.Click('我的', '我的收益返回')
    ui_handle.Click('我的', '邀请好友')
    ui_handle.Click('我的', '取消分享')
    ui_handle.Click('我的', '分享礼包')
    ui_handle.Click('我的', '分享礼包返回')
    ui_handle.Click('我的', '会员首选')
    ui_handle.Click('我的', '会员首选返回')
    ui_handle.Click('我的', '足迹')
    ui_handle.Click('我的', '足迹返回')
    ui_handle.Click('我的', '领券中心')
    ui_handle.Click('我的', '领券中心返回')
    ui_handle.Click('我的', '优惠券')
    ui_handle.Click('我的', '优惠券返回')
    ui_handle.Click('我的', '我的订单')
    ui_handle.Click('我的', '我的订单返回')
    ui_handle.Click('我的', '代付款')
    ui_handle.Click('我的', '我的订单返回')
    ui_handle.Click('我的', '待发货')
    ui_handle.Click('我的', '我的订单返回')
    ui_handle.Click('我的', '待收款')
    ui_handle.Click('我的', '我的订单返回')
    ui_handle.Click('我的', '交易完成')
    ui_handle.Click('我的', '我的订单返回')
    ui_handle.Click('我的', '退款货')
    ui_handle.Click('我的', '我的订单返回')
    ui_handle.Swipe(500, 1500, 500, 700)
    ui_handle.Click('我的', '签到领钱')
    ui_handle.Click('我的', '签到领钱返回')
    ui_handle.Click('我的', '充值中心')
    ui_handle.Click('我的', '充值中心返回')
    ui_handle.Click('我的', '收货地址')
    ui_handle.Click('我的', '收货地址返回')
    ui_handle.Click('我的', '帮助与客服')
    ui_handle.Click('我的', '帮助与客服返回')
    ui_handle.Click('我的', '售后规则')
    ui_handle.Click('我的', '售后规则返回')
    ui_handle.Click('我的', '扫一扫')
    ui_handle.Allow(driver, 5)
    ui_handle.Click('我的', '始终允许相机权限')
    ui_handle.Click('我的', '扫一扫返回')
    ui_handle.Click('我的', '系统设置')
    ui_handle.Click('我的', '系统设置返回')


    # name = driver.find_element_by_xpath('//*[@text="新增服务号"]').text
    # 定义截图方法
    img = get_screenshot(driver)

    ui_handle.quit()
    # 定义数组a，包含name和img
    a = [img]
    return a
