"""
25 April 2018 by Nathalie van Sterkenburg.
"""

import analytical_R_vs_r as ma
import simulation.main as mi
import matplotlib.pyplot as plt

def main():
    R, r = ma.main()
    ir_list, T = mi.main()
    
    plt.figure()
    plt.plot(r, R)
    plt.plot(ir_list, T, 'p-')
    plt.plot(ir_list, T, 'go')
    plt.show()
    
if __name__ == "__main__":
    main()