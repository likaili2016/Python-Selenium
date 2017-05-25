#coding=utf-8

import xlrd
import hashlib
import json
import os
import sys
import logging

def RunTest(TestCaseFile):
       TestCaseFile = os.path.join(os.getcwd(), TestCaseFile)
       if not os.path.exists(TestCaseFile):
           print ('测试用例文件不存在')
           sys.exit()
       TestCase = xlrd.open_workbook(TestCaseFile)
       table = TestCase.sheet_by_index(0)
       errorCase = []  # 用于保存接口返回的内容和http状态码

       s = None
       for i in range(1, table.nrows):
           if table.cell(i, 9).value.replace('\n', '').replace('\r', '')!= 'Yes':
             continue




