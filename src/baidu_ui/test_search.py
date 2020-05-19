#-*- conding:utf-8 -*-
import pytest
import xlrd
from selenium import webdriver
from time import sleep, ctime
import os
from .const import *

class Test_baidu_search():
    def test_search_from_excel(self,excel_dir=EXCEL_DIR):
        
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        #将excel文件打开
        excel_file=xlrd.open_workbook(EXCEL_DIR)
        #获取第一个sheet脚本
        sheet = excel_file.sheet_by_index(0)
        #获取第一列数据，并返回列表,下标是从0开始的，第一个也就是0
        cols=sheet.col_values(0)
        print(cols)
        #遍历列表，拿取数据作为测试输入
        for query in cols:
            driver.find_element_by_id("kw").clear()
            #clear，每次过后进行清空
            driver.find_element_by_id("kw").send_keys(str(query))
            #进行str转换，只接受str格式
            driver.find_element_by_id("su").click()
            sleep(2)
            
        driver.quit()
    def test_ssss(self):
        #todo ........
        print("1111111111111111111111")
        assert   1==1
    
    def test_failed(self):
        print("2222222222222222222222222")
        assert 1==8