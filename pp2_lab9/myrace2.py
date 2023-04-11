import pygame as pg #import libs
import random
pg.init()#pygame init
Bg = pg.image.load("C:\\Users\\User\\Desktop\\Программирование\\my\\pp2-22B030391\\tsis8\\2\\Bg.png")#loading background image #####from tsis 8 all images
Br = Bg.get_rect()#getting rectangle of background image
Bw, Bh = Br[2],Br[3]#and its width height 
W = Bw#width of screen that equal to images width....
H = Bh#height .of screen that equal to images height
fps = 30#FPS
WHITE = ((255,255,255))#RGB colors
RED = ((255,0,0))
GREEN = ((0,255,0))
BLACK = ((0,0,0))
scr = pg.display.set_mode((W,H))#SCREEN SETTING
clock = pg.time.Clock()#time setting
my_font = pg.font.SysFont('Verdana', 20)# text style setting
game_over = my_font.render("Game Over", True, RED)#Gameover text
NeW = my_font.render("New Game", True, GREEN)#New game text
N = 5#number of coins
score = 0#score number
coins = 0#coins weight summ number
over = 0#gameover flag
class Coin():#coin object class
    def __init__(self,x):
        self.y = 0#coins will move to us so we dont need other coins y 
        self.x = x#coins x that will be randomly setted
        self.im = pg.image.load("C:\\Users\\User\\Desktop\\Программирование\\my\\pp2-22B030391\\tsis8\\2\\Coin.png")#loading coin image
        self.rect = self.im.get_rect()#getting rect of coin image(x,y,width,height)
        self.w, self.h = self.rect[2], self.rect[3]
        self.dy = 10#default speed of coin
        self.weight = 1#default weight of coin
    def reset(self):#reseting coin ,used when coin collided with player or enemy
        self.y = -self.h#put coin at start with shift out of border by coins height
        self.x = random.randint(0,W-self.w)#randomly setted coins x
        self.weight = random.randint(0,10)#random weight of coin when resetted
    def move(self):
        self.y += self.dy#moving coin to us(down)
        if self.y > H:#if coin flew away it will be teleported to start
            self.y = -self.h
            self.x = random.randint(0,W-self.w)#with randomized x
    def chcoll(self,enemy):#function of checking collision with player or enemy
        if enemy.x -self.w <= self.x <= enemy.x + enemy.w  and  enemy.y -self.h <= self.y <= enemy.y + enemy.h:#same as how i did button check
            self.y = -self.h
            self.x = random.randint(0,W-self.w)# x random number in interval from 0 to W - coins width because else it will appear without its part at border or out of border(screen)
            return True
        return False
    def draw(self,scr):
        self.im.set_colorkey((255,255,255))#using this will make white pixels in image "invisible" on screen
        scr.blit(self.im,(self.x,self.y))# bliting image on screen
class Enemy():#Enemy class
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.im = pg.image.load("C:\\Users\\User\\Desktop\\Программирование\\my\\pp2-22B030391\\tsis8\\2\\Enemy.png")#enemy  image loading
        self.rect = self.im.get_rect()#same things as with coin
        self.w, self.h = self.rect[2], self.rect[3]
        self.dy = 10
    def move(self):
        self.y += self.dy
        global score
        if self.y > H:
            score += 1#when enemy crossing border score increase 
            self.y = -self.h#teleporting enemy to start same as with coin
            self.x = random.randint(0,W-self.w)
            self.dy += 1
    def draw(self,scr):#enemy draw same as with coin
        self.im.set_colorkey((0,0,0))
        scr.blit(self.im,(self.x,self.y))
class Player():#Player class 
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.im = pg.image.load("C:\\Users\\User\\Desktop\\Программирование\\my\\pp2-22B030391\\tsis8\\2\\Player.png")
        self.rect = self.im.get_rect()
        self.w, self.h = self.rect[2], self.rect[3]
        
    def move(self,dx):#to move player we need only x and dx
        key = pg.key.get_pressed()
        if key[pg.K_LEFT] and self.x>0:# if Player pressed left/right button players x will decrease/increase by its speed dx and this limited with 0 and W - coins width if it will be limited with 0 and W when player will be near with border player will see part of his  body
            self.x -= dx 
        if key[pg.K_RIGHT] and self.x<W - self.w - 10:
            self.x += dx
    def chcoll(self,enemy):#function of checking colliding player with enemy with same method as with coin 
        if enemy.x -self.w <= self.x <= enemy.x + enemy.w  and  enemy.y -self.h <= self.y <= enemy.y + enemy.h:
            return True
        return False
    def draw(self,scr):#player draw....
        self.im.set_colorkey((0,0,0))
        scr.blit(self.im,(self.x,self.y))
def main():
    cl = 0# NEW GAME buttom flag
    nn = 0#number of coins
    global score 
    global coins
    run = True#running flag
    coin = Coin(W//2)#coin,enemy,player creating
    enemy = Enemy(W//2,0)
    player = Player(W//2,H - 120)   
    dx = 15# speed of player
    global over
    while run:# game loop
        mouse = pg.mouse.get_pos()#mouse position getting when game is not over and over
        for event in pg.event.get():# events ...
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN and over == 1:# check we pressed NEW GAME BUTTON? yes cl = 1 no cl = 0
                if (W//2 <= mouse[0] <= W//2 + 200) and (H//2 + 50<= mouse[1] <= H//2 + 100):
                    cl = 1
        if cl == 1:#resetting start data
            score = 0
            coins = 0
            enemy.dy = 10
            enemy.y = -enemy.h
            player.x = W//2
            nn = 0
            over = 0#starting new game
        if over == 0:#if game not over
            if coins == N or nn == N:
                enemy.dy += 5
            cl = 0
            tscore = my_font.render("Score: "+str(score), True, BLACK)
            tcoins = my_font.render("Coins: "+str(coins), True, BLACK)
            if player.chcoll(enemy):#check collision of player with enemy
                over = 1 # if player collided with enemy game is over
            if coin.chcoll(player):#check collision of coin with player
                nn += 1# counting coins
                coins += coin.weight
                coin.reset()#reset coins weight randomly as coin collided with player
            if coin.chcoll(enemy):#check collision of coin with enemy
                coin.reset()
            scr.blit(Bg, (0,0)) 
            player.move(dx)#draw objects
            player.draw(scr)
            enemy.move()
            coin.move()
            enemy.draw(scr)
            coin.draw(scr)
            scr.blit(tscore, (W-130,10)) #draw coins and score
            scr.blit(tcoins, (10,10)) 
        elif over == 1:#if over then show game over scene with NEW GAME button
            scr.fill(BLACK)
            scr.blit(game_over, (W//2,H//2)) 
            scr.blit(NeW, (W//2,H//2 + 50))
        
        pg.display.flip()#updating screen
        clock.tick(fps)#game loop time tick 


if __name__ == '__main__':
    main()
