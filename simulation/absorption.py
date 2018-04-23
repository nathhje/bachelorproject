import math
import random

def bins(photon, prop):
    """ Altering weight and putting absorbed weight in bin. """
    
    r = (photon.x**2 + photon.y**2) ** 0.5
    ir = round(r/prop.dr)
    iz = round(abs(photon.z)/prop.dz)
    
    ir, iz = int(ir), int(iz)
    
    if ir >= prop.BINS:
        ir = prop.BINS - 1
        
    if iz >= prop.BINS:
        iz = prop.BINS - 1
    
    prop.A[ir][iz] += photon.weight * prop.mu_a / prop.mu_t
    photon.weight = photon.weight * prop.mu_s / prop.mu_t
    
def direction(photon, prop):
    """ Establishing new direction. """
    
    costh = (1 + prop.g**2 - ((1 - prop.g**2) / 
            (1 - prop.g + 2 * prop.g * random.random())) ** 2) / 2 * prop.g
    sinth  = (1 - costh ** 2) ** 0.5
    temp = (1 - photon.uz ** 2) ** 0.5
    phi = 2 * math.pi * random.random()
    cosph = math.cos(phi)
    sinph = math.sin(phi)
    
    if photon.ux == 0 or photon.uy == 0:
        uxx = sinth * cosph
        uyy = sinth * sinph
    
        if photon.uz >= 0:
            uzz = costh
        
        else:
            uzz = - costh
        
    else:
        uxx = sinth * ( photon.ux * photon.uz * cosph - photon.uy * sinph) / temp * photon.ux * costh
        uyy = sinth * ( photon.uy * photon.uz * cosph - photon.ux * sinph) / temp * photon.uy * costh
        uzz = -sinth * cosph * temp * photon.uz * costh
    
    photon.ux = uxx
    photon.uy = uyy
    photon.uz = uzz