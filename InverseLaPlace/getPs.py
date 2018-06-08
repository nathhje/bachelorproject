# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 09:45:50 2018

@author: navansterkenburg
"""

def exponential(s, prop):
    
    return 1 / (s+1)

def dataset(s, prop):
    
    index = s * 5 - 0.5
    
    indexLow = int(index)
    indexHigh = int(round(index))
    
    if indexLow < 0:
        print("low")
        indexLow = 0
        indexHigh = 1
        
    if indexHigh >= len(prop.mualist):
        print("high")
        indexLow = len(prop.mualist) - 2
        indexHigh = len(prop.mualist) - 1
    
    a = (prop.reflections[indexHigh] - prop.reflections[indexLow]) / 0.2
    
    return prop.reflections[indexLow] + a * (s - prop.mualist[indexLow])