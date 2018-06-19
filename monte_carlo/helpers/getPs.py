# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 09:45:50 2018

@author: navansterkenburg
"""

import math
import helpers.analyticalvalues as av
import random

def exponential(s, prop):
    
    P = 1 / (s+1)
    Pd = P * (random.random()* 21./110. + 10./11.)
    
    prop.s.append(s)
    prop.moreref.append(P)
    prop.Ps.append(Pd)
    
    return Pd

def cosine(s, prop):
    
    return s / (s ** 2 + 1)

def reflectance(s, prop):
    
    values = av.analyticalValues(prop.r, s)
    
    return (values.z0 * (values.ueff + values.rho1 ** -1) * math.exp( -values.ueff * values.rho1) 
            / (values.rho1 ** 2) + (values.z0 + 2 * values.zb) * (values.ueff + values.rho2 ** -1) 
            * math.exp( -values.ueff * values.rho2) / (values.rho2 ** 2)) / 4 / math.pi

def dataset(s, prop):
    #print("dataset")
    
    index = s * 20
    
    indexLow = int(index)
    indexHigh = int(round(index))
    
    #print(index)
    #print(indexLow)
    #print(indexHigh)
    
    if indexLow < 0:
        indexLow = 0
        indexHigh = 1
        
    if indexHigh >= len(prop.mualist):
        indexLow = len(prop.mualist) - 2
        indexHigh = len(prop.mualist) - 1
    
    a = (prop.reflections[indexHigh] - prop.reflections[indexLow]) / 0.2
    
    #print(prop.reflections[indexLow])
    #print(prop.reflections[indexHigh])
    
    P = prop.reflections[indexLow] + a * (s - prop.mualist[indexLow])
    
    if s < 10000000:
        
        prop.s.append(s)
        #prop.moreref.append(reflectance(s, prop))
        prop.Ps.append(P)

    return P