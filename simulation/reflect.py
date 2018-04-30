"""
12 April 2018 by Nathalie van Sterkenburg.
Contains a function that reflects a photon when it crosses the boundary. Part
of the weight is let through and saved as radial reflectance, the rest is send 
back into the tissue to continue propagating.
"""

import math

def reflect(photon, s, prop):
    """ 
    Reflects a photon against the boundary. s is length of the previous step the
    photon has taken.
    """
    
    # The number of times the photon is reflected increases.
    photon.nrreflect += 1
    
    # The photon has already taken a step to cross the boundary, so it now has
    # to take the same step back.
    photon.x -= s * photon.ux
    photon.y -= s * photon.uy
    photon.z -= s * photon.uz
    
    # Another stepsize is calculated that will put the photon on the boundary.
    s1 = abs(photon.z / photon.uz)
    
    # The photon takes this step.
    photon.x += s1 * photon.ux
    photon.y += s1 * photon.uy
    photon.z = 0
    
    # The velocity in the z-direction is reversed so the photon goes back.
    photon.uz = -1 * photon.uz
    
    # The goniometric parameters are calculated that are used for determining 
    # the part of the photon weight that will be reflected.
    cost = photon.uz
    sint = (1 - photon.uz ** 2) ** 0.5
    sinf = math.sin( math.asin(sint) * (prop.n/prop.n1))
    cosf = (1 - sint **2) ** 0.5
    
    # The fraction of the photon weight that continues propagating is determined.
    Ri = (((sint * cosf - cost * sinf) ** 2) / 2) * (((cost * cosf + sint * sinf) 
            ** 2 + (cost * cosf - sint * sinf) ** 2) / ((sint * cosf + cost * sinf) 
            ** 2 * (cost * cosf + sint * sinf) ** 2))
    
    # The index of the bin that should save the photon weight is determined.
    r = (photon.x ** 2 + photon.y ** 2) ** 0.5
    ir = int(round(r / prop.dr))
    
    # Makes certain the bin index isn't out of range.
    if ir >= prop.BINS:
        ir = prop.BINS - 1
        
    # Puts the right weight in the right bin, increases the total lost weight and
    # updates the photon weight.
    prop.R[ir] += (1 - Ri) * photon.weight
    prop.totalR += (1 - Ri) * photon.weight
    photon.weight = Ri * photon.weight
    
    # Adds the photon's pathlength to the list for the pathlength distribution
    prop.pathlengths.append(photon.path)
    
    # The second part of the initial step is taken.
    photon.x += (s - s1) * photon.ux
    photon.y += (s - s1) * photon.uy
    photon.z += (s - s1) * photon.uz