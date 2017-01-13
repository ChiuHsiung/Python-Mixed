# -*- coding: utf-8 -*-
# PickleTest.py created by zhuangqiuxiong on 2017/1/13.
__author__ = 'zhuangqiuxiong'

'''

数据保存在pickle中
缺点:数据提取的次序和保存的次序相关,大多数情况下需要一个对象保存在一个pickle文件中

'''

import pickle

class PKClass:

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return str('PKClass->name: {0}'.format(self.name))

if __name__ == "__main__":

    #Save
    dbfile = open('pickle_db', 'wb')
    pickle_object1 = PKClass('zhqiux')
    pickle_object2 = PKClass('zhqiux 2')
    pickle.dump(pickle_object1, dbfile)#支持类型:包括列表,字典,类实例,嵌套结构
    pickle.dump(pickle_object2, dbfile)  # 支持类型:包括列表,字典,类实例,嵌套结构

    dbfile.close()

    #Load
    dbfile = open('pickle_db', 'rb')
    load_data = pickle.load(dbfile)
    print(load_data)
    load_data = pickle.load(dbfile)
    print(load_data)
    dbfile.close()


