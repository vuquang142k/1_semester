import pygame, sys
from math import *
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((600, 500))
x0, y0 = 85, 400
anpla = radians(60)
v = 70
t = 0
g = 10
r = 25  
scale = 1
ymin = y0

def chuyen(xs, ys, x, y, t):
    xss = (x - xs) * cos(radians(t*50)) + (y - ys) * sin(radians(t*50)) + xs
    yss = (x - xs) * -sin(radians(t*50)) + (y - ys) * cos(radians(t*50)) + ys
    return (xss, yss)

while True:
    window.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.draw.polygon(window, (255,0,0), ((0, 500), (60, 400), (110, 400), (170, 500)))
    pygame.draw.ellipse(window, (0,255,0), Rect((60, 390), (50, 25)))
    x = x0 + t * v * cos(anpla)
    y = y0 - t * v * sin(anpla) +  1/2 * g * t * t
    if y < ymin:
        ymin = y
        scale -= 0.0125
    else:
        scale += 0.0125
    x1 = r * cos(radians(60))*scale
    y1 = r * sin(radians(60))*scale
    
    pygame.draw.polygon(window, (0,0,255), [chuyen(x, y, x -x1, y - y1, t), chuyen(x, y, x + x1, y - y1, t), chuyen(x, y, x + r*scale, y, t), chuyen(x, y, x + x1, y+y1, t), chuyen(x, y, x - x1, y+y1, t), chuyen(x, y, x - r*scale, y, t)])
    t += 0.1
    if x > 600 or y< 0 or y > 500:
        t = 0
        scale = 1
        ymin = y0
    pygame.display.update()
    clock.tick(90)
    #