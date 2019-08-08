# -*- coding: utf-8 -*-
#用于实现智能等待页面元素的出现

from selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitUtil(object):
    def __init__(self,driver):
        self.locationTypeDic ={
            "xpath":By.XPATH,
            "id":By.ID,
            "name":By.NAME,
            "class_name":By.CLASS_NAME,
            "tag_name":By.TAG_NAME,
            "link_text":By.LINK_TEXT,
            "partial_link_text":By.PARTIAL_LINK_TEXT
        }
        self.driver=driver
        self.wait = WebDriverWait(self.driver,30)

    def presenceOfElementLocated(self,locationType,locatorExpression,*arg):
        '''显式等待页面元素出现在DOM中，但并不一定可见，存在则返回该页面元素对象'''
        try:
            if self.locationTypeDic.has_key(locationType.lower()):
                self.wait.until(
                    EC.presence_of_element_located((
                        self.locationTypeDic[locationType.lower()],
                        locatorExpression
                    ))
                )
            else:
                raise TypeError(u"未找到定位方式，请确认定位方法是否写正确")
        except Exception,e:
            raise e


    def frameToBeAvailableAndSwitchToIt(self,locationType,locatorExpression,*arg):
        '''
        检查frame是否存在，存在则切换进frame控件中
        :param locationType:
        :param locatorExpression:
        :return:
        '''
        try:
            self.wait.until(
                EC.frame_to_be_available_and_switch_to_it
                            ((self.locationTypeDic[locationType.lower()],
                              locatorExpression)))
        except Exception,e:
            raise e

    def visibilityOfElementLocated(self,locationType,locatorExpression,*arg):
        '''显式等待页面元素的出现'''
        try:
            self.wait.until(
                EC.visibility_of_element_located((
                    self.locationTypeDic[locationType.lower()],
                    locatorExpression)))
            #return element
        except Exception,e:
            raise e


if __name__ =="__main__":
    from selenium import webdriver
    driver= webdriver.Firefox(executable_path="C:\\WebDriver\\geckodriver")
    driver.get("http://mail.126.com")
    waitUtil=WaitUtil(driver)

    waitUtil.frameToBeAvailableAndSwitchToIt('xpath',"//iframe[@name='']")

    #e = waitUtil.visibilityElementLocated('xpath',"//input[@name='email']")

    waitUtil.visibilityOfElementLocated('xpath', "//input[@placeholder='邮箱帐号或手机号' and @name='email']")

    waitUtil.presenceOfElementLocated("xpath","//input[@name='email']")
    #e.send_keys("success")
    driver.quit()