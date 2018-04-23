from reflect import reflect

class Photon:
    
    def __init__(self):
        
        self.x = 0.
        self.y = 0.
        self.z = 0.
        
        self.ux = 0.
        self.uy = 0.
        self.uz = 1.
        
        self.weight = 1.
        self.path = 0.
        self.nrreflect = 0.
    
    def change_position(self, s, prop):
        
        self.x += s * self.ux
        self.y += s * self.uy
        self.z += s * self.uz
        self.path += s
        
        if self.z < 0 and self.uz < 0:
            reflect(self, s, prop)