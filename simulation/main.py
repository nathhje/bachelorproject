from properties import Properties
from photon import Photon
from output import output
import absorption
import random
import math

def main():

    prop = Properties()
    
    for i in range(10000):
        
        prop.photon_list.append(Photon())
        
    # running the beam
    while prop.counter < prop.N:
        
        for index, photon in enumerate(prop.photon_list):
                
            s = - math.log(random.random())/prop.mu_t
                
            photon.change_position(s, prop)
            absorption.bins(photon, prop)
            absorption.direction(photon, prop)
        
            if photon.weight < prop.TRESHOLD:
                
                if random.random() <= prop.CHANCE:
                    
                    photon.weight = photon.weight / prop.CHANCE
                    
                else:
                    
                    prop.reflects.append(photon.nrreflect)
                    
                    prop.pathlengths.append(photon.path)
                    prop.photon_list[index] = Photon()
                    
                    prop.counter += 1
    
    output(prop)
    
if __name__ == "__main__":
    main()