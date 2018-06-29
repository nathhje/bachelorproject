# -*- coding: utf-8 -*-
"""
Contains functions that return the analytical solution to an inverse Laplace
transform, F(t).

Every function has the same input:
T: the x-value for which a y value has to found.
prop: a class with a all constants, lists, functions that perform the
algorithm and functions that provide output.
"""

import math
import helpers.analyticalvalues as av

def exponential(T, prop):
    """ Returns a point on an exponential function. """
    
    return math.exp(-T)

def cosine(T, prop):
    """ Returns a point on a goniometric function. """
    
    return math.cos(T)

def reflectance(T, prop):
    """ Returns a point on the function for reflectance as a function of 
    absorption coefficient.
    """
    
    values = av.analyticalValues(prop.r, 0.0)
    
    return 1 * T ** (-2.5) * (values.z0 * math.exp(- values.rho1**2 / (4 * values.D * T)) + (values.z0 + 2 * values.zb) * math.exp(- values.rho2**2 / (4 * values.D * T)))