# -*- coding: utf-8 -*-
# 2_Entry.py created by zhuangqiuxiong on 2017/1/19.
__author__ = 'zhuangqiuxiong'

from tkinter import *
from tkinter.messagebox import showinfo

def reply(name):
    showinfo(title='Reply', message='Hello {}'.format(name))


if __name__ == "__main__":

    window = Tk()
    window.title = 'Echo'

    Label(window, text='Enter your name:').pack(side=TOP)
    entry = Entry(window)
    entry.pack(side=TOP)
    Button(window, text='Submit', command=(lambda : reply(entry.get()))).pack(side=TOP)

    window.mainloop()
