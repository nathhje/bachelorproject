# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 10:58:25 2018

@author: Gebruiker
"""

import xlwt

def fitSave(prop):
    
    prop.retrieveData()
    
    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet("Sheet 1")
    
    for i in range(len(prop.mualist)):
        
        sheet1.write(i, 0, prop.mualist[i])
        sheet1.write(i, 1, prop.reflections[i])
        
    book.save("reflectancevsmua.xls")