import pygame#importing libs
import os
import math
import numpy  as np
from DATA import *#importing some data from DATA file
pygame.init()#pygame methods functions initialization
pygame.display.set_caption("PainT_Ilyasa")# name progr
font = pygame.font.SysFont('Verdana', 11)#text style for buttons 
font1 = pygame.font.SysFont('Verdana', 20)#text stylw for text that used in opening file and saving
scr = pygame.display.set_mode((WIDTH,HEIGHT))#screen creating
canv = pygame.Surface((WIDTH,HEIGHT-70)).convert_alpha()#creating sub surface that on scr , where we can draw
scanv = pygame.Surface((500,200))#sub surface on scr , we will use it for open/save 
clock = pygame.time.Clock()# time creating
run = True # game loop flag
k = 2*(3**0.5)/3
b1t = font.render("PEN", True, WHITE)# Button texts
b2t = font.render("RECT", True, WHITE)
b3t = font.render("CIRC", True, WHITE)
b6t = font.render("SAVE", True, WHITE)
b7t = font.render("OPEN", True, WHITE)
b8t = font.render("CLOSE", True, WHITE)
b9t = font.render("PTNGL", True, WHITE)
b10t = font.render("ERASE", True, BLACK)
b11t = font.render("LINE", True, BLACK)
b12t = font.render("SQUAR", True, BLACK)
b13t = font.render("RTRIN", True, BLACK)
b14t =  font.render("RHMB", True, BLACK)
class Button:
    def __init__(self,x,y,wid,hei,col,text = "1"):
        self.x = x
        self.y = y
        self.color = col
        self.wid = wid
        self.hei = hei
        self.text = text
        self.rect = pygame.Rect(self.x,self.y,self.wid,self.hei)# need to chec collision with cursor
    def draw(self):
        pygame.draw.rect(scr,
                         self.color,
                         (self.x,self.y,self.wid,self.hei),
                         10
                         )# drawing colored rect
        pygame.draw.rect(scr,
                         WHITE,
                         (self.x,self.y,self.wid,self.hei),
                         1
                         )#drawing border
        if self.text != "1":#if button with text
            scr.blit(self.text, (self.x,self.y - 2))#blit button with text
class GameObject:# gameobj used to change active obj without None
    def draw(self):
        return
    def update(self,width,color,current_pos):
        return
class Pen(GameObject):
    def __init__(self, *args, **kwargs): #for pen we need points , color , width
        self.points = []
        self.color = RED
        self.width = 1 
    def draw(self):
        for idx, point in enumerate(self.points[:-1]):  # range(len(self.points))
            next_point = self.points[idx + 1]
            pygame.draw.line(
                canv,
                self.color,
                (point[0], point[1]), 
                (next_point[0], next_point[1]),
                self.width
            )
    def update(self,width,color,current_pos):#updating color width and points of object (when moving)
        self.points.append(current_pos)
        self.color = color
        self.width = width
class Rectangle(GameObject):#for rect we need just two  points (start and end points) ,color ,width
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_posx, self.start_posy  = start_pos
        self.end_posx, self.end_posy = start_pos 
        self.color = RED
        self.width = 1 
    def draw(self):
        start_pos_x = min(self.start_posx, self.end_posx)  
        start_pos_y = min(self.start_posy, self.end_posy) # finding the nearest point of rect
        end_pos_x = max(self.start_posx, self.end_posx) 
        end_pos_y = max(self.start_posy, self.end_posy)# finding the furthest point of rect
        pygame.draw.rect(
            canv,
            self.color,
            (
                start_pos_x, start_pos_y,#start 
                end_pos_x - start_pos_x,#width of rect
                end_pos_y - start_pos_y,#height of rect
            ),
            self.width,
        )

    def update(self,width,color,current_pos):# same as pen update
        self.end_posx, self.end_posy = current_pos#end point is current position of mouse
        self.color = color
        self.width = width
class Square(GameObject):#for square we need just two  points (start and end points) ,color ,width
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_posx, self.start_posy  = start_pos
        self.end_posx, self.end_posy = start_pos 
        self.color = RED
        self.width = 1 
    def draw(self):
        start_pos_x = min(self.start_posx, self.end_posx)  
        start_pos_y = min(self.start_posy, self.end_posy) # finding the nearest point of rect
        end_pos_x = max(self.start_posx, self.end_posx) 
        end_pos_y = max(self.start_posy, self.end_posy)# finding the furthest point of rect
        pygame.draw.rect(
            canv,
            self.color,
            (
                start_pos_x, start_pos_y,#start 
                end_pos_x - start_pos_x,#width of rect
                end_pos_x - start_pos_x,#height of rect
            )
        )

    def update(self,width,color,current_pos):# same as pen update
        self.end_posx, self.end_posy = current_pos#end point is current position of mouse
        self.color = color
        self.width = width
class Circle(GameObject):
    def __init__(self, start_pos, *args, **kwargs):#for circle we need just two points (start and end points) ,color ,width
        self.start_posx, self.start_posy = start_pos
        self.end_posx, self.end_posy = start_pos
        self.color = RED
        self.width = 1 
    def draw(self):
        r = ((self.end_posx-self.start_posx)**2+(self.end_posy-self.start_posy)**2)**0.5#finding radius of circle
        pygame.draw.circle(
            canv,
            self.color,
            (self.start_posx,self.start_posy),
            r,
            self.width
        )

    def update(self,width,color,current_pos):#same as others upd
        self.end_posx, self.end_posy = current_pos #end point is current position of mouse
        self.color = color
        self.width = width
class Triag(GameObject):#perfect or equilateral triangle
    def __init__(self, start_pos, *args, **kwargs):#for circle we need just two points (start and end points) ,color ,width
        self.start_posx, self.start_posy = start_pos
        self.end_posx, self.end_posy = start_pos
        self.color = BLACK
        self.width = 1 
    def draw(self):
        d = ((self.end_posx-self.start_posx)**2 + (self.end_posy-self.start_posy)**2)**0.5
        dx,dy = self.end_posx-self.start_posx,self.end_posy-self.start_posy
        a = math.atan2(dx,dy)#
        y2 = self.start_posy - k*d*np.sin(a-(np.pi/3))     
        x2 = self.start_posx + (self.start_posy - y2)/(np.tan(-(np.pi/3)+a))
        y3 = self.start_posy + k*d*np.sin(a+(np.pi/3)) 
        x3 = self.start_posx + (self.start_posy - y3)/(np.tan(+(np.pi/3)+a))
        #pygame.draw.line(canv, self.color,(self.start_posx, self.start_posy),(self.end_posx, self.end_posy),self.width)
        pygame.draw.line(canv, self.color,(self.end_posx, self.end_posy),(x2,y2),self.width)
        pygame.draw.line(canv, self.color,(self.start_posx, self.start_posy),(x2,y2),self.width)
        pygame.draw.line(canv, self.color,(self.start_posx, self.start_posy),(x3,y3),self.width)
        pygame.draw.line(canv, self.color,(x2,y2),(x3,y3),self.width)
    def update(self,width,color,current_pos):#same as others upd
        self.end_posx, self.end_posy = current_pos #end point is current position of mouse
        self.color = color
        self.width = width
class RTriag(GameObject):
    def __init__(self, start_pos, *args, **kwargs):#Right triangle
        self.start_posx, self.start_posy = start_pos
        self.end_posx, self.end_posy = start_pos
        self.color = BLACK
        self.width = 1 
    def draw(self):
        d = ((self.end_posx-self.start_posx)**2 + (self.end_posy-self.start_posy)**2)**0.5
        dx,dy = self.end_posx-self.start_posx,self.end_posy-self.start_posy
        a = math.atan2(dx,dy)#
        y2 = self.start_posy - k*d*np.sin(a-(np.pi/3))     
        x2 = self.start_posx + (self.start_posy - y2)/(np.tan(-(np.pi/3)+a))
        y3 = self.start_posy + k*d*np.sin(a+(np.pi/3)) 
        x3 = self.start_posx + (self.start_posy - y3)/(np.tan(+(np.pi/3)+a))
        pygame.draw.line(canv, self.color,(self.start_posx, self.start_posy),(self.end_posx, self.end_posy),self.width)
        pygame.draw.line(canv, self.color,(self.end_posx, self.end_posy),(x2,y2),self.width)
        pygame.draw.line(canv, self.color,(self.start_posx, self.start_posy),(x2,y2),self.width)
    def update(self,width,color,current_pos):#same as others upd
        self.end_posx, self.end_posy = current_pos #end point is current position of mouse
        self.color = color
        self.width = width
class Line(GameObject):
    def __init__(self, start_pos, *args, **kwargs):#for line we need just two points (start and end points) ,color ,width
        self.start_posx, self.start_posy = start_pos
        self.end_posx, self.end_posy = start_pos
        self.color = BLACK
        self.width = 1 
    def draw(self):
        pygame.draw.line(canv, self.color,(self.start_posx, self.start_posy),(self.end_posx, self.end_posy),self.width)
    def update(self,width,color,current_pos):#same as others upd
        self.end_posx, self.end_posy = current_pos #end point is current position of mouse
        self.color = color
        self.width = width
class Erase(GameObject):
    def __init__(self, *args, **kwargs): 
        self.points = []
        self.color = WHITE
        self.width = 10 
    def draw(self):
        for idx, point in enumerate(self.points[:-1]):  # range(len(self.points))
            next_point = self.points[idx + 1]
            pygame.draw.line(
                canv,
                WHITE,
                (point[0], point[1]), 
                (next_point[0], next_point[1]),
                self.width
            )
    def update(self,width,color,current_pos):#updating color width and points of object (when moving)
        self.points.append(current_pos)
        self.color = color
        self.width = width
class Rhomb(GameObject):
    def __init__(self, start_pos, *args, **kwargs): 
        self.start_posx, self.start_posy  = start_pos
        self.end_posx, self.end_posy = start_pos 
        self.color = RED
        self.width = 1 
    def draw(self):
        d = ((self.end_posx-self.start_posx)**2 + (self.end_posy-self.start_posy)**2)**0.5
        dx,dy = self.end_posx-self.start_posx,self.end_posy-self.start_posy
        a = math.atan2(dx,dy)#
        y2 = self.start_posy - k*d*np.sin(a-(np.pi/3))     
        x2 = self.start_posx + (self.start_posy - y2)/(np.tan(-(np.pi/3)+a))
        y3 = self.start_posy + k*d*np.sin(a+(np.pi/3)) 
        x3 = self.start_posx + (self.start_posy - y3)/(np.tan(+(np.pi/3)+a))
        pygame.draw.line(canv, self.color,(x2,y2),(2*self.end_posx-self.start_posx,2*self.end_posy-self.start_posy),self.width)
        pygame.draw.line(canv, self.color,(x3,y3),(2*self.end_posx-self.start_posx,2*self.end_posy-self.start_posy),self.width)
        pygame.draw.line(canv, self.color,(self.start_posx, self.start_posy),(x2,y2),self.width)
        pygame.draw.line(canv, self.color,(self.start_posx, self.start_posy),(x3,y3),self.width)
        
    def update(self,width,color,current_pos):# same as others update
        self.end_posx, self.end_posy = current_pos#end point is current position of mouse
        self.color = color
        self.width = width
#loading and saving flags
load = False
save = False
i = 0
j = 0
#buttons creating
b16 = Button(240,20,37,10,DARKGRN,b6t)
b17 = Button(240,35,37,10,DARKGRN,b7t)
b18 = Button(240,50,37,10,RED,b8t)
b19 = Button(140,20,37,10,DARKGRN,b9t)
b20 = Button(140,35,37,10,WHITE,b10t)
b21 = Button(140,50,37,10,DARKGRN,b11t)
b22 = Button(180,20,37,10,DARKGRN,b12t)
b23 = Button(180,35,37,10,DARKGRN,b13t)
b24 = Button(180,50,37,10,DARKGRN,b14t)
b1 = Button(20,20,27,10,DARKGRN,b1t)
b2 = Button(20,50,27,10,DARKGRN,b2t)
b3 = Button(20,35,27,10,DARKGRN,b3t)

b4 = Button(60,20,27,10,RED)# color buttons
b5 = Button(60,35,27,10,ORANGE)
b6 = Button(60,50,27,10,YELLOW)

b7 = Button(100,20,27,10,GREEN)
b8 = Button(100,35,27,10,BBLUE)
b9 = Button(100,50,27,10,BLUE)

drawload = False
filename = ""
file_dir = "C:\\Users\\User\\Desktop\\Программирование\\my\\pp2-22B030391\\tsis9\\3\\Images"
files_list = os.listdir(file_dir)#list of files in Images 
widt = 1#standart width and color
colo = RED

game_object = GameObject()
active_obj = game_object
current_shape = Pen  # current_shape()
objects = []#objects that will be drawn

while run:#game loop
    scr.fill(BLACK)
    scr.blit(canv,(0,70))   
    canv.fill(WHITE)
    if drawload:#drawing loaded image
        canv.blit(imag, (0,0)) 
    scanv.fill(GREY)
    if save:
        tx = 50
        ty = (scanv.get_height()//2) - 15
        tw = 400
        tt = font1.render("Сохранить как", True, (255, 0, 0))
        ts = font1.render(filename, True, (255, 0, 0))
        th = ts.get_height() +10
        pygame.draw.rect(scanv,
                         BLACK,
                         (tx,ty,tw,th),
                         1
                         )
        scanv.blit(ts, ts.get_rect(center = scanv.get_rect().center)) 
        scanv.blit(tt, (40 , 34))  
        scr.blit(scanv,(200,200))

    elif load:  
        tx = 50
        ty = (scanv.get_height()//2) - 15
        tw = 400
        tt = font1.render("Введите название файла без формата", True, (255, 0, 0))
        ts = font1.render(filename, True, (255, 0, 0))
        th = ts.get_height() +10
        pygame.draw.rect(scanv,
                         BLACK,
                         (tx,ty,tw,th),
                         1
                         )
        scanv.blit(ts, ts.get_rect(center = scanv.get_rect().center)) 
        scanv.blit(tt, (40 , 34))  
        scr.blit(scanv,(200,200))
    b1.draw()#drawing all buttons on screen
    b2.draw()
    b3.draw()
    b4.draw()
    b5.draw()
    b6.draw()
    b7.draw()
    b8.draw()
    b9.draw()
    b16.draw()
    b17.draw()
    b18.draw()
    b19.draw()
    b20.draw()
    b21.draw()
    b22.draw()
    b23.draw()
    b24.draw()
    for event in pygame.event.get(): #events checking
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if b18.rect.collidepoint(event.pos):#close button 
                run = False
            if b1.rect.collidepoint(event.pos):#Changing cur shape when buttons pressed
                current_shape = Pen
            if b2.rect.collidepoint(event.pos):
                current_shape = Rectangle
            if b3.rect.collidepoint(event.pos):
                current_shape = Circle
            if b19.rect.collidepoint(event.pos):
                current_shape = Triag#Ptrd
            if b21.rect.collidepoint(event.pos):
                current_shape = Line
            if b20.rect.collidepoint(event.pos):
                current_shape = Erase
            if b22.rect.collidepoint(event.pos):
                current_shape = Square
            if b23.rect.collidepoint(event.pos):
                current_shape = RTriag
            if b24.rect.collidepoint(event.pos):
                current_shape = Rhomb
            if b16.rect.collidepoint(event.pos):# if save button pressed
                save = True #starting save
            if b17.rect.collidepoint(event.pos):# if open button pressed
                load = True #starting load
            if b4.rect.collidepoint(event.pos):# color change if color button pressed
                colo = RED
            if b5.rect.collidepoint(event.pos):
                colo = ORANGE
            if b6.rect.collidepoint(event.pos):
                colo = YELLOW
            if b7.rect.collidepoint(event.pos):
                colo = GREEN
            if b8.rect.collidepoint(event.pos):
                colo = BBLUE
            if b9.rect.collidepoint(event.pos):
                colo = BLUE
        
            
            else:# if you drawing on canvas (not pressing buttons)
                active_obj = current_shape(start_pos=(event.pos[0],event.pos[1]-70))#taking start pos for object 
                objects.append(active_obj)#creating new object when you pressed mouse button
        if event.type == pygame.MOUSEMOTION:
            if widt <= 0:
                widt = 1
            curp = (event.pos[0],event.pos[1]-70)#taking current position of mouse
            active_obj.update(widt,colo,curp)
        if event.type == pygame.MOUSEBUTTONUP:# clear active object
            active_obj = game_object
        if event.type == pygame.KEYDOWN and (load or save):#for load/save
                if event.key == pygame.K_RETURN:
                    if load and not save:
                        i = 1 
                    elif save and not load:
                        j = 1
                    load = False
                    save = False
                elif event.key == pygame.K_BACKSPACE:#if BACKSPACE we shift text 
                    filename =  filename[:-1]
                else:
                    filename += event.unicode# else we input text
        elif event.type == pygame.MOUSEWHEEL:# increase/decrease width of tool when mouse wheel scrolled 
                widt += event.y   
    for obj in objects:#drawing all created objects 
        obj.draw()
    if i == 1:
        try:
            objects = []#clear image that was before
            imag = pygame.image.load("C:\\Users\\User\\Desktop\\Программирование\\my\\pp2-22B030391\\tsis9\\3\\Images\\"+str(filename)+".png")
            drawload = True
        except FileNotFoundError: 
            drawload = False  
        i = 0# closing "opening" surface
    if j == 1:#same for "saving"
        pygame.image.save(canv, "C:\\Users\\User\\Desktop\\Программирование\\my\\pp2-22B030391\\tsis9\\3\\Images\\"+str(filename)+".png")
        j = 0  
    clock.tick(FPS)#set time 
    pygame.display.flip()#updating all screen
pygame.quit()#quit from program if game loop stopped