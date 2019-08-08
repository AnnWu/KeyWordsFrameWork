# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import traceback

if __name__=="__main__":


    driver = webdriver.Firefox(executable_path='C:\\WebDriver\\geckodriver')
    driver.get('http://mail.126.com')
    try:
        wait = WebDriverWait(driver, 30, 0.2)  # 显示等待
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@name='']"))  # 切换到用户名和密码输入框所在的frame元素
        #driver.switch_to_frame()
        name = wait.until(lambda x: x.find_element_by_xpath("//input[@placeholder='邮箱帐号或手机号'and @name='email']"))
        name.send_keys('username')
        password = wait.until(lambda x: x.find_element_by_xpath("//input[@placeholder='密码']"))
        password.send_keys('passwd')
        submit = wait.until(lambda x: x.find_element_by_xpath("//a[@id='dologin']"))
        submit.click()
    except TimeoutException, e:
        # 捕获TimeoutException异常
        print traceback.print_exc()

    except NoSuchElementException, e:
        # 捕获NoSuchElementException异常
        print traceback.print_exc()

    except Exception, e:
        # 捕获其他异常
        print traceback.print_exc()
