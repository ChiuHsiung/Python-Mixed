# -*- coding: utf-8 -*-
# ShelvesTest.py created by zhuangqiuxiong on 2017/1/13.
__author__ = 'zhuangqiuxiong'

'''

数据保存在shelve中
优点: 对象根据key来保存,多个对象可保存在同一文件中,且读取顺序跟保存顺序无关
缺点: 对象的修改需要再次保存回key中才能生效, 否则改动只会在内存中生效(除非open时用了wirteback=True，但不推荐这种做法)

'''

import shelve

if __name__ == "__main__":

    #Save
    db = shelve.open('shelve_db')#缺省打开方式:需要时创建文件,否则以可读可写的方式打开
    db['name'] = {'first name': 'Qiuxiong', 'last name': 'Zhuang'}
    db.close()

    #Load
    db = shelve.open('shelve_db')
    print(db['name'])
    name_dict = db['name']
    name_dict['first name'] = 'Boss'
    db['name'] = name_dict #如果没有这一步的话, shelve不会更新存储数据


    db.close()