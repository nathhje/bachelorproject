# -*- coding: utf-8 -*-
"""
Retrieves lists for reflectance and absorption coefficient for a certain radial
distance from the data set and saves these lists to an excel file.
"""

import xlwt
import csv

def fitSave(prop):
    
    # Retrieve the lists
    prop.retrieveData()
    
    # Make the excel file
    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet("Sheet 1")
    
    sheet1.write(0,0, "mu_a")
    sheet1.write(0,1, "reflectance")
    
    for i in range(len(prop.mualist)):
        
        sheet1.write(i+1, 0, prop.mualist[i])
        sheet1.write(i+1, 1, prop.reflections[i])
        
    book.save("reflectancevsmuaforr" + str(prop.r) + ".xls")
        
    filename = 'pathlengthforr' + str(prop.r) + '.csv'
        
    with open(filename, 'a', newline = '') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        
        for i in range(len(prop.weights)):
            writer.writerow([prop.weights[i], prop.pathlengths[i]])
            
        
    