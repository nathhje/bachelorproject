# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 10:29:46 2018

@author: Gebruiker
"""

import matplotlib.pyplot as plt
import helpers.getFt
from helpers.getPs import exponential
from helpers.getPs import dataset
from helpers.getPs import reflectance
import numpy as np
import csv

class Properties:
    
    def __init__(self):
        
        self.N = 22
        self.r = 1.
        self.delta = 0.0005
        self.mualist = []
        self.reflections = []
        self.formula = ""
        self.G = []
        self.H = []
        self.V = []
        self.T = []
        self.Fa = []
        
    def algorithm(self):
        
        self.createV()
        
        self.createF()
        
    def createV(self):
    
        Nh = int(self.N / 2)
        self.G.append(1)
        
        for i in range(1, self.N+1):
            self.G.append(self.G[i-1] * i)
        
        self.H = [1, 2 / self.G[Nh-1]]
    
        for i in range(2, Nh+1):
            self.H.append(i ** (Nh) * self.G[2*i] / (self.G[Nh-i] * self.G[i] * self.G[i-1]))
        
        sn = (-1) ** (self.N/2 + 1)
    
        self.V.append(0)
    
        for i in range(1, self.N+1):
            self.V.append(0)
            limit = Nh+1
        
            if i < Nh:
            
                limit = i+1
            
            for k in range(int((i+1) / 2), limit, 1):
            
                self.V[i] += self.H[k] / (self.G[i-k] * self.G[2 * k - i])
            
            self.V[i] *= sn
        
            sn = - sn
        
        print(self.G)
        print(self.H)
        print(self.V)
    
    def createF(self):
    
        function = globals()[self.formula]
    
        for i in np.arange(0.5, 20.0, 0.01):
            
            a = 0.69314 / i
            nextFa = 0
    
            for j in range(1, self.N+1):
        
                Ps = function(a * j, self)
                if Ps < 0:
                    Ps = 0
                    
                nextFa += self.V[j] * Ps
        
            nextFa *= a
    
            self.T.append(i)
            self.Fa.append(nextFa)
            
    def retrieveData(self):
    
        self.mualist = [round(i, 2) for i in np.arange(0.0, 10.005, 0.05)]
    
        for mua in self.mualist:
            print(mua)
        
            counter = 0
        
            reflection = 0
        
            with open("data\\photonsformua" + str(mua) + ".csv", "r") as csvfile:
            
                reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            
                for row in reader:
                    
                    counter += 1
                
                    if counter > 10000:
                        break
                    
                    if self.r - self.delta < float(row[1]) <= self.r + self.delta:
                    
                        reflection += float(row[2])
        
            self.reflections.append(reflection)
        
        plt.figure()
        plt.plot(self.mualist, self.reflections)
        #plt.plot(mualist, reflections, 'bo')
        plt.show()
        
    def algorithmOutcome(self):
        
        plt.figure()
        plt.plot(self.T, self.Fa)
        plt.plot(self.T, self.Fa, 'bo')
        plt.xlabel("t")
        plt.ylabel("F")
        plt.title("Harald Stefest's algorithm", y = 1.08)
        plt.show()
        
    def numVsAn(self):
        print(self.T)
        print(self.Fa)
        Ft = []
    
        for i in self.T:
        
            Ft.append(helpers.getFt.exponential(i))
        
        plt.figure()
        plt.plot(self.T, self.Fa)
        plt.plot(self.T, self.Fa, 'bo')
        plt.plot(self.T, Ft, 'g-')
        #plt.plot(self.T, Ft, 'go')
        plt.xlabel("t")
        plt.ylabel("F")
        plt.title("Analytical solution of a function vs Harald Stefest's algorithm", y = 1.08)
        plt.show()