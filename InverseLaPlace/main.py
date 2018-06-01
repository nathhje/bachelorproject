# -*- coding: utf-8 -*-
"""
Created on Tue May 29 10:29:46 2018

@author: Gebruiker
"""

import calculateValues as cv
import retrieveData as rd

def main(r):
    
    N = 20
    
    delta = 0.001
    #mualist, reflections = rd.retrieveData(r, delta)
    
    V = cv.V(N)
    
    #Fa = cv.F()
    
    
    
if __name__ == "__main__":
    r = 0.5
    main(r)