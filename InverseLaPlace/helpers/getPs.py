# -*- coding: utf-8 -*-
"""
Contains functions that return a value for P(s), either by using an exact 
formula or interpolating in a discrete set of points. Used to perform an 
inverse Laplace transform on the formula or discrete set of points.

Every function has the same input:
s: the x-value for which a y value has to found.
prop: a class with a all constants, lists, functions that perform the
algorithm and functions that provide output.
"""

import math
import helpers.analyticalvalues as av
import random

def exponential(s, prop):
    """ The Laplace transform of an exponential function. """
    
    P = 1 / (s+1)
    
    prop.s.append(s)
    prop.Ps.append(P)
    
    return P

def exponentialSys(s, prop):
    """ The Laplace transfrom of an exponential function, but with a systematic
    deviation.
    """
    
    # original value
    P = 1 / (s+1)
    
    # with a deviation
    Pd = P * 1.1
    
    prop.s.append(s)
    prop.moreref.append(P)
    prop.Ps.append(Pd)
    
    return Pd

def exponentialRand(s, prop):
    """ The Laplace transfrom of an exponential function, but with a random
    deviation.
    """
    
    # original value
    P = 1 / (s+1)
    
    # with a deviation
    Pd = P * (random.random()* 21./110. + 10./11.)
    
    prop.s.append(s)
    prop.moreref.append(P)
    prop.Ps.append(Pd)
    
    return Pd

def cosine(s, prop):
    """ The Laplace transform of a goniometric function. """
    
    P = s / (s ** 2 + 1)
    
    prop.s.append(s)
    prop.Ps.append(P)
    
    return P

def fit(s, prop):
    """ A fit made to the reflectance vs absorption coefficient from the data
    set.
    """
    
    P = 0.019892974 * math.e ** (-0.651220312*s)
    
    prop.s.append(s)
    prop.Ps.append(P)
    
    return P

def reflectance(s, prop):
    """ A function of reflectance as a function of absorption coefficient. """
    
    values = av.analyticalValues(prop.r, s)
    
    P =(values.z0 * (values.ueff + values.rho1 ** -1) * math.exp( -values.ueff * values.rho1) 
            / (values.rho1 ** 2) + (values.z0 + 2 * values.zb) * (values.ueff + values.rho2 ** -1) 
            * math.exp( -values.ueff * values.rho2) / (values.rho2 ** 2)) / 4 / math.pi
    
    prop.s.append(s)
    prop.Ps.append(P)
    
    return P

def dataset(s, prop):
    """ Determines the right value of P(s) from a discrete set of points. """
    
    # index will be a float in between two real indices
    index = s / prop.deltamua
    
    # These indices are determined
    indexLow = int(index)
    indexHigh = int(index) + 1
    
    # It is checked if these indices are within the range of mualist
    # If not, the two closest points are extrapolated
    if indexLow < 0:
        indexLow = 0
        indexHigh = 1
        
    if indexHigh >= len(prop.mualist):
        indexLow = len(prop.mualist) - 2
        indexHigh = len(prop.mualist) - 1
    
    # The slope between the two closest data points
    a = (prop.reflections[indexHigh] - prop.reflections[indexLow]) / 0.2
    
    # The value of P(s)
    P = prop.reflections[indexLow] + a * (s - indexLow * prop.deltamua)
    
    # If the data points are derived from the Laplace transform of the
    # exponential function or the reflectance vs absorption coefficient,
    # the exact value is also saved to show how close the two outcomes are
    if prop.FtFormula == "exponentialFt":
        prop.moreref.append(1 / (s+1))
        
    if prop.FtFormula == "reflectanceFt":
        prop.moreref.append(getReflectance(s,prop))
        
    prop.s.append(s)
    prop.Ps.append(P)

    return P

def getReflectance(s, prop):
    """ A function of reflectance as a function of absorption coefficient, 
    but without saving the values to a list. 
    """
    
    values = av.analyticalValues(prop.r, s)
    
    P =(values.z0 * (values.ueff + values.rho1 ** -1) * math.exp( -values.ueff * values.rho1) 
            / (values.rho1 ** 2) + (values.z0 + 2 * values.zb) * (values.ueff + values.rho2 ** -1) 
            * math.exp( -values.ueff * values.rho2) / (values.rho2 ** 2)) / 4 / math.pi
    
    return P