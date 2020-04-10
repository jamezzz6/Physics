import matplotlib.pyplot as plt
from vector3 import Vector3
from physics import Gravity, Entity
import itertools

ents = []
# Initialize sun
pos_sun = Vector3(0, 0, 0)
v0_sun = Vector3(0, 0, 0)
m_sun = 1.98847e30
sun = Entity(pos_sun, v0_sun, m_sun, [])
ents.append(sun)
# Initialize earth
pos_earth = Vector3(1.4959787e11, 0, 0)
v0_earth = Vector3(0, 29.78e3, 0)
m_earth = 5.9722e24
earth = Entity(pos_earth, v0_earth, m_earth, [])
ents.append(earth)

##Add gravity between all entities
for o1, o2 in itertools.permutations(ents):
    o1.forces = [Gravity(o2, o1)]

# Time steps of 1/1000th of a day (in seconds)
dt = 0.001 * 365 * 24 * 60 * 60
N_steps = 990

# Time array
ts = [dt * i for i in range(N_steps)]
p_log = []
v_log = []
for _ in ts:
    for o in ents:
        o.update(dt)  # update step for every physical entity
    p_log.append(earth.pos)
    v_log.append(earth.velocity)








xs = [p.x for p in p_log]
ys = [p.y for p in p_log]
zs = [p.z for p in p_log]
vxs = [v.x for v in v_log]
vys = [v.y for v in v_log]
vzs = [v.z for v in v_log]

plt.plot(xs, ys)
plt.show()
