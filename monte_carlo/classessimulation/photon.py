"""
12 April 2018 by Nathalie van Sterkenburg.
Contains a class for a photon. The class keeps track of the photon position,
direction and speed as well as it's weight and pathlength and number of times
reflected. Also has a function for updating the position.
"""

from helpers.reflect import reflect

class Photon:
    """ Keeps track of a photon. """
    
    def __init__(self):
        
        # The photons position.
        self.x = 0.
        self.y = 0.
        self.z = 0.
        
        # The photons direction.
        self.ux = 0.
        self.uy = 0.
        self.uz = 1.
        
        # Photon weight, covered pathlength and number of times reflected.
        self.weight = 1.
        self.path = 0.
    
    def change_position(self, s, prop):
        """ 
        Updates the photons position and checks if it has to be reflected. 
        s is the length of the step the photon has to take.
        """
        
        # Updates position.
        self.x += s * self.ux
        self.y += s * self.uy
        self.z += s * self.uz
        
        # Increases the total pathlength covered.
        self.path += s
        
        # Checkes if the photon has crossed the boundary...
        if self.z < 0 and self.uz < 0:
            
            # ... reflects the photon if it did.
            reflect(self, s, prop)