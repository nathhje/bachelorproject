# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 10:01:39 2018

@author: navansterkenburg
"""

import math
import helpers.analyticalvalues as av

def exponential(T, prop):
    
    return math.exp(-T)

def cosine(T, prop):
    
    return math.cos(T)

def reflectance(T, prop):
    
    # speed of light
    c = 299792458
    l = T
    values = av.analyticalValues(prop.r, 0.0)
    
    c1 = c / (8 * (math.pi * values.D) ** 1.5)
    
    return 1 * l ** (-2.5) * (values.z0 * math.exp(- values.rho1**2 / (4 * values.D * l)) + (values.z0 + 2 * values.zb) * math.exp(- values.rho2**2 / (4 * values.D * l)))