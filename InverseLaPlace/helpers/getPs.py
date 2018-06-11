# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 09:45:50 2018

@author: navansterkenburg
"""

import math

def exponential(s, prop):
    
    return 1 / (s+1)

def reflectance(s, prop):
    
    mua = s
    
    #self.mus = 10.
    g = 0.8
    #self.muc = (1 - self.g) * self.mus
    muc = 10.
    mus = muc / (1 - g)
        
    # The refractive indices.
    nin = 1.
    nuit = 1.
    n = nin / nuit
    
    # All parameters used in calculation
    a = muc / (mua + muc)
        
    ueff = mua * (3. / (1 - a)) ** 0.5
    rid = -1.44 * n ** -2 + 0.71 * n ** -1 + 0.67 + 0.0636 * n
        
    k = (1 + rid) / (1 - rid)
    D = (3 * (mua + muc)) ** -1
        
    z0 = (mua + muc) ** -1
    zb = 2 * k * D
    
    rho1 = (z0 ** 2 + prop.r ** 2) ** 0.5
        
    rho2 = ((z0 + 2*zb) ** 2 + prop.r**2) ** 0.5
    
    return (z0 * (ueff + rho1 ** -1) * math.exp( -ueff * rho1) 
            / (rho1 ** 2) + (z0 + 2 * zb) * (ueff + rho2 ** -1) 
            * math.exp( -ueff * rho2) / (rho2 ** 2)) / 4 / math.pi

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