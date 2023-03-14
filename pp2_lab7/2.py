import pygame
pygame.init()

#Global Variables
WIDTH, HEIGHT = 500, 500
FPS = 20

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Initialization
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MUSIC PLAYER")

clock = pygame.time.Clock()
finished = False

img = pygame.image.load("./img/image.png")

playlist = []
playlist.append("./music/music.mp3")
playlist.append("./music/music1.mp3")
playlist.append("./music/bob.mp3")
playlist.append("./music/audio.mp3")

def get_next():
    global playlist
    playlist = playlist[1:] + [playlist[0]]
    pygame.mixer.music.load(playlist[0])
    pygame.mixer.music.play()
    
pygame.mixer.music.load(playlist.pop()) 
# pygame.mixer.music.set_endevent(pygame.USEREVENT)    
pygame.mixer.music.play()  

def get_prev():
    global playlist
    playlist = [playlist[-1]] + playlist [:-1]
    pygame.mixer.music.load(playlist[0])
    pygame.mixer.music.play()

while not finished:
    clock.tick(FPS)
    # screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        screen.blit(img, (0, 0))
        if event.type == pygame.KEYDOWN:   
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    pygame.mixer.music.stop()
                    get_next()
                if event.key==pygame.K_RIGHT:
                    pygame.mixer.music.stop()
                    get_prev()
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.pause()
                if event.key==pygame.K_p:
                    pygame.mixer.music.unpause()
    pygame.display.flip()
pygame.quit()