"""
Simulation of photons moving through tissue. There's only a front boundary and 
the pathlength, weight and radial distance of each photon is measured. Based on 
algorithm chapter 5 of Optical-Thermal Response of Laser-Irradiated Tissue.
"""

from classessimulation.properties import Properties
from classessimulation.photon import Photon
import helpers.absorption as absorption
import random
import math

def runSimulation(mua, r, name):
    """ Runs the simulation. 
    
    mua: the absorption coefficient for this run.
    r: reflections with this radial distance are saved and used for output.
    name: name determines in what way the reflections and absorptions are 
    stored.
    """

    prop = Properties(mua, r, name)
    
    # The list of photons is generated
    for i in range(prop.Nt):
        
        prop.photon_list.append(Photon())
        
        prop.madecounter += 1
        
    # The beam is simulated and the outcome saved
    while prop.abcounter < prop.N:
        
        # Each photon takes a step
        for index, photon in enumerate(prop.photon_list):
                
            # The length of the step
            s = - math.log(random.random())/prop.mu_t
                
            # The photon is updated
            photon.change_position(s, prop)
            absorption.bins(photon, prop)
            absorption.direction(photon, prop)
            
            # It is decided if the photon is terminated.
            if photon.weight.real < prop.TRESHOLD:
                
                # The photons weight is increased and it continues propagating
                if random.random() <= prop.CHANCE:
                    
                    photon.weight = photon.weight / prop.CHANCE
                    
                # The photon is terminated
                else:
                    
                    # If new photons are still needed, a new one is created
                    if prop.madecounter < prop.N:
                        prop.photon_list[index] = Photon()
                        prop.madecounter += 1 
                        
                    # If not, the list entry is removed
                    else:
                        prop.photon_list.remove(photon)
                                       
                    # Number of terminated photons
                    prop.abcounter += 1
                    
                    # If photons have to be saved, they are saved regularly
                    # to avoid memory overload.
                    if prop.abcounter % 10000 == 0:
                        
                        if prop.name == "savePhotons":
                            prop.savePhotons()
    
    # The last photons are saved if they have to be saved
    if prop.name == "savePhotons":
        prop.savePhotons()
                    
    return prop