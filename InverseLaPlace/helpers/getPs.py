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

def exponent(s, prop):
    
    P = 0.019892974 * math.e ** (-0.651220312*s)
    
    prop.s.append(s)
    prop.Ps.append(P)
    
    return P

def polynomial(s, prop):
    
    constants = [-5.43079E-08,	2.63248E-06,	-5.41409E-05,	0.00061561,	-0.004227447,	0.017989602,	-0.046860681,	0.071184663,	-0.056953756,	0.018767629]
   
    poly = len(constants)
    
    P = 0
    
    for i in range(poly):
        
        P += constants[i] * s ** (poly-1-i)
    
    prop.s.append(s)
    prop.Ps.append(P)
    return P

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
        prop.moreref.append(exponential(s, prop))
        prop.Ps.append(P)

    return P