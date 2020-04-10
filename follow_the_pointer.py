from vector3 import Vector3
import pygame

pygame.init()
pygame.display.set_caption('Escape!')
white = (255, 255, 255)
display = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
speed  =0.005

clock = pygame.time.Clock()

mouse = Vector3(0,0,0)
mouse_img = pygame.image.load('earth.png')
abs_to_rel = 3000.0 / 800.0
rel_to_abs = 1/abs_to_rel

def update_mouse(mouse):
    display.blit(mouse_img, (mouse.x*abs_to_rel+400, mouse.y*abs_to_rel+400))

crashed = False
while not crashed:
    display.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    p = pygame.mouse.get_pos()
    print(p)
    pv = Vector3(p[0], p[1], 0)
    diff = rel_to_abs*(pv-Vector3(400,400,0))-mouse
    dm = speed*diff
    mouse += dm
    update_mouse(mouse)
    pygame.display.update()
    clock.tick(30)

