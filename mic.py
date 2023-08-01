import numpy as np

class Mic():
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def dist(self,mic):
        return np.sqrt((self.x-mic.x)**2+(self.y-mic.y)**2+(self.z-mic.z)**2)