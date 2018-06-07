# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 14:32:51 2018

@author: Gebruiker
"""

import sys
import helpers.simulations as sim

def main():
    """ Performs desired algorithm for desired number of houses, handles output
    and saves best outcome.

    """

    if sys.argv[1] == "Rvsr":
        
        sim.Rvsr()

    elif sys.argv[1] == "RvsMua":
        
        sim.RvsMua()
    
    elif sys.argv[1] == "savePhotons":
        
        sim.savePhotons()
        
    elif sys.argv[1] == "RvsrThree":
        
        sim.RvsrThree()

if __name__ == "__main__":
    main()