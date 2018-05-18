# -*- coding: utf-8 -*-
"""
Created on Thu May 17 11:10:54 2018

Filters only the reflected photons, not the absorped.
"""

import csv

reflectedPhotons = []

with open("actualphotonsformua0.1.csv", 'r') as csvfile:
    
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    
    counter = 0
    
    for row in reader:
        
        # Checks if row is reflected or absorbed
        if row[0] == 'r':
            
            reflectedPhotons.append(row)
        counter += 1
        
        # Results are written away to avoid memory error
        if counter % 10000 == 0:
            
            with open("photonsformua0.1.csv", 'a', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='"')
    
                for row in reflectedPhotons:
        
                    writer.writerow(row)
                    
            reflectedPhotons = []
            
# Final rows are saved
with open("photonsformua0.1.csv", 'a', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"')
    
    for row in reflectedPhotons:
        
        writer.writerow(row)
        