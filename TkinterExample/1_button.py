# -*- coding: utf-8 -*-
# 1_button.py created by zhuangqiuxiong on 2017/1/19.
__author__ = 'zhuangqiuxiong'

from tkinter import *
from tkinter.messagebox import showinfo

def reply():
    showinfo(title="Popup", message="Button pressed!")

if __name__ == "__main__":

    window = Tk()
    button = Button(window, text='press', command=reply)
    button.pack()
    window.mainloop()

