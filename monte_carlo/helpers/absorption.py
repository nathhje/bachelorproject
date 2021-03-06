"""
Contains two funcitons that deal with the absorption of photons that propagate
through tissue. Each photon has a weight that is partly absorped, the rest of
the photon will continue to propagate in a new direction.
"""

import math
import random

def bins(photon, prop):
    """ Alters photon weight and puts absorbed weight in bin. 
    
    photon: the instance of the absorbed photon.
    prop: contains all constants, methods of saving and outputs.
    """
    
    # Puts absorbed weight in a bin if Rvsr is run
    if prop.name == "Rvsr":
        prop.RvsrBins(photon)
        
    # Adjusts the weight of the photon
    photon.weight = photon.weight * prop.mu_s / prop.mu_t
    
def direction(photon, prop):
    """ Establishes new direction for a photon.
     
    photon: the instance of the absorbed photon.
    prop: contains all constants, methods of saving and outputs.
    """
    
    # All necessary goniometric expressions are calculated
    costh = (1 + prop.g**2 - ((1 - prop.g**2) / 
            (1 - prop.g + 2 * prop.g * random.random())) ** 2) / (2 * prop.g)
    sinth  = (1 - costh ** 2) ** 0.5
    temp = (1 - photon.uz ** 2) ** 0.5
    phi = 2 * math.pi * random.random()
    cosph = math.cos(phi)
    sinph = math.sin(phi)
    
    # Updates photon direction the very first time, when it only moves in the 
    # z-direction
    if 1. - abs(photon.uz) < 10**-12:
        uxx = sinth * cosph
        uyy = sinth * sinph
    
        if photon.uz >= 0:
            uzz = costh
        
        else:
            uzz = - costh
        
        # For proper normalization
        total = uxx ** 2 + uyy ** 2 + uzz ** 2
        
        uxx = uxx / total
        uyy = uyy / total
        uzz = uzz / total
            
        
    # Calculates the new photon direction
    else:
        uxx = sinth * ( photon.ux * photon.uz * cosph - photon.uy * sinph) / temp + photon.ux * costh
        uyy = sinth * ( photon.uy * photon.uz * cosph + photon.ux * sinph) / temp + photon.uy * costh
        uzz = -sinth * cosph * temp + photon.uz * costh
        
        # For proper normalization
        total = uxx ** 2 + uyy ** 2 + uzz ** 2
        
        uxx = uxx / total
        uyy = uyy / total
        uzz = uzz / total
        
    # Updates the photon direction.
    photon.ux = uxx
    photon.uy = uyy
    photon.uz = uzz