import pygame 
from datetime import datetime 

pygame.init() 
 
#global Variables 
WIDTH, HEIGHT = 800 , 600
FPS = 10

BLACK = (0, 0, 0) 
 
def blitRotateCenter(surf, image, topleft, angle): 
     
    rotated_image = pygame.transform.rotate(image, angle) 
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center) 
 
    surf.blit(rotated_image, new_rect) 
 
#Initializing 
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Mickey's clock") 
 
#variables 
x, y = WIDTH // 2, HEIGHT // 2 
color = BLACK 
RAD = 10 
 
#img 
mickey = pygame.image.load('./img/mickeyN.png') 
mickey = pygame.transform.scale(mickey, (WIDTH, HEIGHT)) 
right_hand = pygame.image.load('./img/min.png') 
left_hand = pygame.image.load('./img/sec.png') 
 
 
pygame.mixer.music.load("./music/tick.mp3") 
pygame.mixer.music.play(-1) 
 
clock = pygame.time.Clock() 
 
finished = False 
 
def time(time): 
    return 360 - time * 6 
 
while not finished: 
    clock.tick(FPS) 
 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            finished = True 
 
    screen.blit(mickey, (0, 0)) 
 
    t = datetime.now() 
 
    angle_sec = time(t.second + 1) 
    angle_min = time(t.minute) 
 
    blitRotateCenter(screen, left_hand, (WIDTH // 4 - 52, HEIGHT // 4 - 100), angle_sec) 
    blitRotateCenter(screen, right_hand , (WIDTH // 4 - 52, HEIGHT // 4 - 100), angle_min) 
     
    pygame.draw.circle(screen, color, (x, y), RAD) 
     
    pygame.display.flip() 
pygame.quit()