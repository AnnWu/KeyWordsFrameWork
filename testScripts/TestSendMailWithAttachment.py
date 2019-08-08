# -*- coding: utf-8 -*-
#用于编写具体的测试逻辑代码
from action.PageAction import *
from util.ParseExcel import ParseExcel
from config.VarConfig import *
import time
import traceback
from util.Log import *

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

excelObj = ParseExcel()
excelObj.loadWorkBook(dataFilePath)

def writeTestResult(sheetObj,rowNo,colsNo,testResult,errorInfo=None,picPath=None):
    colorDict={'pass':"green",'faild':"red"}

    colsDict ={
        "testCase":[testCase_runTime,testCase_testResult],
        "caseStep":[testStep_runTime,testStep_testResult]}

    try:
        excelObj.writeCellCurrenTime(sheetObj,rowNo=rowNo,colNo=colsDict[colsNo][0])

        excelObj.writeCell(sheetObj,content=testResult,rowNo=rowNo,\
                           colNo=colsDict[colsNo][1],style= colorDict[testResult])
        if errorInfo and picPath:
            #写入异常信息，测试步骤执行失败时
            excelObj.writeCell(sheetObj,content=errorInfo,rowNo=rowNo,\
                           colNo=testStep_errorInfo)
            #写异常截图
            excelObj.writeCell(sheetObj, content=picPath, rowNo=rowNo, \
                       colNo=testStep_errorPic)

        else:
            #写入异常信息，测试步骤执行失败时
            excelObj.writeCell(sheetObj,content="",rowNo=rowNo,\
                           colNo=testStep_errorInfo)
            #写异常截图
            excelObj.writeCell(sheetObj, content="", rowNo=rowNo, \
                       colNo=testStep_errorPic)

    except Exception,e:
        print u"写excel 出错",traceback.print_exc()
        logging.debug(u"写excel出错%s"%traceback.print_exc())


def TestSendMailWithAttachment():

    try:
        caseSheet = excelObj.getSheetByName(u"测试用例")

        isExecuteColumn= excelObj.getColumn(caseSheet,testCase_isExcute)

        successfulCase = 0
        requiredCase = 0
        for idx,i in enumerate(isExecuteColumn[1:]):
            #用例sheet中的第一行为标题行，无须执行
            if i.value.lower()=='y':
                requiredCase +=1

                caseRow = excelObj.getRow(caseSheet,idx+2)

                caseStepSheetName = caseRow[testCase_testStepSheetName-1].value

                stepSheet = excelObj.getSheetByName(caseStepSheetName)
                stepNum = excelObj.getRowsNumber(stepSheet)
                #记录测试用例i的步骤成功数
                successfulSteps = 0
                print (u"开始执行用例'%s'"%caseRow[testCase_testCaseName-1].value)
                logging.info(u"开始执行用例'%s'"%caseRow[testCase_testCaseName-1].value)

                for step in xrange(2,stepNum+1):
                    stepRow = excelObj.getRow(stepSheet,step)

                    #获取步骤的关键字作为调用的函数名
                    keyWord = stepRow[testStep_keyWords-1].value
                    print keyWord
                    locationType = stepRow[testStep_loactionType-1].value
                    locatorExpression = stepRow[testStep_locatorExpression - 1].value

                    operteValue =  stepRow[testStep_operateValue-1].value

                    if isinstance(operteValue,long):
                        operteValue=str(operteValue)

                    expressionStr = "" #构造需要执行的python 表达式
                    if keyWord and operteValue and\
                                    locationType is None and locatorExpression is None:
                        expressionStr = keyWord.strip()+"(u'"+operteValue+"')"

                    elif keyWord and operteValue is None and \
                                    locationType is None and locatorExpression is None:
                        expressionStr = keyWord.strip() + "()"

                    elif keyWord and operteValue and \
                         locationType and locatorExpression is None:
                        expressionStr = keyWord.strip() + \
                                        "('"+locationType.strip()+"',u'"+operteValue+"')"
                    elif keyWord and operteValue and \
                         locationType and locatorExpression:
                        expressionStr = keyWord.strip() + \
                                    "('" + locationType.strip() + "','"+\
                                    locatorExpression.replace("'",'"').strip()+\
                                    "',u'" + operteValue + "')"

                    elif keyWord and locationType \
                            and locatorExpression and operteValue is None:
                        expressionStr = keyWord.strip() + \
                                    "('" + locationType.strip() + "', '" + \
                                    locatorExpression.replace("'", '"').strip()+ "')"

                    print expressionStr

                    try:
                        eval(expressionStr)
                        excelObj.writeCellCurrenTime(
                            stepSheet,
                            rowNo=step,
                            colNo=testStep_runTime)
                    except Exception ,e:
                        #截取异常屏幕截图
                        capturePic=capture_screen()
                        #获取详细的异常堆栈信息
                        errorInfo = traceback.format_exc()

                        writeTestResult(stepSheet,step,"caseStep","faild",errorInfo,capturePic)
                        #这里失败的步骤是否加1？
                        print (u"步骤'%s'执行失败！"%stepRow[testStep_testStepDescribe-1].value)
                        logging.info(u"步骤'%s'执行失败,错误信息：%s"%(stepRow[testStep_testStepDescribe-1].value,errorInfo))
                    else:
                        writeTestResult(stepSheet, step, "caseStep", "pass")
                        successfulSteps+=1
                        print (u"步骤'%s'执行通过！" % stepRow[testStep_testStepDescribe - 1].value)
                        logging.info(u"步骤'%s'执行通过！" % stepRow[testStep_testStepDescribe - 1].value)
                if successfulSteps == stepNum-1:
                    writeTestResult(caseSheet,idx+2,"testCase","pass")
                    successfulCase += 1

                else:
                    writeTestResult(caseSheet, idx + 2, "testCase", "faild")
        print u"共%d 条用例，%d条需要被执行，本次通过%d条"\
        %(len(isExecuteColumn)-1,requiredCase,successfulCase)
        logging.info(u"共%d 条用例，%d条需要被执行，本次通过%d条."
        %(len(isExecuteColumn)-1,requiredCase,successfulCase))
    except Exception,e:
        print traceback.print_exc()
if __name__=="__main__":
    TestSendMailWithAttachment()