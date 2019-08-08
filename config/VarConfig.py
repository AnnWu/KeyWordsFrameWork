# -*- coding: utf-8 -*-
#用于定义整个框架中所需的一些全局常量值，方便维护
import os
ieDriverFilePath="C:\WebDrivers\geckodriver"
chromeDriverFilePath="C:\WebDrivers\chromedriver"
firefoxDriverFilePath="C:\WebDrivers\geckodriver"

parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

screenPictureDir = parentDirPath + "\\exceptionpictures\\"

dataFilePath = parentDirPath+ u"\\testData\\126邮箱发送邮件.xlsx"

#用例表部分列对应的序号
testCase_testCaseName = 2
testCase_testStepSheetName = 4
testCase_isExcute = 5
testCase_runTime = 6
testCase_testResult = 7

#步骤表中，部分列对应的数字序号
testStep_testStepDescribe = 2
testStep_keyWords = 3
testStep_loactionType = 4
testStep_locatorExpression = 5
testStep_operateValue = 6
testStep_runTime = 7
testStep_testResult = 8
testStep_errorInfo = 9
testStep_errorPic = 10

