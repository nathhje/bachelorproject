"""
12 April 2018 by Nathalie van Sterkenburg.
Simulation of photons in tissue. There's a front boundary and the pathlength of
each photon is measured. Based on algorithm chapter 5 of Optical-Thermal 
Response of Laser-Irradiated Tissue.
"""

from properties import Properties
from photon import Photon
import absorption
import random
import math

def runSimulation(mua):
    """ Runs the simulation. """

    prop = Properties(mua)
    
    # The list of photons is generated.
    for i in range(prop.Nt):
        
        prop.photon_list.append(Photon())
        
        prop.madecounter += 1
        
    # The beam is simulated and the outcome saved.
    while prop.abcounter < prop.N:
        
        # Each photon takes a step.
        for index, photon in enumerate(prop.photon_list):
                
            # The length of the step.
            s = - math.log(random.random())/prop.mu_t
                
            # The photon is updated.
            photon.change_position(s, prop)
            absorption.bins(photon, prop)
            absorption.direction(photon, prop)
        
            # It is decided if the photon is terminated.
            if photon.weight < prop.TRESHOLD:
                
                # The photons weight is increased and it continues propagating.
                if random.random() <= prop.CHANCE:
                    
                    photon.weight = photon.weight / prop.CHANCE
                    
                # The photon is terminated.
                else:
                    
                    # The photons data are saved.
                    prop.reflects.append(photon.nrreflect)
                    
                    # If new photons are still needed, a new one is created.
                    if prop.madecounter < prop.N:
                        prop.photon_list[index] = Photon()
                        prop.madecounter += 1 
                        
                    # If not, the list entry is removed.
                    else:
                        prop.photon_list.remove(photon)
                                       
                    prop.abcounter += 1
                    
    return prop
    
    
if __name__ == "__main__":
    
    mua = 1.
    
    prop = runSimulation(mua)
    
    prop.oneOutput()