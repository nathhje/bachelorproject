"""
16 April 2018 by Nathalie van Sterkenburg
Analytical solution for radial reflection from photons in tissue. Based on
Welch and Van Gemert and the article by Farrell and Patterson.
"""

import math
import matplotlib.pyplot as plt
import numpy as np

mua, mus, g, nin = 1., 100., 0.9, 1.4

muc, nuit = (1 - g) * mus, 1.4

n = nin / nuit

def main():

    rlist = []
    Rlist = []
    
    a = muc / (mua + muc)
    
    ueff = mua * (3 / (1 - a)) ** 0.5
    
    rid = -1.44 * n ** -2 + 0.71 * n ** -1 + 0.67 + 0.0636 * n
    
    k = (1 + rid) / (1 - rid)
    
    D = (3 * (mua + muc)) ** -1
    
    z0 = (mua + muc) ** -1
    
    zb = 2 * k * D
    
    for r in np.arange(0, 1., 0.002):
        
        rlist.append(r)
        
        rho1 = (z0 ** 2 + r ** 2) ** 0.5
        
        rho2 = ((z0 + 2*zb) ** 2 + r**2)
        
        R = (z0 * (ueff + rho1 ** -1) * math.exp( -ueff * rho1) / (rho1 ** 2)
            + (z0 + 2 * zb) * (ueff + rho2 ** -1) * math.exp( -ueff * rho2)
            / (rho2 ** 2)) / 4 / math.pi
            
        Rlist.append(R)
        
    plt.figure()
    plt.plot(rlist, Rlist)
    plt.title("Analytical")
    plt.xlabel("r(cm)?")
    plt.ylabel("R(photons/cm)?")
    plt.show()
    
    
if __name__ == "__main__":
    main()