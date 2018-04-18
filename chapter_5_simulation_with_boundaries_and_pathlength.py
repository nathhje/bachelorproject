"""
12 April 2018 by Nathalie van Sterkenburg
Simulation of photons in tissue. There's a front boundary and the pathlength of
each photon is measured. Based on algorithm chapter 5 of Optical-Thermal 
Response of Laser-Irradiated Tissue.
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import math
import numpy as np

mu_a, mu_s, g, n, BINS = 1., 100., 0.9, 1.4, 100

z1, z2, n1, n2 = 0., 0.01, 1., 1.

rmax, zmax = 1., 0.08

mu_t, TRESHOLD, CHANCE = mu_a + mu_s, 10. ** -4, 0.1

dr, dz, N = rmax / BINS, zmax / BINS, 1000000

pathlengths = []

def main():

    # setting up the beam    
    A = np.zeros([BINS, BINS])
    R = [0 for i in range(BINS)]
    
    counter = 0
    
    photon_list = []
    
    for i in range(100000):
        
        photon_list.append(Photon())
        
        counter += 1
        
    # running the beam
    while counter < N:
        
        for photon in photon_list:
                
            s = - math.log(random.random())/mu_t
                
            photon.change_position(s, R)
            bins(photon, A)
            direction(photon)
        
            if photon.weight < TRESHOLD:
                
                if random.random() <= CHANCE:
                    
                    photon.weight = photon.weight / CHANCE
                    
                else:
                    
                    photon = Photon()
                    
                    counter += 1
    
                                 
    output(A, R)
    
    
    
class Photon:
    
    def __init__(self):
        
        self.x = 0.
        self.y = 0.
        self.z = 0.
        
        self.ux = 0.
        self.uy = 0.
        self.uz = 1.
        
        self.weight = 1.
        self.path = 0.
    
    def change_position(self, s, R):
        
        self.x += s * self.ux
        self.y += s * self.uy
        self.z += s * self.uz
        self.path += s
        
        if self.z < 0 and self.uz < 0:
            reflect(self, s, R)
        
def reflect(photon, s, R):
    
    photon.x -= s * photon.ux
    photon.y -= s * photon.uy
    photon.z -= s * photon.uz
    
    s1 = abs(photon.z / photon.uz)
    
    photon.x += s1 * photon.ux
    photon.y += s1 * photon.uy
    photon.z = 0
    
    photon.uz = -1 * photon.uz
    
    cost = photon.uz
    sint = (1 - photon.uz ** 2) ** 0.5
    sinf = math.sin( math.asin(sint) * (n/n1))
    cosf = (1 - sint **2) ** 0.5
    
    Ri = (((sint * cosf - cost * sinf) ** 2) / 2) * (((cost * cosf + sint * sinf) 
            ** 2 + (cost * cosf - sint * sinf) ** 2) / ((sint * cosf + cost * sinf) 
            ** 2 * (cost * cosf + sint * sinf) ** 2))
            
    """
    print "uz"
    print photon.uz
    print "sint"
    print sint
    print "sinf"
    print sinf
    print "cosf"
    print cosf
    print "Ri"
    print Ri
    """
    r = (photon.x ** 2 + photon.y ** 2) ** 0.5
    
    ir = int(round(r / dr))
    
    if ir >= BINS:
        ir = BINS - 1
    
    R[ir] += (1 - Ri) * photon.weight
    photon.weight = Ri * photon.weight
    
    pathlengths.append(photon.path)
    
    photon.uz = - photon.uz
    
    photon.x += (s - s1) * photon.ux
    photon.y += (s - s1) * photon.uy
    photon.z += (s - s1) * photon.uz
        
def bins(photon, A):
    """ Altering weight and putting absorbed weight in bin. """
    
    r = (photon.x**2 + photon.y**2) ** 0.5
    ir = round(r/dr)
    iz = round(abs(photon.z)/dz)
    
    ir, iz = int(ir), int(iz)
    
    if ir >= BINS:
        ir = BINS - 1
        
    if iz >= BINS:
        iz = BINS - 1
    
    A[ir][iz] += photon.weight * mu_a / mu_t
    photon.weight = photon.weight * mu_s / mu_t
    
def direction(photon):
    """ Establishing new direction. """
    
    costh = (1 + g**2 - ((1 - g**2) / (1 - g + 2 * g * random.random())) ** 2) / 2 * g
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
    
def output(A, R):
    
    
    for ir in range(BINS):
        
        V = 2 * math.pi * (ir - 0.5) * dr ** 2 * dz
        
        AREA = 2 * math.pi * (ir - 0.5) * dr ** 2
        
        R[ir] = R[ir] / (AREA * N)
        
        for iz in range(BINS):
            
            A[ir, iz] = A[ir, iz] / (V * N)
    
    
    ir_list = [i for i in np.arange(dr, rmax - dr - 0.5 * dr, dr)]
    iz_list = [i for i in np.arange(dz, zmax - dz - 0.5 * dz, dz)]
    
    B = np.zeros([BINS - 2, BINS - 2])
    
    counter = 0
    anothercounter = 0
    
    for ir in range(BINS - 2):
        
        anothercounter += 1
    
        for iz in range(BINS - 2):
            
            j = ir + 1
            k = iz + 1
            
            B[ir, iz] = A[j, k]
            counter += 1
            
    T = []
    
    for ir in range(BINS - 2):
        
        T.append(R[ir + 1])
    
    ir_matrix, iz_matrix = np.meshgrid(ir_list, iz_list)
    
    print len(pathlengths)
    
    plt.figure()
    plt.hist(pathlengths)
    plt.show()
    
    plt.figure()
    plt.plot(ir_list, T)
    plt.show()
    
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    surf = ax.plot_surface(ir_matrix, iz_matrix, B, cmap=plt.cm.coolwarm, linewidth=0, antialiased=False)
    ax.set_xlabel("r (cm)")
    ax.set_ylabel("z (cm)")
    ax.set_zlabel("A")
    ax.set_ylim3d(0., zmax / 10)
    fig.colorbar(surf, shrink=0.5, aspect=5, label = "Value of A")
    plt.show()
    
    
if __name__ == "__main__":
    main()