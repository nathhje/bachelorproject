# -*- coding: utf-8 -*-
"""
A class which contaisn all constants, lists and functions that are needed to
perform Harald Stehfest's algorithm.
"""

import matplotlib.pyplot as plt
from helpers.getPs import exponential
from helpers.getPs import cosine
from helpers.getPs import dataset
from helpers.getPs import reflectance
from helpers.getPs import fit
from helpers.getPs import exponentialSys
from helpers.getPs import exponentialRand
from helpers.getFt import exponential as exponentialFt
from helpers.getFt import cosine as cosineFt
from helpers.getFt import reflectance as reflectanceFt
import numpy as np
import csv
import math

class Properties:
    
    def __init__(self):
        """ A collection of all variables and lists used in the algorithm. """
        
        # The number of points used to determine F(T)
        # Optimal solution depends on computer accuracy, was 22 for the computer
        # the code was used on
        self.N = 22
        
        # The radial distance at which the path length distribution is determined
        # in cm
        self.r = 1.
        
        # The range of radial distances that are close enough to self.r to be
        # selected from the data set
        self.delta = 0.1
        
        # The space between two points of the mualist, helps determine the right
        # index when interpolating
        self.deltamua = 0.05
        
        # The space between two path lengths in the path length distribution,
        # used in creating F
        self.step = 0.1
        
        # The area beneath the graph of the outcome of the algorithm and the
        # analytical solution
        self.algar = 0.
        self.anaar = 0.
        
        # The normalization constant of the analytical solution for the used 
        # data set with the used N
        self.normalize = 1.85
        
        # The lists that contain data for the reflectance vs mua graph
        self.mualist = []
        self.reflections = []
        
        # These strings determine what function will be used for P(s) and F(t)
        self.formula = ""
        self.FtFormula = ""
        
        # Lists that help create V
        self.G = []
        self.H = []
        
        # Used for determining F
        self.V = []
        
        # Used to save the outcome of the algorithm
        self.T = []
        self.Fa = []
        
        # Used to save all points on P(s) that the algorithm uses and plot F(t)
        self.Ps = []
        self.s = []
        
        # Used to save all points of the exact analytical version of P(s) that
        # the algorithm uses and used to compare with P(s)
        self.moreref = []
        
        # Used for creating a histogram of path length distribution directly
        # from the data set.
        self.weights = []
        self.pathlengths = []
        
    def algorithm(self):
        """ Runs the algorithm. """
        
        self.createV()
        
        self.createF()
        
    def createV(self):
        """ Creates the list of V which is used to determine all points F(T). """
    
        Nh = int(self.N / 2)
        
        # List G is a list of factorials, G[i] = i!
        self.G.append(1)
        
        for i in range(1, self.N+1):
            self.G.append(self.G[i-1] * i)
        
        # List G is created
        self.H = [1, 2 / self.G[Nh-1]]
    
        for i in range(2, Nh+1):
            self.H.append(i ** (Nh) * self.G[2*i] / (self.G[Nh-i] * self.G[i] * self.G[i-1]))
        
        # Determines for each value in V if it's positive or negative
        sn = (-1) ** (self.N/2 + 1)
    
        # List V is created
        self.V.append(0)
    
        for i in range(1, self.N+1):
            
            self.V.append(0)
            
            # The limit is determined as the lowest of two values
            limit = Nh+1
        
            if i < Nh:
            
                limit = i+1
            
            # V[i] is determined
            for k in range(int((i+1) / 2), limit, 1):
            
                self.V[i] += self.H[k] / (self.G[i-k] * self.G[2 * k - i])
            
            self.V[i] *= sn
        
            sn = - sn
    
    def createF(self):
        """ Determines each point F(T). """
    
        # The correct function to use as P(s) is determined
        function = globals()[self.formula]
    
        # Loops through all F(T)
        for i in np.arange(0.01, 20., self.step):
            
            a = 0.69314 / i
            nextFa = 0
            
            # Determines the value of this F(T)
            for j in range(1, self.N+1):
                
                # s = a*j
                Ps = function(a * j, self)
                if Ps < 0:
                    Ps = 0
                    
                nextFa += self.V[j] * Ps
        
            nextFa *= a
    
            self.T.append(i)
            self.Fa.append(nextFa)
            self.algar += self.step * nextFa
            
    def retrieveData(self):
        """ Retrieves all reflectance and mua for the correct r. """
        
        # The data is saved by mua, so a list of all available mua is created
        self.mualist = [round(i, 2) for i in np.arange(0.0, 10.001, self.deltamua)]
        
        for mua in self.mualist:
            print(mua)
        
            # For each mua the corresponding file is opened and searched
            with open("data\\photonsformua" + str(mua) + ".csv", "r") as csvfile:
                    
                reflection = 0
                
                reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                
                # For each reflection with this mua, it is checked if it is in
                # right range for r
                for row in reader:
                    
                    if self.r - self.delta < float(row[0]) <= self.r + self.delta:
                        
                        # If it is, its weight is saved as reflectance
                        reflection += float(row[1])
                        
                        # the path length distribution can be gained from the
                        # mua=0 file
                        if mua == 0.0 and float(row[2]) < 40.:
                            self.weights.append(float(row[1]))
                            self.pathlengths.append(float(row[2]))
            
                self.reflections.append(reflection)
        
        # The data path length distribution from mua=0 is normalized
        AREA = math.pi * ((self.r + self.delta) ** 2 - (self.r - self.delta) ** 2)
        
        for i in range(len(self.reflections)):
            
            self.reflections[i] = self.reflections[i] / (AREA * 1000000)
            
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] / 1000000
            
        # The path length distribution from the data set is plotted
        plt.figure()
        plt.title(r"Reflectance as a function of absorption coefficient at $r=1cm$")
        plt.xlabel(r"$\mu_a (cm^{-1})$")
        plt.ylabel(r"$R (cm^{-2})$")
        plt.yscale('log')
        plt.plot(self.mualist, self.reflections)
        plt.legend(["directly from data set"])
        plt.show()
        
    def createData(self):
        """ Creates a discrete list of data points from an exact function, to
        test how interpolation affects the outcome. """
        
        # The right function is chosen to create the list
        function = globals()[self.formula]
        
        # The range of the discrete set is established
        self.mualist = [round(i, 3) for i in np.arange(0.0, 40.001, self.deltamua)]
        
        # The set is created
        for mua in self.mualist:
            
            reflection = function(mua, self)
            
            self.reflections.append(reflection)
            
        plt.figure()
        plt.title(r"Reflectance as a function of absorption coefficient at $r=1cm$")
        plt.xlabel(r"$\mu_a (cm^{-1})$")
        plt.ylabel(r"$R (cm^{-2})$")
        plt.yscale('log')
        plt.plot(self.mualist, self.reflections)
        plt.legend(["directly from data set"])
        plt.show()
            
            
    def getAnalytical(self):
        """ Makes a list with the analytical solution to the inverse Laplace
        transform to compare to the outcome of the algorithm. """
            
        # The right function for F(t) is determined
        function = globals()[self.FtFormula]
            
        self.Ft = []
    
        # for each T the right value is determined
        for i in self.T:
            
            nextFt = function(i, self)
        
            # The outcome is normalized (normalize=1 for functions that don't 
            # have to be normalized)
            self.Ft.append(nextFt * self.normalize)
            
            # The area under the graph, for normalization purposes
            self.anaar += self.step * nextFt
        
    def algorithmOutcome(self):
        """ Plots the outcome of the algorithm and the path length distribution
        from the data set. """
        
        # The outcome of the algorithm
        plt.figure()
        plt.plot(self.T, self.Fa, 'bo')
        plt.xlabel(r"$l(cm)$")
        plt.ylabel(r"$p(l)$")
        plt.title(r"Path length distribution at $r=1cm$")
        plt.legend(["algorithm used on dataset"])
        plt.show()
        
        # A histogram of the path length distribution from the data set
        plt.figure()
        plt.xlabel(r"$l(cm)$")
        plt.ylabel(r"$p(l)$")
        plt.title(r"Path length distribution at $r=1cm$")
        plt.hist(self.pathlengths, bins = 100, weights = self.weights, color = 'r')
        plt.legend(["directly from dataset"])
        plt.show()
        
    def algorithmOnlyOutcome(self):
        """ Plots the outcome of the algorithm. """
        
        plt.figure()
        plt.plot(self.T, self.Fa, 'bo' )
        plt.xlabel(r"t")
        plt.ylabel(r"F")
        plt.title(r"The inverse Laplace transform")
        plt.show()
        
    def numVsAn(self):
        """ Plots the outcome of the algorithm and analytical solution for the
        inverse Laplace transform. """
        
        # The analytical solution is determined
        self.getAnalytical()
        
        # Both functions are plotted in the same figure
        plt.figure()
        plt.plot(self.T, self.Fa, 'ro')
        #plt.plot(self.T, self.Ft, 'b-')
        plt.xlabel(r"$t$")
        plt.ylabel(r"$F$")
        plt.title(r"Exponential function")
        plt.legend(["random deviation in algorithm"])
        plt.show()
        
    def PsCompare(self):
        """ Plots the function the algorithm was used on and the exact analytical
        version of this function to check if the altered function is accurate. 
        """ 
            
        plt.figure()
        plt.plot(self.s, self.moreref, 'bs')
        plt.plot(self.s, self.Ps, 'r.')
        plt.xlabel(r'$s$')
        plt.ylabel(r'$P$')
        plt.legend(("exact", "random deviation"))
        plt.title(r"Laplace transform of an exponential function")
        plt.yscale('log')
        plt.show()
        
    def PsOnly(self):
        """ Plots the function the algorithm was used on to check if nothing
        obvious is going wrong. """
        
        plt.figure()
        plt.plot(self.s, self.Ps, 'r.')
        plt.xlabel(r'$s$')
        plt.ylabel(r'$P$')
        plt.title(r"Laplace transform of an exponential function")
        plt.legend(("exact", "interpolation"))
        plt.yscale('log')
        plt.show()