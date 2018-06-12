# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 10:01:39 2018

@author: navansterkenburg
"""

import math
import helpers.analyticalvalues as av

def exponential(T, prop):
    
   return math.exp(-T)

def reflectance(T, prop):
    
    values = av.analyticalValues(prop.r, T)
    
    return values.z0 * math.exp(- values.rho1**2 / (4 * values.D)) + (values.z0 + 2 * values.zb) * math.exp(- values.rho2**2 / (4 * values.D))