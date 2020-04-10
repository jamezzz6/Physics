import matplotlib.pyplot as plt
from vector3 import Vector3
from physics import Gravity, Entity
import itertools
import pygame

pygame.init()
pygame.display.set_caption('Earth according to Newton')
white = (255,255,255)
simulation_display = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()


ents = []
# Initialize sun
pos_sun = Vector3(0, 0, 0)
v0_sun = Vector3(0, 0, 0)
m_sun = 1.98847e30
sun = Entity(pos_sun, v0_sun, m_sun, [])
sun_img = pygame.image.load('sun.png')
ents.append(sun)

# Initialize earth
pos_earth = Vector3(1.4959787e11, 0, 0)
v0_earth = Vector3(0, 29.78e3, 0)
m_earth = 5.9722e24
earth = Entity(pos_earth, v0_earth, m_earth, [])
earth_img = pygame.image.load("earth.png")
ents.append(earth)

def update_celestial_objects(Sun,Earth):
    abs_to_rel = 4e11/800
    simulation_display.blit(sun_img, (sun.pos.x/abs_to_rel+400,sun.pos.y/abs_to_rel+400))
    simulation_display.blit(earth_img,(earth.pos.x/abs_to_rel+400,earth.pos.y/abs_to_rel+400))



##Add gravity between all entities
for o1, o2 in itertools.permutations(ents):
    o1.forces = [Gravity(o2, o1)]

# Time steps of 1/1000th of a day (in seconds)
dt = 0.001 * 365 * 24 * 60 * 60
N_steps = 990

# Time array
#ts = [dt * i for i in range(N_steps)]
p_log = []
v_log = []

crashed = False

xs = []
ys = [] #I'd like better logging
zs = [] #Maybe no logging, depends on where we go
vxs = []
vys = []
vzs = []

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)


    for o in ents:
        o.update(dt)  # update step for every physical entity
    simulation_display.fill(white)
    update_celestial_objects(sun, earth)
    xs.append(earth.pos.x)
    ys.append(earth.pos.y)
    zs.append(earth.pos.z)
    vxs.append(earth.velocity.x)
    vys.append(earth.velocity.y)
    vzs.append(earth.velocity.z)
    pygame.display.update()
    clock.tick(600)
pygame.quit()
plt.plot(xs, ys)
plt.show()



