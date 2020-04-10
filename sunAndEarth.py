import matplotlib.pyplot as plt
from vector3 import Vector3
from physics import Gravity, Entity



pos_sun = Vector3(0, 0, 0)
v0_sun = Vector3(0, 0, 0)
m_sun = 1.98847e30
sun   = Entity(pos_sun, v0_sun, m_sun, [])

pos_earth = Vector3(1.4959787e11, 0,0)
v0_earth = Vector3(0, 29.78e3, 0)
m_earth = 5.9722e24
earth = Entity(pos_earth, v0_earth, m_earth, [])

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