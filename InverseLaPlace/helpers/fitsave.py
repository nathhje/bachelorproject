# -*- coding: utf-8 -*-
"""
Retrieves lists for reflectance and absorption coefficient for a certain radial
distance from the data set and saves these lists to an excel file.
"""

import xlwt

def fitSave(prop):
    
    # Retrieve the lists
    prop.retrieveData()
    
    # Make the excel file
    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet("Sheet 1")
    
    for i in range(len(prop.mualist)):
        
        sheet1.write(i, 0, prop.mualist[i])
        sheet1.write(i, 1, prop.reflections[i])
        
    book.save("reflectancevsmua.xls")