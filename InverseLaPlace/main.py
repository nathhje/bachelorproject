# -*- coding: utf-8 -*-
"""
Created on Tue May 29 10:29:46 2018

"""

import sys 
import classes.properties as properties
import numpy as np

def main():
    
    prop = properties.Properties()
    
    if sys.argv[1] == "exponential":
        
        prop.formula = "exponential"
        prop.FtFormula = "exponentialFt"
        prop.normalize = 1
        
        prop.algorithm()
        
        prop.PsCompare()
        prop.numVsAn()
        
    if sys.argv[1] == "exponentialNum":
        
        prop.formula = "exponential"
        prop.FtFormula = "exponentialFt"
        prop.normalize = 1
        
        prop.createData()
        
        prop.formula = "dataset"
        
        prop.algorithm()
        
        prop.PsCompare()
        prop.numVsAn()
        
    if sys.argv[1] == "cosine":
        
        prop.formula = "cosine"
        prop.FtFormula = "cosineFt"
        prop.normalize = 1
        
        prop.algorithm()
        
        prop.numVsAn()
        
    if sys.argv[1] == "cosineNum":
        
        prop.formula = "cosine"
        prop.FtFormula = "cosineFt"
        prop.normalize = 1
        
        prop.createData()
        
        prop.formula = "dataset"
        
        prop.algorithm()
        
        prop.PsCompare()
        prop.numVsAn()
        
    if sys.argv[1] == "dataset":
        
        prop.retrieveData()
        
        prop.formula = "dataset"
        
        prop.algorithm()
        
        prop.PsCompare()
        prop.algorithmOutcome()
        
    if sys.argv[1] == "reflectance":
        
        prop.formula = "reflectance"
        prop.FtFormula = "reflectanceFt"
        
        prop.algorithm()
        
        prop.numVsAn()
        
    if sys.argv[1] == "reflectanceNum":
        
        prop.formula = "reflectance"
        prop.FtFormula = "reflectanceFt"
        
        prop.createData()
        
        prop.formula = "dataset"
        
        prop.algorithm()
        
        prop.PsCompare()
        prop.numVsAn()
        
    if sys.argv[1] == "normalize":
        
        normalizelist = []
        
        for r in np.arange(0.3, 0.4, 0.001):
            r = round(r,4)
            prop.r = r
            
            prop.formula = "reflectance"
            prop.FtFormula = "reflectanceFt"
            
            prop.algorithm()
            
            prop.getAnalytical()
            
            normalize = prop.algar / prop.anaar
            
            normalizelist.append(normalize)
            
            print(r, normalize)
            
            prop = properties.Properties()
    
if __name__ == "__main__":
    main()