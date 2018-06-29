"""
Contains a function that reflects a photon when it crosses the boundary. Part
of the weight is let through and saved as radial reflectance, the rest is send 
back into the tissue to continue propagating.
"""

def reflect(photon, s, prop):
    """ 
    Reflects a photon against the boundary.
    
    photon: the instance of the absorbed photon.
    s: length of the previous step the photon has taken.
    prop: contains all constants, methods of saving and outputs.
    """
    
    # The photon has already taken a step to cross the boundary, so it now has
    # to take the same step back.
    photon.x -= s * photon.ux
    photon.y -= s * photon.uy
    photon.z -= s * photon.uz
    
    # Another stepsize is calculated that will put the photon on the boundary.
    s1 = abs(photon.z / photon.uz)
    
    # The photon takes this step.
    photon.x += s1 * photon.ux
    photon.y += s1 * photon.uy
    photon.z = 0
    
    # The velocity in the z-direction is reversed so the photon goes back.
    photon.uz = -1 * photon.uz
    
    if photon.uz == 1.0:
        Ri = 0
    
    else:
        # The goniometric parameters are calculated that are used for determining 
        # the part of the photon weight that will be reflected.
        cost = photon.uz
        sint = (1 - photon.uz ** 2) ** 0.5
        sinf = sint * prop.n/prop.n1
        cosf = (1 - sint **2) ** 0.5
        
        # The fraction of the photon weight that continues propagating is determined.
        Ri = (((sint * cosf - cost * sinf) ** 2) / 2) * (((cost * cosf + sint * sinf) 
                ** 2 + (cost * cosf - sint * sinf) ** 2) / ((sint * cosf + cost * sinf) 
                ** 2 * (cost * cosf + sint * sinf) ** 2))
    
    # The radius from the source is determined
    r = (photon.x ** 2 + photon.y ** 2) ** 0.5
    
    # The weight that is let through
    goneweight = (1 - Ri) * photon.weight
    
    # How the removed weight is stored depents on how he simulation is run
    if prop.name == "Rvsr":
        
        prop.RvsrReflect(r, goneweight)
        
    elif prop.name == "RvsMua":
        
        prop.RvsMuaReflect(r, goneweight)
        
    elif prop.name == "savePhotons":
        
        prop.savePhotonsReflect(r, goneweight, photon, s1)
    
    # Weight is updated
    photon.weight = Ri * photon.weight
    
    # The second part of the initial step is taken.
    photon.x += (s - s1) * photon.ux
    photon.y += (s - s1) * photon.uy
    photon.z += (s - s1) * photon.uz