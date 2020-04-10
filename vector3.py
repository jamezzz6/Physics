from math import sqrt
class Vector3:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z+other.z)

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return  Vector3(other*self.x, other*self.y, other*self.z)
    __rmul__ = __mul__

    def __str__(self):
        return "".join(['(',str(self.x),', ',str(self.y),', ',str(self.z),')'])

    def squared_norm(self):
        return self.x*self.x+self.y*self.y+self.z*self.z
    def norm(self):
        return sqrt(self.squared_norm())
