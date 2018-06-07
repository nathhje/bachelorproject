# -*- coding: utf-8 -*-
"""
Created on Tue May 29 10:29:46 2018

@author: Gebruiker
"""

import calculateValues as cv
import retrieveData as rd
import numpy as np
import output

def main(r):
    
    N = 22
    
    delta = 0.001
    #mualist, reflections = rd.retrieveData(r, delta)
    
    V = cv.V(N)
    
    T = []
    Fa = []
    
    for i in np.arange(0.01, 10., 0.01):
        
        T.append(i)
        Fa.append(cv.F(V, N, i))
    
    output.numVsAn(T, Fa)
    
if __name__ == "__main__":
    r = 0.3
    main(r)