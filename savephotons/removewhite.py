# -*- coding: utf-8 -*-
"""
Created on Thu May 17 11:10:54 2018

Removes the white lines from a file.
"""

import csv

actualPhotons = []

with open("photonsformua4.7.csv", 'r') as csvfile:
    
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    
    counter = 0
    
    for row in reader:
        
        # Every other line is white space and should not be included
        if counter % 2 == 0:
            
            actualPhotons.append(row)
        counter += 1
        
        # Results are written away to avoid memory error
        if counter % 10000 == 0:
            
            with open("actualphotonsformua4.7.csv", 'a', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='"')
    
                for row in actualPhotons:
        
                    writer.writerow(row)
                    
            actualPhotons = []
            
# Final rows are saved
with open("actualphotonsformua4.7.csv", 'a', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"')
    
    for row in actualPhotons:
        
        writer.writerow(row)
        