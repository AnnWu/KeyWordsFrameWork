# -*- coding: utf-8 -*-
#用于编写具体的测试逻辑代码
from action.PageAction import *
#from util.ParseExcel import ParseExcel
#from config.VarConfig import *
import time
#import traceback

def TestSendMailWithAttachment():
    open_browser("FireFox")

    maximize_browser()

    visit_url("http://mail.126.com")
    sleep(6)

    assert_string_in_pagesource(u"126网易免费邮")

    waitFrameToBeAvailableAndSwitchToIt('xpath',"//iframe[@name='']")

    input_string('xpath',"//input[@name='email']","minwu126")

    input_string('xpath', "//input[@name='password']", "wuli8228680")

    click("id","dologin")

    sleep(10)

    assert_title(u"网易邮箱")
    print (u"登录成功")
    sleep(5)

    switch_to_default_content() #

    waitVisibilityOfElementLocated("xpath","//span[text()='写 信']")

    click("xpath","//span[text()='写 信']")

    print (u"开始写信")
    input_string("xpath",
                 "//div[contains(@id,'_mail_emailinput')]/input",u"757693255@qq.com")

    print (u"输入邮件主题")
    input_string("xpath",
                 "//div[@aria-label='邮件主题输入框，请输入邮件主题']/input",u"新邮件")
    sleep(10)
    print (u"点击上传附件按钮")

    #waitVisibilityOfElementLocated("xpath", "//div[@title='点击添加附件']/input[@size='1' and @type='file']")
    #click("xpath","//div[@title='点击添加附件' and contains(@id,'attachBrowser')]/input")
    #click("xpath","//div[@title='点击添加附件']/input[@size='1' and @type='file']")


    #上传附件类型为input,直接使用send_keys()方法
    input_string("xpath","//div[@title='点击添加附件']/input[@size='1' and @type='file']",u"d:\\a.txt")

    sleep(5)

    print (u"上传附件")
    #paste_string(u"d:\\a.txt")

    #press_enter_key()

    waitFrameToBeAvailableAndSwitchToIt("xpath","//iframe[@tabindex=1]")
    print u"写入邮件正文"

    input_string("xpath","/html/body",u"发给未来自己的一封信")

    switch_to_default_content()
    print (u"写信完成")
    click("xpath","//header//span[text()='发送']")

    sleep(3)

    assert_string_in_pagesource(u"发送成功")

    sleep(3)

    close_browser()

if __name__=="__main__":
    TestSendMailWithAttachment()