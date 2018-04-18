"""
9 April 2018 by Nathalie van Sterkenburg
Simulation of photons in tissue. Third step, boundaries are added. Based on 
algorithm chapter 5 of Optical-Thermal Response of Laser-Irradiated Tissue.
Incomplete
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import math
import numpy as np

mislukt, slecht = 0, 0

mu_a, mu_s, g, n, BINS = 1., 100., 0.9, 1.4, 100

z1, z2, n1, n2 = 0., 0.01, 1., 1.

rmax, zmax, D = 0.12, 0.08, 0.05

mu_t, TRESHOLD, CHANCE = mu_a + mu_s, 10. ** -4, 0.1

dr, dz, N = rmax / BINS, zmax / BINS, 100000

def main():

    # setting up the beam    
    A = np.zeros([BINS, BINS])
    R = [0 for i in range(BINS)]
    T = [0 for i in range(BINS)]
    
    counter = 0
    
    photon_list = []
    
    for i in range(1000):
        
        photon_list.append(Photon())
        
        counter += 1
        
    # running the beam
    while counter < N:
        
        for photon in photon_list:
                
            s = - math.log(random.random())/mu_t
                
            photon.change_position(s, R, T)
            bins(photon, A)
            direction(photon)
        
            if photon.weight < TRESHOLD:
                
                if random.random() <= CHANCE:
                    
                    photon.weight = photon.weight / CHANCE
                    
                else:
                    
                    photon = Photon()
                    
                    counter += 1
    
    print mislukt
    print slecht
    output(A, R, T)
    
    
    
class Photon:
    
    def __init__(self):
        
        self.x = 0.
        self.y = 0.
        self.z = 0.
        
        self.ux = 0.
        self.uy = 0.
        self.uz = 1.
        
        self.weight = 1.
    
    def change_position(self, s, R, T):
        
        self.x += s * self.ux
        self.y += s * self.uy
        self.z += s * self.uz
        
        if self.z < 0 and self.uz < 0:
            reflect(self, s, R, 0)
        
        if self.z > D and self.uz > 0:
            reflect(self, s, T, D)
        
        
def reflect(photon, s, V, d):
    
    photon.x -= s * photon.ux
    photon.y -= s * photon.uy
    photon.z -= s * photon.uz
    
    photon.z
    
    s1 = abs((photon.z - d) / photon.uz)
    
    photon.x += s1 * photon.ux
    photon.y += s1 * photon.uy
    photon.z += d
    
    photon.uz = photon.uz * -1    
    
    cost = photon.uz
    
    if cost == 1:
        cost = 0.999999
    if cost == -1:
        cost = -0.999999
    
    sint = (1 - cost ** 2) ** 0.5
    sinf = math.sin( math.asin(sint) * (n/n1))
    cosf = (1 - sint **2) ** 0.5
    
    
    Vi = (((sint * cosf - cost * sinf) ** 2) / 2) * (((cost * cosf + sint * sinf) 
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
    
    V[ir] += (1 - Vi) * photon.weight
    photon.weight = Vi * photon.weight
    
    photon.uz = - photon.uz
    
    photon.x += (s - s1) * photon.ux
    photon.y += (s - s1) * photon.uy
    photon.z += (s - s1) * photon.uz
    
    if photon.z < 0 and photon.uz < 0:
        mislukt += 1
    
    if photon.z > d and photon.uz > 0:
        slecht -= 1
        
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
    
def output(A, R, T):
    
    """
    for ir in range(BINS):
        
        V = 2 * math.pi * (ir - 0.5) * dr ** 2 * dz
        
        for iz in range(BINS):
            
            A[ir, iz] = A[ir, iz] / (V * N * mu_a)
    """
    
    ir_list = [i for i in np.arange(dr, rmax - dr, dr)]
    iz_list = [i for i in np.arange(dz, zmax - dz - 0.5 * dz, dz)]
    
    B = np.zeros([BINS - 2, BINS - 2])
    
    counter = 0
    nogeencounter = 0
    
    for ir in range(BINS - 2):
        
        nogeencounter += 1
        
        for iz in range(BINS - 2):
            
            j = ir + 1
            k = iz + 1
            
            B[ir, iz] = A[j, k]
            counter += 1
            
    S = []
    
    for ir in range(BINS - 2):
        
        S.append(R[ir + 1])
        
    U = []
    
    for ir in range(BINS - 2):
        
        U.append(T[ir + 1])
        
    
    ir_matrix, iz_matrix = np.meshgrid(ir_list, iz_list)
    
    plt.figure()
    plt.plot(ir_list, S, 'g-')
    plt.plot(ir_list, U, 'b-')
    plt.show()
    
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    surf = ax.plot_surface(ir_matrix, iz_matrix, B, cmap=plt.cm.coolwarm, linewidth=0, antialiased=False)
    ax.set_xlabel("r (cm)")
    ax.set_ylabel("z (cm)")
    ax.set_zlabel("A")
    fig.colorbar(surf, shrink=0.5, aspect=5, label = "Value of A")
    plt.show()
    
    
if __name__ == "__main__":
    main()