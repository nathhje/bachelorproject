import numpy as np

class Properties:
    
    def __init__(self):
        
        self.reflects = []
        self.pathlengths = []
        self.totalR = 0
        
        self.mu_a = 1.
        self.mu_s = 100.
        self.mu_t = self.mu_a + self.mu_s
        self.g = 0.9
        self.n = 1.4
        
        self.z1 = 0.
        self.z2 = 0.01
        self.n1 = 1.4
        self.n2 = 1.4
        
        self.rmax = 0.15
        self.zmax = 0.08
        
        self.BINS = 200
        self.TRESHOLD = 10. ** -4
        self.CHANCE = 0.1
        
        self.dr = self.rmax / self.BINS
        self.dz = self.zmax / self.BINS
        
        self.N = 1000
        self.Nt = 1000
        
        self.A = np.zeros([self.BINS, self.BINS])
        self.R = [0 for i in range(self.BINS)]
        
        self.counter = 0
        self.photon_list = []