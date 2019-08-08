# -*- coding: utf-8 -*-

#用于实现定位页面元素

from selenium.webdriver.support.ui import WebDriverWait

#获取单个页面元素对象
def getElement(driver,locationType,locationExpression):
    try:
        element = WebDriverWait(driver,30).until\
            (lambda x:x.find_element(by=locationType,value=locationExpression))
        return element
    except Exception,e:
        raise e

def getElements(driver,locationType,locationExpression):
    try:
        element = WebDriverWait(driver,30).until\
            (lambda x:x.find_elements(by=locationType,value=locationExpression))
        return element
    except Exception,e:
        raise e

if __name__ =="__main__":
    from selenium import webdriver
    driver= webdriver.Firefox(executable_path="C:\WebDriver\geckodriver.exe")
    driver.get("http://www.baidu.com")
    searchBox = getElement(driver,"id","kw")
    print searchBox.tag_name
    aList = getElements(driver,"tag name","a")
    print len(aList)
    driver.quit()