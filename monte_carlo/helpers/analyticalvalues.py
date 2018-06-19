# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 15:11:23 2018

@author: navansterkenburg
"""

class analyticalValues:
    
    def __init__(self, r, mua):
    
        #self.mus = 10.
        self.g = 0.8
        #self.muc = (1 - self.g) * self.mus
        self.muc = 10.
        self.mus = self.muc / (1 - self.g)
            
        # The refractive indices.
        self.nin = 1.
        self.nuit = 1.
        self.n = self.nin / self.nuit
        
        # All parameters used in calculation
        self.ueff = (3 * mua * (mua + self.muc)) ** 0.5
        self.rid = -1.44 * self.n ** -2 + 0.71 * self.n ** -1 + 0.67 + 0.0636 * self.n
        
        self.k = (1 + self.rid) / (1 - self.rid)
        self.D = (3 * (self.muc)) ** -1
            
        self.z0 = (self.muc) ** -1
        self.zb = 2 * self.k * self.D
        
        self.rho1 = (self.z0 ** 2 + r ** 2) ** 0.5
            
        self.rho2 = ((self.z0 + 2*self.zb) ** 2 + r**2) ** 0.5