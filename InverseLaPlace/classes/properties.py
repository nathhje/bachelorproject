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
from helpers.getPs import polynomial
from helpers.getPs import exponent
from helpers.getFt import exponential as exponentialFt
from helpers.getFt import cosine as cosineFt
from helpers.getFt import reflectance as reflectanceFt
import numpy as np
import csv
import math

class Properties:
    
    def __init__(self):
        
        self.N = 22
        
        self.r = 1.
        
        self.delta = 0.1
        
        self.step = 0.1
        self.algar = 0.
        self.anaar = 0.
        self.normalize = 1.85
        
        self.mualist = []
        self.reflections = []
        self.formula = ""
        self.FtFormula = ""
        self.G = []
        self.H = []
        self.V = []
        self.T = []
        self.Fa = []
        
        self.Ps = []
        self.moreref = []
        self.s = []
        
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
    
    def createF(self):
    
        function = globals()[self.formula]
    
        for i in np.arange(0.1, 20., self.step):
            
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
            self.algar += self.step * nextFa
            
    def retrieveData(self):
        
        self.mualist = [round(i, 2) for i in np.arange(0.0, 10.001, 0.05)]
        for mua in self.mualist:
            print(mua)
        
            counter = 0
        
            reflection = 0
            
            with open("data\\photonsmua" + str(mua) + ".csv", "r") as csvfile:
                    
                reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                    
                for row in reader:
                    '''
                    counter += 1
                    
                    if counter > 10000:
                        break
                    '''
                    if self.r - self.delta < float(row[0]) <= self.r + self.delta:
                        
                        reflection += float(row[1])
                        
                        if mua == 0.0:
                            self.weights.append(float(row[1]))
                            self.pathlengths.append(float(row[2]))
            
                self.reflections.append(reflection)
                print(mua, reflection)
        
        AREA = math.pi * ((self.r + self.delta) ** 2 - (self.r - self.delta) ** 2)
        
        for i in range(len(self.reflections)):
            
            self.reflections[i] = self.reflections[i] / (AREA * 1000000)
            
        for i in range(len(self.weights)):
            self.weights[i] = self.pathlengths[i] / 1000000
            
        plt.figure()
        plt.title(r"Reflectance as a function of absorption coefficient at $r=1cm$")
        plt.xlabel(r"$\mu_a (cm^{-1})$")
        plt.ylabel(r"$R (cm^{-2})$")
        plt.plot(self.mualist, self.reflections)
        plt.legend(["directly from data set"])
        #plt.plot(mualist, reflections, 'bo')
        plt.show()
        
    def createData(self):
        
        function = globals()[self.formula]
        
        self.mualist = [round(i, 3) for i in np.arange(0.0, 40.001, 0.05)]
        
        for mua in self.mualist:
            
            reflection = function(mua, self)
            
            self.reflections.append(reflection)
            
            
    def getAnalytical(self):
            
            function = globals()[self.FtFormula]
            
            self.Ft = []
    
            for i in self.T:
            
                nextFt = function(i, self)
        
                self.Ft.append(nextFt * self.normalize)
            
                self.anaar += self.step * nextFt
        
    def algorithmOutcome(self):
        
        plt.figure()
        #plt.plot(self.T, self.Fa)
        plt.plot(self.T, self.Fa, 'bo')
        plt.hist(self.pathlengths, bins = 100, weights = self.weights, color = 'r')
        plt.xlabel(r"$r (cm)$")
        plt.ylabel(r"frequency $(cm^-{2})$")
        plt.title(r"Path length distribution at $r=1cm$")
        plt.legend(["algorithm used on dataset"])
        plt.show()
        
        plt.figure()
        plt.title(r"Path length distribution at $r=1cm$")
        plt.xlabel(r"$r (cm)$")
        plt.ylabel(r"frequency $(cm^-{2})$")
        plt.hist(self.pathlengths, bins = 100, weights = self.weights, color = 'r')
        plt.legend(["directly from data set"])
        plt.show()
        
    def algorithmOnlyOutcome(self):
        
        plt.figure()
        plt.plot(self.T, self.Fa, 'bo' )
        plt.xlabel(r"$r (cm)$")
        plt.ylabel(r"frequency $(cm^{-2})$")
        plt.title(r"Path length distribution at $r=1cm$")
        plt.legend(["algorithm used on a fit of the data set"])
        plt.show()
        
    def numVsAn(self):
        
        self.getAnalytical()
        
        plt.figure()
        #plt.plot(self.T, self.Fa)
        plt.plot(self.T, self.Fa, 'ro')
        #plt.plot(self.T, self.Ft, 'b-')
        #plt.plot(self.T, Ft, 'ro')
        plt.xlabel(r"$t$")
        plt.ylabel(r"$F$")
        plt.title(r"Exponential function")
        plt.legend(["random deviation in algorithm", "analytical"])
        plt.show()
        
        print(self.algar)
        print(self.anaar)
        
    def PsCompare(self):
            
        plt.figure()
        plt.plot(self.s, self.moreref, 'bs')
        plt.plot(self.s, self.Ps, 'r.')
        plt.xlabel(r'$s$')
        plt.ylabel(r'$P$')
        plt.legend(("exact", "random deviation"))
        plt.title(r"Laplace transform of an exponential function")
        plt.show()