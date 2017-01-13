# -*- coding: utf-8 -*-
# ShelvesTest.py created by zhuangqiuxiong on 2017/1/13.
__author__ = 'zhuangqiuxiong'

'''

数据保存在shelve中
优点: 对象根据key来保存,多个对象可保存在同一文件中,且读取顺序跟保存顺序无关

'''

import shelve

if __name__ == "__main__":

    #Save
    db = shelve.open('shelve_db')
    db['name'] = 'zhqiux'
    db.close()

    #Load
    db = shelve.open('shelve_db')
    print(db['name'])
    db.close()