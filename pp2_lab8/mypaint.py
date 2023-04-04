import pygame
import sys
WIDTH=800
HEIGHT=600
mode='red'
radius=10
pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
running=True
drawing=False
ptc=pygame.time.Clock()
FPS=1000
screen.fill((255,255,255))
color=(225,0,0)
circ=True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running=False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            if circ:
                circ = False
            else:
                circ = True

        elif event.type == pygame.MOUSEMOTION and drawing:
            if circ:
                pygame.draw.circle(screen, color, event.pos, radius)
            else:
                pygame.draw.rect(screen,color,pygame.Rect(event.pos[0],event.pos[1],radius,radius))
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]: radius+=0.5
        elif pressed[pygame.K_DOWN]:
            if radius>= 10:
                radius-=2.5
        if pressed[pygame.K_r] and event.type == pygame.MOUSEBUTTONUP : pygame.draw.rect(screen, color, pygame.Rect(event.pos[0], event.pos[1], radius, radius))
        if pressed[pygame.K_c] and event.type == pygame.MOUSEBUTTONUP : pygame.draw.circle(screen, color, event.pos, radius)
        if pressed[pygame.K_0]: screen.fill((255,255,255))
        if pressed[pygame.K_1]: color = ((0,0,0))#черный
        if pressed[pygame.K_2]: color = ((255,0,0))#красный
        if pressed[pygame.K_3]: color = ((0,255,0))#зеленый
        if pressed[pygame.K_4]: color = ((0,0,255))#синий
        if pressed[pygame.K_5]: color = ((255,255,0))#желтый
        if pressed[pygame.K_6]: color = ((255,0,255))#розовый
        if pressed[pygame.K_7]: color = ((0, 255, 255))#бирюзовый
        if pressed[pygame.K_9]: color = ((255, 255, 255))#ластик
        ptc.tick(FPS)
    pygame.display.flip()
