# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 10:00:00 2018

@author: navansterkenburg
"""

import matplotlib.pyplot as plt
import getFt

def numVsAn(T, Fa):
    
    Ft = []
    
    for i in T:
        
        Ft.append(getFt.exponential(i))
        
    plt.figure()
    plt.plot(T, Fa)
    plt.plot(T, Fa, 'bo')
    plt.plot(T, Ft, 'g-')
    plt.plot(T, Ft, 'go')
    plt.show()