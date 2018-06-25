# -*- coding: utf-8 -*-
"""
Created on Thu May 17 11:10:54 2018

Filters only the reflected photons, not the absorped.
"""

import csv
import numpy as np

reflectedPhotons = []

for mua in np.arange(0.0, 10.01, 0.05):
    
    mua = round(mua,2)
    
    with open("data\\photonsformua" + str(mua) + ".csv", "r") as csvfile:
        
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        
        counter = 0
        
        for row in reader:
            
            weight = row[1].replace("(","")
            weigh = weight.replace(")","")
            
            weig = complex(weigh)
            
            newrow = [float(row[0]), weig.real, float(row[2])]
                
            reflectedPhotons.append(newrow)
            counter += 1
            
            # Results are written away to avoid memory error
            if counter % 10000 == 0:
                
                with open("data\\photonsmua" + str(mua) + ".csv", 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        
                    for morerow in reflectedPhotons:
            
                        writer.writerow(morerow)
                        
                reflectedPhotons = []
                
    # Final rows are saved
    with open("data\\photonsmua" + str(mua) + ".csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        
        for row in reflectedPhotons:
            
            writer.writerow(row)
            