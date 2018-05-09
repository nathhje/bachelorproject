# -*- coding: utf-8 -*-
"""
Created on Tue May  8 09:37:08 2018

@author: Sterkenburg
"""

import main as m
import matplotlib.pyplot as plt

def main():
    
    ir_list1, T1 = m.main(0.1)
    ir_list2, T2 = m.main(1.)
    ir_list3, T3 = m.main(2.)
    
    plt.figure()
    plt.plot(ir_list1, T1, 'bo')
    plt.plot(ir_list2, T2, 'go')
    plt.plot(ir_list3, T3, 'ro')
    plt.yscale("log")
    plt.xlim(0.01, 0.35)
    plt.ylim(10**-2, 10**2)
    plt.title("Reflectance as a function of radius")
    plt.xlabel("r (cm)")
    plt.ylabel("R (cm^-2)")
    plt.show()
    
if __name__ == "__main__":
    main()