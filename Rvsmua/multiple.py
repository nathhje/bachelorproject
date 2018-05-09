# -*- coding: utf-8 -*-
"""
Created on Tue May  8 10:27:53 2018

@author: Sterkenburg
"""

import main as m
import matplotlib.pyplot as plt

def main():
    
    mua_list1, T1 = m.main(0.1)
    mua_list2, T2 = m.main(0.2)
    mua_list3, T3 = m.main(0.3)
    
    plt.figure()
    plt.plot(mua_list1, T1, 'bo')
    plt.plot(mua_list2, T2, 'go')
    plt.plot(mua_list3, T3, 'ro')
    plt.title("Reflectance as a function of absorption coefficient")
    plt.xlabel("mua (cm^-1)")
    plt.ylabel("R (cm^-2)")
    
    plt.figure()
    plt.plot(mua_list1, T1, 'bo')
    plt.plot(mua_list2, T2, 'go')
    plt.plot(mua_list3, T3, 'ro')
    plt.title("Reflectance as a function of absorption coefficient")
    plt.xlabel("mua (cm^-1)")
    plt.ylabel("R (cm^-2)")
    plt.yscale('log')
    plt.show()
    
if __name__ == "__main__":
    main()