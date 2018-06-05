# -*- coding: utf-8 -*-
"""
Created on Tue May 29 10:29:14 2018

@author: Gebruiker
"""

import getPs

def V(N):
    
    Nh = int(N / 2)
    print(Nh)
    G = [1]
    for i in range(1, N):
        G.append(G[i-1] * i)
        
    H = [1, 2 / G[Nh-1]]
    
    for i in range(2, Nh):
        H.append(i ** (Nh+1) * G[2*i] / (G[Nh-i] * G[i] * G[i-1]))
        
    sn = (-1) ** (N/2 + 1)
    
    V = [0]
    
    for i in range(1, N):
        V.append(0)
        limit = Nh
        
        if i < Nh:
            
            limit = i
            
        for k in range(int((i+1) / 2), limit, 1):
            
            V[i] += H[k] / (G[i-k] * G[2 * k - i])
            
        V[i] *= sn
        
        sn = - sn
        
    print(G)
    print(H)
    print(V)
    
    return V

def F(V, N, T):
    
    a = 0.69314 / T
    
    Fa = 0
    
    for i in range(1, N):
        
        Ps = getPs.exponential(a * i)
        
        Fa += V[i] * Ps
        
    Fa *= a
    
    return Fa