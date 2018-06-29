# -*- coding: utf-8 -*-
"""
Deterimines the reflectance based on r and mua.
"""

import math
import helpers.analyticalvalues as av

def reflectance(mua, r):
    """
    mua: the absorption coefficient used.
    r: the radial distance used.
    """
    
    values = av.analyticalValues(r, mua)
    
    # the value of the reflectance is determined
    return (values.z0 * (values.ueff + values.rho1 ** -1) * math.exp( -values.ueff * values.rho1) 
            / (values.rho1 ** 2) + (values.z0 + 2 * values.zb) * (values.ueff + values.rho2 ** -1) 
            * math.exp( -values.ueff * values.rho2) / (values.rho2 ** 2)) / 4 / math.pi
