# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 10:03:24 2018

@author: Gebruiker
"""

import helpers.calculateValues as cv
import numpy as np
import helpers.output as output

def runAlgorithm(N, formula):
    
    V = cv.V(N)
    
    T = []
    Fa = []
    
    for i in np.arange(0.01, 10., 0.01):
        
        T.append(i)
        Fa.append(cv.F(V, N, i, formula))
    
    output.numVsAn(T, Fa)