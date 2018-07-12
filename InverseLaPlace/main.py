# -*- coding: utf-8 -*-
"""
Performs an inverse Laplace transform on a function based on the algorithm
suggested by Harald Stehfest.

"""

import sys 
import classes.property as properties
import numpy as np
import helpers.fitsave as fs

def main():
    
    prop = properties.Properties()
    
    # Uses the algorithm on a function that has an exponential outcome.
    if sys.argv[1] == "exponential":
        
        # Setting the right functions to be used
        prop.formula = "exponential"
        prop.FtFormula = "exponentialFt"
        prop.normalize = 1
        
        prop.algorithm()
        
        prop.PsOnly()
        prop.numVsAn()
        
    # Uses the algorithm on a function that has an exponential outcome, but Ps
    # has a systemetic deviation
    if sys.argv[1] == "exponentialSys":
        
        # Setting the right functions to be used
        prop.formula = "exponentialSys"
        prop.FtFormula = "exponentialFt"
        prop.normalize = 1
        
        prop.algorithm()
        
        prop.PsCompare()
        prop.numVsAn()
        
    # Uses the algorithm on a function that has an exponential outcome, but Ps
    # has a random deviation
    if sys.argv[1] == "exponentialRand":
        
        # Setting the right functions to be used
        prop.formula = "exponentialRand"
        prop.FtFormula = "exponentialFt"
        prop.normalize = 1
        
        prop.algorithm()
        
        prop.PsCompare()
        prop.numVsAn()
    
    # Uses the algorithm on a function that has an exponential outcome, but Ps
    # is a discrete set of points, and exact values are determined by interpolating
    if sys.argv[1] == "exponentialNum":
        
        # Setting the right functions to be used
        prop.formula = "exponential"
        prop.FtFormula = "exponentialFt"
        prop.normalize = 1
        
        prop.createData()
        
        # Changing the used function to interpolation
        prop.formula = "dataset"
        prop.s = []
        prop.Ps = []
        
        prop.algorithm()
        
        prop.PsCompare()
        prop.numVsAn()
        
    # Uses the algorithm on a function that has a goniometric outcome
    if sys.argv[1] == "cosine":
        
        # Setting the right functions to be used
        prop.formula = "cosine"
        prop.FtFormula = "cosineFt"
        prop.normalize = 1
        
        prop.algorithm()
        
        prop.PsOnly()
        prop.numVsAn()
        
    # Uses the algorithm on a fit to the reflectance vs absorption coefficient 
    # from the data set to get a path length distribution
    if sys.argv[1] == "fit":
        
        # Setting the right functions to be used
        prop.formula = "fit"
        prop.normalize = 1
        
        prop.algorithm()
        
        prop.PsOnly()
        prop.algorithmOnlyOutcome()
        
    # Uses the algorithm on the reflectance vs absorption coefficient from the
    # data set to get a path length distribution
    if sys.argv[1] == "dataset":
        
        prop.retrieveData()
        
        # Setting the right functions to be used
        prop.formula = "dataset"
        
        prop.algorithm()
        
        prop.algorithmOutcome()
        
    # Uses the algorithm on a function of reflectance vs absorption coefficient
    # to get a path length distribution
    if sys.argv[1] == "reflectance":
        
        # Setting the right functions to be used
        prop.formula = "reflectance"
        prop.FtFormula = "reflectanceFt"
        
        prop.algorithm()
        
        prop.PsOnly()
        prop.numVsAn()
        
    # Uses the algorithm on a function of reflectance vs absorption coefficient
    # to get a path length distributionbut, but Ps is a discrete set of points, 
    # and exact values are determined by interpolating
    if sys.argv[1] == "reflectanceNum":
        
        # Setting the right functions to be used
        prop.formula = "reflectance"
        prop.FtFormula = "reflectanceFt"
        
        prop.createData()
        
        # Changing the used function to interpolation
        prop.formula = "dataset"
        prop.s = []
        prop.Ps = []
        
        prop.algorithm()
        
        prop.PsCompare()
        prop.numVsAn()
        
    # Normalization constants are found for a set of radial distances, to 
    # determine what the right constant is and starting at what distance this
    # constant becomes valid
    if sys.argv[1] == "normalize":
        
        # Setting the right functions to be used
        normalizelist = []
        prop.normalize = 1.
        
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
            
    # Creates lists of reflectance and absorption coefficient for a certain
    # radial distance, does this with data from the data set and then saves
    # these list in an excel file
    if sys.argv[1] == "saveForFit":
        
        fs.fitSave(prop)
    
if __name__ == "__main__":
    main()