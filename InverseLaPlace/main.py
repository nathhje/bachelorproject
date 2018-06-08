# -*- coding: utf-8 -*-
"""
Created on Tue May 29 10:29:46 2018

@author: Gebruiker
"""

import sys
import classes.properties as properties

def main():
    
    prop = properties.Properties()
    
    if sys.argv[1] == "exponential":
        
        prop.formula = "exponential"
        
        prop.algorithm()
        
        prop.numVsAn()
        
    if sys.argv[1] == "dataset":
        
        prop.retrieveData()
        
        prop.formula = "dataset"
        
        prop.algorithm()
        
        prop.algorithmOutcome()
    
if __name__ == "__main__":
    main()