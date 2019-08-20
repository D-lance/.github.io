__author__ = 'dingxinhui'
# -*-coding:utf-8-*-
import os
import time
# 截图函数


def insert_img(driver, file_name):
    # 获得当前时间的列表  年月日
    now = time.strftime('%Y-%m-%d')
    # 定义截图路径
    PATH = '/Users/apple/Documents/work/uiauto/android_mb/picture/photo'
    print(PATH)
    setpath = PATH+'/'+now
    print(setpath)
    try:
        if os.path.exists(setpath):
            # print(u"文件已存在")
            pass
        else:
            os.mkdir(PATH+'/'+now)
            # os.chdir(path+'\\'+now)
    except Exception as e:
        print(e)

    now2 = time.strftime('%Y-%m-%d_%H_%M_%S_')
    file_path = setpath + '/' + 'picture_' + now2 + file_name
    driver.get_screenshot_as_file(file_path)
