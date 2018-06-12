# -*- coding: utf-8 -*-
"""
Created on Thu May 17 11:10:54 2018

Filters only the reflected photons, not the absorped.
"""

import csv


for mua in [0.0, 0.1, 0.2, 0.3]:
    row_count = 0
    reflectedPhotons = []
    with open("photonsformua" + str(mua) + ".csv", 'r') as csvfile:
        
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        
        counter = 0
        row_count = sum(1 for row in reader)
        
    with open("photonsformua" + str(mua) + ".csv", 'r') as csvfile:
        
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    
        for row in reader:
            
            reflectedPhotons.append(row)
            
            counter += 1
            
            # Results are written away to avoid memory error
            if counter % 10000 == 0:
                
                with open("photonsmua" + str(mua) + ".csv", 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        
                    for arow in reflectedPhotons:
                        writer.writerow(arow)
                        
                reflectedPhotons = []
            
            if counter == int(row_count / 2.):
                break
            
    # Final rows are saved
    with open("photonsmua" + str(mua) + ".csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        
        for row in reflectedPhotons:
            
            writer.writerow(row)
        