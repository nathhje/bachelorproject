# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 10:29:46 2018

@author: Gebruiker
"""

import matplotlib.pyplot as plt
from helpers.getPs import exponential
from helpers.getPs import cosine
from helpers.getPs import dataset
from helpers.getPs import reflectance
from helpers.getFt import exponential as exponentialFt
from helpers.getFt import cosine as cosineFt
from helpers.getFt import reflectance as reflectanceFt
import numpy as np
import csv
import math

class Properties:
    
    def __init__(self):
        
        self.N = 22
        
        self.r = 0.5
        self.delta = 0.01
        
        self.step = 0.1
        self.algar = 0.
        self.anaar = 0.
        
        self.mualist = []
        self.reflections = []
        self.formula = ""
        self.FtFormula = ""
        self.G = []
        self.H = []
        self.V = []
        self.T = []
        self.Fa = []
        
        self.weights = []
        self.pathlengths = []
        
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
    
        for i in np.arange(0.1, 10., self.step):
            
            a = 0.69314 / i
            nextFa = 0
            
            for j in range(1, self.N+1):
                #print("new")
                Ps = function(a * j, self)
                if Ps < 0:
                    Ps = 0
                #print(Ps)
                #print(exponential(a*j, self))
                nextFa += self.V[j] * Ps
        
            nextFa *= a
    
            self.T.append(i)
            self.Fa.append(nextFa)
            self.algar += self.step * nextFa
            
    def retrieveData(self):
    
        self.mualist = [round(i, 1) for i in np.arange(0.0, 10.001, 0.1)]
        for mua in self.mualist:
            print(mua)
        
            counter = 0
        
            reflection = 0
            
            with open("data\\photonsformua" + str(mua) + ".csv", "r") as csvfile:
                    
                reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                    
                for row in reader:
                    """
                    counter += 1
                    
                    if counter > 10000:
                        break
                    """
                    if self.r - self.delta < float(row[0]) <= self.r + self.delta:
                        
                        reflection += float(row[1])
                        
                        if mua == 0.0:
                            self.weights.append(float(row[1]))
                            self.pathlengths.append(float(row[2]))
            
                self.reflections.append(reflection)
        
        AREA = math.pi * ((self.r + self.delta) ** 2 - (self.r - self.delta) ** 2)
        
        for i in range(len(self.reflections)):
            
            self.reflections[i] = self.reflections[i] / (AREA * 1000000)
            
        for i in range(len(self.weights)):
            self.weights[i] = self.pathlengths[i] / 1000000
            
        plt.figure()
        plt.plot(self.mualist, self.reflections)
        #plt.plot(mualist, reflections, 'bo')
        plt.show()
        
    def createData(self):
        
        function = globals()[self.formula]
        
        self.mualist = [round(i, 1) for i in np.arange(0.0, 40.001, 0.1)]
        
        for mua in self.mualist:
            
            reflection = function(mua, self)
            
            self.reflections.append(reflection)
        
    def algorithmOutcome(self):
        
        plt.figure()
        plt.plot(self.T, self.Fa)
        plt.plot(self.T, self.Fa, 'bo')
        plt.hist(self.pathlengths, bins = 100, weights = self.weights, color = 'r')
        plt.xlabel("t")
        plt.xlim(0., 5.)
        plt.ylabel("F")
        plt.title("Harald Stefest's algorithm", y = 1.08)
        plt.show()
        
        plt.figure()
        plt.hist(self.pathlengths, bins = 100, weights = self.weights, color = 'r')
        plt.xlim(0., 5.)
        plt.show()
        
    def numVsAn(self):
        
        function = globals()[self.FtFormula]
        Psfunction = globals()[self.formula]
        
        mualist = [round(i,1) for i in np.arange(0.0, 10.01, 0.1)]
        Ps = []
        
        for mua in mualist:
            
            Ps.append(Psfunction(mua, self))
            
        plt.figure()
        plt.plot(mualist, Ps)
        plt.xlabel('s')
        plt.ylabel('P')
        plt.title("Reflectance as a function of absorption coefficient")
        plt.show()
        
        Ft = []
    
        for i in self.T:
            
            nextFt = function(i, self)
        
            Ft.append(nextFt)
            
            self.anaar += self.step * nextFt
            
        normalize = self.algar / self.anaar
        
        #for i in range(len(Ft)):
        
            #Ft[i] = Ft[i] * normalize
        
        plt.figure()
        #plt.plot(self.T, self.Fa)
        plt.plot(self.T, self.Fa, 'bo')
        plt.plot(self.T, Ft, 'r-')
        #plt.plot(self.T, Ft, 'ro')
        plt.xlabel("t")
        plt.ylabel("F")
        plt.title("Analytical solution of a function vs Harald Stefest's algorithm", y = 1.08)
        plt.show()
        
        print(self.algar)
        print(self.anaar)
        print(normalize)