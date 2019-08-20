__author__ = 'dingxinhui'
# !/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import time

from PIL import Image, ImageDraw


def image(el, element, cls):
    # 赋值控件的位置
    locations = el.location
    # 赋值控件的size
    sizes = el.size
    # 控件的宽、高
    rangle = (int(locations['x']), int(locations['y']), int(locations['x'] + sizes['width']),
              int(locations['y'] + sizes['height']))
    # 定义图片存放目录
    now = time.strftime('%Y-%m-%d')
    path = os.path.abspath('./picture/photo')
    setpath = path + '/' + now
    # 判断文件夹是否存在
    try:
        if os.path.exists(setpath):
            # print(u"文件已存在")
            pass
        else:
            os.mkdir(path + '/' + now)
    except Exception as e:
        print(e)

    now1 = time.strftime('%Y-%m-%d_%H_%M_%S_')
    file_path = setpath + '/' + 'picture_' + now1
    # 定义原始图片
    a = setpath + ".png"
    a1 = file_path + element + ".png"
    cls.driver.save_screenshot(a)
    img01 = Image.open(a)
    b = ImageDraw.Draw(img01)
    b.arc(rangle, 0, 360, fill=(255, 0, 0), width=5)
    # b.ellipse(rangle, fill=(0, 0, 255))
    # 保存修改后的图片
    img01.save(a1)
    time.sleep(3)