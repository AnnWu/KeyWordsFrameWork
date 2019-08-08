# -*- coding: utf-8 -*-
#用于实现将数据设置到剪贴板中

import win32con
import win32clipboard as w

class Clipboard(object):
    '''
    模拟Windows设置剪贴板
    '''
    @staticmethod
    def getText():
        #打开剪贴板
        w.OpenClipboard()
        d = w.GetClipboardData(win32con.CF_TEXT)
        w.CloseClipboard()
        return d

    @staticmethod
    def setText(aString):
        #打开剪贴板
        w.OpenClipboard()
        w.EmptyClipboard()#清空剪贴板
        w.SetClipboardData(win32con.CF_UNICODETEXT,aString)

        w.CloseClipboard()