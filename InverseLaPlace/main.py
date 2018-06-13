# -*- coding: utf-8 -*-
"""
Created on Tue May 29 10:29:46 2018

"""

import sys 
import classes.properties as properties

def main():
    
    prop = properties.Properties()
    
    if sys.argv[1] == "exponential":
        
        prop.formula = "exponential"
        prop.FtFormula = "exponentialFt"
        
        prop.algorithm()
        
        prop.numVsAn()
        
    if sys.argv[1] == "exponentialNum":
        
        prop.formula = "exponential"
        prop.FtFormula = "exponentialFt"
        
        prop.createData()
        
        prop.formula = "dataset"
        
        prop.algorithm()
        
        prop.numVsAn()
        
    if sys.argv[1] == "cosine":
        
        prop.formula = "cosine"
        prop.FtFormula = "cosineFt"
        
        prop.algorithm()
        
        prop.numVsAn()
        
    if sys.argv[1] == "cosineNum":
        
        prop.formula = "cosine"
        prop.FtFormula = "cosineFt"
        
        prop.createData()
        
        prop.formula = "dataset"
        
        prop.algorithm()
        
        prop.numVsAn()
        
    if sys.argv[1] == "dataset":
        
        prop.retrieveData()
        
        prop.formula = "dataset"
        
        prop.algorithm()
        
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
        
        prop.numVsAn()
    
if __name__ == "__main__":
    main()