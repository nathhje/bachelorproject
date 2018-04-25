import analytical
import math
import matplotlib.pyplot as plt
import numpy as np

def output(prop):
    print("output")
    print(prop.totalR)
    for ir in range(prop.BINS):
        
        V = 2 * math.pi * (ir - 0.5) * prop.dr ** 2 * prop.dz
        
        AREA = 2 * math.pi * (ir - 0.5) * prop.dr ** 2
        
        
        prop.R[ir] = prop.R[ir] / (AREA * prop.N)
        
        for iz in range(prop.BINS):
            
            prop.A[ir, iz] = prop.A[ir, iz] / (V * prop.N)
    
    
    ir_list = [i for i in np.arange(0.01, prop.rmax - prop.dr - 0.5 * prop.dr, prop.dr)]
    iz_list = [i for i in np.arange(prop.dz, prop.zmax - prop.dz - 0.5 * prop.dz, prop.dz)]
    
    B = np.zeros([prop.BINS - 2, prop.BINS - 2])
    
    counter = 0
    anothercounter = 0
    
    for ir in range(prop.BINS - 2 - len(ir_list), prop.BINS - 2):
        
        anothercounter += 1
    
        for iz in range(prop.BINS - 2):
            
            j = ir + 1
            k = iz + 1
            
            B[ir, iz] = prop.A[j, k]
            counter += 1
            
    T = []
    
    for ir in range(prop.BINS - 2 - len(ir_list), prop.BINS - 2):
        
        T.append(prop.R[ir + 1])
    
    ir_matrix, iz_matrix = np.meshgrid(ir_list, iz_list)
    
    print("last stuff")
    print(len(prop.pathlengths))
    print(T[0])
    print(T[1])
    """
    plt.figure()
    plt.hist(pathlengths)
    plt.show()
    """
    plt.figure()
    plt.plot(ir_list, T, 'p-')
    plt.plot(ir_list, T, 'go')
    plt.title("500 bins")
    plt.xlabel("r(cm)")
    plt.ylabel("R(cm^-2)")
    plt.show()
    """
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    surf = ax.plot_surface(ir_matrix, iz_matrix, B, cmap=plt.cm.coolwarm, linewidth=0, antialiased=False)
    ax.set_xlabel("r (cm)")
    ax.set_ylabel("z (cm)")
    ax.set_zlabel("A")
    fig.colorbar(surf, shrink=0.5, aspect=5, label = "Value of A")
    plt.show()
    """
    
    R, r = analytical.main()
    
    plt.figure()
    plt.plot(ir_list, T, 'p-')
    plt.plot(ir_list, T, 'go')
    plt.plot(r, R)
    plt.xlim(0.01, 1.)
    plt.show()
    
    return ir_list, T