# -*- coding: utf-8 -*-

from selenium import webdriver
from config.VarConfig import ieDriverFilePath
from config.VarConfig import chromeDriverFilePath
from config.VarConfig import firefoxDriverFilePath
from util.ObjectMap import getElement
from util.ClipboardUtil import Clipboard
from util.KeyBoardUtil import KeyBoardKeys
from util.DirAndTime import *
from util.WaitUtil import WaitUtil
from selenium.webdriver.firefox.options import Options
import time

driver = None

waitUtil = None #全局的等待类实例对象

def open_browser(browserName,*args):
    global driver,waitUtil
    try:
        if browserName.lower() == 'ie':
            driver= webdriver.Ie(executable_path = ieDriverFilePath)
        elif browserName.lower() == 'chrome':
            chrome_options= Options()
            #添加屏蔽 --ignore-certificate-errors 提示信息的设置参数项
            chrome_options.add_experimental_option(
                "excludeSwitches",
                ["ignore-certificate-errors"]
            )
            driver = webdriver.Chrome(executable_path=chromeDriverFilePath,
                                      chrome_options=chrome_options)
        else:
            driver=webdriver.Firefox(executable_path=firefoxDriverFilePath)

        waitUtil = WaitUtil(driver)

    except Exception,e:
        raise e


def visit_url(url,*args):
    global driver
    try:
        driver.get(url)
    except Exception,e:
        raise e
def close_browser(*args):
    global driver
    try:
        driver.quit()
    except Exception,e:
        raise e

def sleep(seconds,*args):
    try:
        time.sleep(int(seconds))
    except Exception, e:
        raise e

def clear(locationType,locatorExpression,*args):
    global driver
    try:
        getElement(driver,locationType,locatorExpression).clear()
    except Exception, e:
        raise e

def input_string(locationType,locatorExpression,inputContent):
    global driver
    try:
        getElement(driver,locationType,locatorExpression).send_keys(inputContent)
    except Exception, e:
        raise e

def click(locationType,locatorExpression,*args):
    global driver
    try:
        getElement(driver,locationType,locatorExpression).click()
    except Exception, e:
        print str(e)
        raise e

def assert_string_in_pagesource(assertString,*args):
    global driver
    try:
        assert assertString in driver.page_source,\
            u"%s not found in page source"%assertString
    except AssertionError,e:
        raise AssertionError(e)
    except Exception,e:
        raise e

def assert_title(titleStr,*args):
    global driver
    try:
        print driver.title
        assert titleStr in driver.title,\
            u"%s not found in title"%titleStr
    except AssertionError,e:
        raise AssertionError(e)
    except Exception,e:
        raise e

def getTitle(*args):
    global  driver
    try:
        return driver.title
    except Exception,e:
        raise e


def getPageSource(*args):
    global driver
    try:
        return driver.page_source
    except Exception, e:
        raise e

def switch_to_frame(locationType,frameLocatorExpression,*args):
    global driver
    try:
        driver.switch_to_frame(getElement(driver, locationType, frameLocatorExpression))
    except Exception, e:
        print "Frame error"
        raise e

def switch_to_default_content(*args):
    global driver
    try:
        driver.switch_to_default_content()
    except Exception, e:
        raise e

def paste_string(pastestring,*args):
    #模拟Ctrl +V
    try:
        Clipboard.setText(pastestring)
        time.sleep(2)
        KeyBoardKeys.twoKeys("ctrl","v")
    except Exception,e:
        raise e
def press_tab_key(*args):
    try:
        KeyBoardKeys.oneKey('tab')
    except Exception,e:
        raise e
def press_enter_key(*args):
    try:
        KeyBoardKeys.oneKey('enter')
    except Exception,e:
        raise e

def maximize_browser():
    global driver
    try:
        driver.maximize_window()
    except Exception,e:
        raise e

def capture_screen(*args):
    global driver
    currTime = getCurrentTime()
    picNameAndPath = str(createCurrentDateDir())+"\\"+str(currTime)+".png"
    try:
        driver.get_screenshot_as_file(picNameAndPath.replace('\\',r'\\'))
    except Exception,e:
        raise e
    else:
        return picNameAndPath


def waitPresenceOfElementLocated(locationType, locatorExpression, *arg):
    '''显式等待页面元素出现在DOM中，但并不一定可见，存在则返回该页面元素对象'''
    global waitUtil
    try:
        waitUtil.presenceOfElementLocated(locationType, locatorExpression)
    except Exception, e:
        raise e


def waitFrameToBeAvailableAndSwitchToIt( locationType, locatorExpression, *arg):
    '''
    检查frame是否存在，存在则切换进frame控件中
    :param locationType:
    :param locatorExpression:
    :return:
    '''
    global waitUtil
    try:
        waitUtil.frameToBeAvailableAndSwitchToIt(locationType,locatorExpression)
    except Exception, e:
        raise e

def waitVisibilityOfElementLocated(locationType,locatorExpression,*arg):
    '''显式等待页面元素的出现'''
    global waitUtil
    try:
        waitUtil.visibilityOfElementLocated(locationType,locatorExpression)
    except Exception,e:
        raise e