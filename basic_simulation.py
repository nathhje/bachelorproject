"""
5 April 2018 by Nathalie van Sterkenburg
Simulation of photons in tissue. First step, little more than a random walk.
"""

import matplotlib.pyplot as plt
import random
import math

def main(mu_a, mu_s):
    
    photon_list = []
    
    plt.figure()
    
    for i in range(60):
        
        start_x = 0
        start_y = 10
        
        photon_list.append(Photon(start_x, start_y))
        
    for i in range(100):
        
        for photon in photon_list:
            
            if not photon.absorbed:
                
                photon.change_position(photon.position_x + math.cos(photon.direction), photon.position_y + math.sin(photon.direction))
        
                chance = random.random()
        
                if chance < mu_a or photon.position_x < 0:
                    
                    photon.absorbed_photon()
            
                elif chance < mu_a + mu_s:
            
                    angle = random.random() * math.pi * 2
            
                    photon.change_direction(angle)
                    
        for photon in photon_list:
            plt.plot(photon.list_x, photon.list_y, "r-")
            plt.plot(photon.position_x, photon.position_y, "bo")
            
        plt.draw()
        plt.pause(0.001)
        plt.clf()
        
    for photon in photon_list:
        #plt.plot(photon.list_x, photon.list_y, "r-")
        plt.plot(photon.position_x, photon.position_y, "bo")
        
    plt.show()
    
    
class Photon:
    
    def __init__(self, start_x, start_y):
        
        self.position_x = start_x
        self.position_y = start_y
        self.list_x = [start_x]
        self.list_y = [start_y]
        self.direction = 0
        self.absorbed = False
    
    def change_position(self, new_x, new_y):
        
        self.position_x = new_x
        self.position_y = new_y
        self.list_x.append(new_x)
        self.list_y.append(new_y)
    
    def change_direction(self, angle):
        self.direction = angle
        
    def absorbed_photon(self):
        self.absorbed = True
    
if __name__ == "__main__":
    main(0.02, 0.1)