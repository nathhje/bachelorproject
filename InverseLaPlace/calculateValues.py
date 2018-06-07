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
    for i in range(1, N+1):
        G.append(G[i-1] * i)
        
    H = [1, 2 / G[Nh-1]]
    
    for i in range(2, Nh+1):
        H.append(i ** (Nh) * G[2*i] / (G[Nh-i] * G[i] * G[i-1]))
        
    sn = (-1) ** (N/2 + 1)
    
    V = [0]
    
    for i in range(1, N+1):
        V.append(0)
        limit = Nh+1
        
        if i < Nh:
            
            limit = i+1
            
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
    
    for i in range(1, N+1):
        
        Ps = getPs.exponential(a * i)
        
        Fa += V[i] * Ps
        
    Fa *= a
    
    return Fa