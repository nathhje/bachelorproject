# -*- coding: utf-8 -*-
"""
Created on Tue May 29 10:36:21 2018

@author: Gebruiker
"""

import csv
import numpy as np
import matplotlib.pyplot as plt

def retrieveData(r, delta):
    
    mualist = [round(i, 1) for i in np.arange(0.1, 5., 0.2)]
        
    reflections = []
    
    for mua in mualist:
        print("another one")
        
        counter = 0
        
        reflection = 0
        
        with open("photonsmua" + str(mua) + ".csv", "r") as csvfile:
            
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            
            for row in reader:
                """
                counter += 1
                
                if counter > 100000:
                    break
                """
                if r - delta < float(row[1]) <= r + delta:
                    
                    reflection += float(row[2])
        
        reflections.append(reflection)
        
    plt.figure()
    plt.plot(mualist, reflections)
    #plt.plot(mualist, reflections, 'bo')
    plt.show()
    return mualist, reflections