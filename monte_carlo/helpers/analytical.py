"""
16 April 2018 by Nathalie van Sterkenburg.
Analytical solution for radial reflection from photons in tissue. Based on
Welch and Van Gemert and the article by Farrell and Patterson.
"""

import math
import matplotlib.pyplot as plt
import numpy as np

def main(mua):
    """ Generates analytical solution. """

    props = Properties(mua)
    
    # Finding R for each r.
    for r in np.arange(0, 1., 0.002):
        
        props.rlist.append(r)
        
        rho1 = (props.z0 ** 2 + r ** 2) ** 0.5
        
        rho2 = ((props.z0 + 2*props.zb) ** 2 + r**2) ** 0.5
        
        # The formula for the analytical solution is calculated.
        R = (props.z0 * (props.ueff + rho1 ** -1) * math.exp( -props.ueff * rho1) 
            / (rho1 ** 2) + (props.z0 + 2 * props.zb) * (props.ueff + rho2 ** -1) 
            * math.exp( -props.ueff * rho2) / (rho2 ** 2)) / 4 / math.pi
            
        props.Rlist.append(R)
        
    # The result is plotted.
    plt.figure()
    plt.plot(props.rlist, props.Rlist)
    plt.title("Analytical")
    plt.xlabel("r(cm)?")
    plt.ylabel("R(photons/cm)?")
    plt.yscale("log")
    plt.axis([0, 0.35, 10**-2, 10**2])
    plt.show()
    
    return props
    
class Properties:
    """ Contains all variables. """
    
    def __init__(self, mua):
        
        # The tissue properties.
        self.mua = mua
        #self.mus = 10.
        self.g = 0.8
        #self.muc = (1 - self.g) * self.mus
        self.muc = 10.
        self.mus = self.muc / (1 - self.g)
        
        # The refractive indices.
        self.nin = 1.
        self.nuit = 1.
        self.n = self.nin / self.nuit
        
        # The changing variables.
        self.rlist = []
        self.Rlist = []
    
        # All parameters used in calculation
        self.ueff = (3 * mua * (mua + self.muc)) ** 0.5
        self.rid = -1.44 * self.n ** -2 + 0.71 * self.n ** -1 + 0.67 + 0.0636 * self.n
        
        self.k = (1 + self.rid) / (1 - self.rid)
        self.D = (3 * (self.mua + self.muc)) ** -1
        
        self.z0 = (self.mua + self.muc) ** -1
        self.zb = 2 * self.k * self.D
        
    
if __name__ == "__main__":
    mua = 1.
    main(mua)