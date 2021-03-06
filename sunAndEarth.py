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
sun_img = pygame.image.load("sun.png")
ents.append(sun)

# Initialize earth
pos_earth = Vector3(1.4959787e11, 0, 0)
v0_earth = Vector3(0, 29.78e3, 0)
m_earth = 5.9722e24
earth = Entity(pos_earth, v0_earth, m_earth, [])
earth_img = pygame.image.load("earth.png")
ents.append(earth)

# Initialize moon
pos_moon = pos_earth + Vector3(0, 3.844e8, 0)
v0_moon  = v0_earth +Vector3(1.023e3,0,0) #This might be the wrong direction, let me fix that visually...
m_moon =7.35e22
moon = Entity(pos_moon, v0_moon, m_moon, [])
moon_img = pygame.image.load("moon.png")
ents.append(moon)

def update_celestial_objects(Sun,Earth):
    abs_to_rel = 4e11/800
    simulation_display.blit(sun_img, (sun.pos.x/abs_to_rel+400,sun.pos.y/abs_to_rel+400))
    simulation_display.blit(earth_img,(earth.pos.x/abs_to_rel+400,earth.pos.y/abs_to_rel+400))
    simulation_display.blit(moon_img, (moon.pos.x/abs_to_rel+400, earth.pos.y/abs_to_rel+400))


##Add gravity between all entities
for o1, o2 in itertools.permutations(ents, 2):
    o1.forces.append(Gravity(o2, o1))

# Time steps of 1/1000th of a day (in seconds)
dt = 0.01 * 24 * 60 * 60
N_steps = 990

p_log = []
v_log = []

crashed = False
## Initiate loggers
start_time = 0
ts = [start_time]
xs = [moon.pos.x-earth.pos.x]
ys = [moon.pos.y-earth.pos.y] #I'd like better logging capabilities

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    for o in ents:
        o.compute_update(dt)  # update step for every physical entity
    for o in ents:
        o.apply_update()
    simulation_display.fill(white)
    update_celestial_objects(sun, earth)
    ## Logging
    ts.append(ts[-1]+dt) # allows for dynamical dt
    xs.append(moon.pos.x-earth.pos.x)
    ys.append(moon.pos.y-earth.pos.y)
    pygame.display.update()
    clock.tick(6000)
pygame.quit()
plt.plot(xs, ys)
plt.show()



