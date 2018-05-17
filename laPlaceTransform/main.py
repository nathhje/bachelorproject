# -*- coding: utf-8 -*-
"""
Created on Thu May 17 13:42:00 2018

@author: Gebruiker
"""

import csv
import matplotlib.pyplot as plt

def main(r):
    
    theweights = []
    pathlengths = []
    
    with open("reflectedPhotons.csv", 'r') as csvfile:
    
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        
        for row in reader:
            
            theweights.append(row[2])
            pathlengths.append(row[3])
            
    plt.figure()
    plt.hist(pathlengths, bins=100, weights=theweights)
    plt.show()
    
if __name__ == "__main__":
    main(0)