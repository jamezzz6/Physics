import matplotlib.pyplot as plt
import pprint
from numpy import sqrt
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

class Force:
    def __init__(self, source, target):
        self.source = source
        self.target = target
    def evaluate(self):
        raise NotImplementedError


class Gravity(Force):
    def evaluate(self):
        G = 6.67430e-11
        diff_vector =self.source.pos-self.target.pos
        amplitude =  G*self.source.mass*self.target.mass/diff_vector.squared_norm()
        return amplitude/diff_vector.norm()*diff_vector


class Object:
    def __init__(self, pos, velocity,mass, forces):
        self.pos = pos
        self.mass = mass
        self.inverse_mass = 1./mass
        self.velocity = velocity
        self.forces = forces

    def update(self, delta_t):
        self.pos += delta_t*self.velocity
        for f in self.forces:
            print(f.evaluate())
            self.velocity += f.evaluate()*self.inverse_mass*delta_t



pos_sun = Vector3(0, 0, 0)
v0_sun = Vector3(0, 0, 0)
m_sun = 1.98847e30
sun   = Object(pos_sun, v0_sun, m_sun,[])

pos_earth = Vector3(1.4959787e11, 0,0)
v0_earth = Vector3(0, 29.78e3, 0)
m_earth = 5.9722e24
earth = Object(pos_earth, v0_earth,m_earth, [])

sun.forces   = [Gravity(earth, sun)]
earth.forces = [Gravity(sun, earth)]


dt = 0.001*365*24*60*60
Nsteps =990

ts = [dt*i for i in range( Nsteps)]
poslog = []
vlog   = []
for _ in ts:
    earth.update(dt)
    sun.update(dt)
    poslog.append(earth.pos)
    vlog.append(earth.velocity)
xs = [p.x for p in poslog]
ys = [p.y for p in poslog]
zs = [p.z for p in poslog]
vxs = [v.x for v in vlog]
vys = [v.y for v in vlog]
vzs = [v.z for v in vlog]

plt.plot(xs,ys)
plt.show()