import math

def reflect(photon, s, prop):
    
    photon.nrreflect += 1
    photon.x -= s * photon.ux
    photon.y -= s * photon.uy
    photon.z -= s * photon.uz
    
    s1 = abs(photon.z / photon.uz)
    
    photon.x += s1 * photon.ux
    photon.y += s1 * photon.uy
    photon.z = 0
    
    photon.uz = -1 * photon.uz
    
    cost = photon.uz
    sint = (1 - photon.uz ** 2) ** 0.5
    sinf = math.sin( math.asin(sint) * (prop.n/prop.n1))
    cosf = (1 - sint **2) ** 0.5
    
    Ri = (((sint * cosf - cost * sinf) ** 2) / 2) * (((cost * cosf + sint * sinf) 
            ** 2 + (cost * cosf - sint * sinf) ** 2) / ((sint * cosf + cost * sinf) 
            ** 2 * (cost * cosf + sint * sinf) ** 2))
            
    """
    print "uz"
    print photon.uz
    print "sint"
    print sint
    print "sinf"
    print sinf
    print "cosf"
    print cosf
    print "Ri"
    print Ri
    """
    r = (photon.x ** 2 + photon.y ** 2) ** 0.5
    
    ir = int(round(r / prop.dr))
    
    if ir >= prop.BINS:
        ir = prop.BINS - 1
        
    prop.R[ir] += (1 - Ri) * photon.weight
    prop.totalR += (1 - Ri) * photon.weight
    photon.weight = Ri * photon.weight
    
    prop.pathlengths.append(photon.path)
    
    photon.uz = - photon.uz
    
    photon.x += (s - s1) * photon.ux
    photon.y += (s - s1) * photon.uy
    photon.z += (s - s1) * photon.uz