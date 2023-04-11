import random#importing libs
import pygame

pygame.init() # инициализация библиотеки pygame 
eatf = pygame.mixer.Sound('C:\\Users\\User\\Desktop\\Программирование\\my\\pp2-22B030391\\tsis8\\1\\11.wav')#loading sound
from data1 import *#loading data RGB COLORS Screen size etc from other python file
clock = pygame.time.Clock() # создание зарержки в игре те времени
my_font = pygame.font.SysFont('Comic Sans MS', 30) # для текста
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))#screen setting

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:#Snake class
    def __init__(self):
        self.body = [# snakes start body
            Point(
                x=WIDTH // BLOCK_SIZE // 2,#head
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
            Point(
                x=WIDTH // BLOCK_SIZE // 2 + 1,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
        ]

    def draw(self):#draw method of snake
        head = self.body[0]
        pygame.draw.rect(#drawing head, draw rectangle on screen that sized with BLOCK_SIZE that in data
            SCREEN,
            RGR,#dark Green head
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        for body in self.body[1:]:#drawing tail ,all body objects without head on screen with same method as we draw head but in for loop of body 
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )

    def move(self, dx, dy):#move method of snake
        for idx in range(len(self.body) - 1, 0, -1): #moving snake from the last part of body(not head)
            self.body[idx].x = self.body[idx - 1].x 
            self.body[idx].y = self.body[idx - 1].y

        self.body[0].x += dx#moving head
        self.body[0].y += dy
        #teleport snake to other side when it crossing border
        if self.body[0].x >= WIDTH // BLOCK_SIZE:
            self.body[0].x = 0 
       
        elif self.body[0].x < 0:
            self.body[0].x = WIDTH // BLOCK_SIZE
        
        elif self.body[0].y < 0:
            self.body[0].y = WIDTH // BLOCK_SIZE
        
        elif self.body[0].y >= HEIGHT // BLOCK_SIZE:
            self.body[0].y = 0 

    def check_collision(self, food):#function of checking collision with food
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True
    def check_selfcol(self):#function of checking collision with self body
        for i in range(len(self.body) - 1, 1, -1):
            if self.body[i].x == self.body[0].x and self.body[i].y == self.body[0].y:
                return True
        return False

def draw_grid():#function of gird drawing on screen with white lines that drawn multiple times with for loop ,that will make gird with block size BLOCK_SIZE
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(x, 0), end_pos=(x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(0, y), end_pos=(WIDTH, y), width=1)

class Food:#food class
    def __init__(self, x, y):
        self.location = Point(x, y)
        self.weight = 1
    def draw(self):#draw method of food
        pygame.draw.rect(#drawing green rect on screen with block size
            SCREEN,
            GREEN,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
    def relocate(self):#relocate that will respawn food to other random position in screen with random weight , that also used to avoid food spawn on snake body
        self.weight = random.randint(1, 10)
        self.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)   
        self.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1) 

def main():
    running = True #running flag
    snake = Snake()  # создание змеи
    food = Food(5, 5)  # создание еды
    dx, dy = 0, 0;T = 5 # начальные данные в игре
    score = 0 ;level = 0
    Ug = 1 ;Rg = 1# moving limit flags that will avoid game over caused  by example if you just moving up and then down 
    over = 0 ;cl = 0# gameover flag and New game button flag
    dt = clock.tick();t = 0; #food timer 
    while running:#game loop
        SCREEN.fill(BLACK)
        mouse = pygame.mouse.get_pos()#
        for i in snake.body:#if foon spawned on snake respawn it
            if i.x == food.location.x and i.y == food.location.y:
                food.relocate()
        for event in pygame.event.get(): # обработка событии
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and over == 1:#NEW Game button check
                if (WIDTH//2 -100 <= mouse[0] <= WIDTH//2 + 100) and (HEIGHT//2 <= mouse[1] <= HEIGHT//2 + 100):
                    cl = 1
            if event.type == pygame.KEYDOWN:  # изменение скорости при нажатии на кнопки
                if event.key == pygame.K_UP and Rg == 1 :#я добавил Rg Ug для того чтобы когда ты к примеру идешь в перед потом назад то ты не сталкивался сам с собой и дальше двигался в перед
                    dx, dy = 0, -1
                    Ug = 1
                    Rg = 0
                elif event.key == pygame.K_DOWN and Rg == 1 :
                    dx, dy = 0, +1
                    Ug = 1
                    Rg = 0
                elif event.key == pygame.K_RIGHT and Ug == 1:
                    dx, dy = 1, 0
                    Rg = 1
                    Ug = 0
                elif event.key == pygame.K_LEFT and Ug == 1:
                    dx, dy = -1, 0
                    Rg = 1
                    Ug = 0
        if over == 0:
            t += dt#time running
            if t >= 3000:
                food.relocate()#перемещаем еду если время прошло
                t = 0 #обнуляем таймер
        if cl == 1:#if button NEW GAME clicked reset game data to start
            dx, dy = 0, 0;T = 5
            score = 0;level = 0
            Ug = 1;Rg = 1
            t = 0; 
            snake.body.clear()
            snake.body = [
            Point(
                x=WIDTH // BLOCK_SIZE // 2,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
            Point(
                x=WIDTH // BLOCK_SIZE // 2 + 1,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
            ]
            over = 0#startting new game
        if over == 0: #if game is not over
            cl = 0
            snake.move(dx, dy)  # вызов функции движения змеи
            if snake.check_collision(food):  # функция столкновения с едой
                pygame.mixer.Sound.play(eatf)#play sound when food collided with snake
                score += food.weight 
                level = score//3
                if level>(score-food.weight)//3:#if level increased increase speed of snake and length of snake
                    dl = int(level-((score-food.weight)//3))
                    T += 1*dl#increasing speed of snake(game)
                    for i in range(dl):
                        if len(snake.body)<maxl - 2: #max length of snake limited by maxl
                            snake.body.append(      
                            Point(snake.body[-1].x, snake.body[-1].y)  # удлиннение змеи 
                            ) 
                food.relocate()#food respawn if it collided with snake
                t = 0 #restart timer
                
            if snake.check_selfcol():  
                over = 1
            snake.draw()# вывод функции для отрисовки змеи
            food.draw() # вывод функции для отрисовки еды
            draw_grid() # вывод функции для отрисовки фона
            
            text_score = my_font.render('Score :'+str(score), False, (0, 255, 0))
            SCREEN.blit(text_score, (20,20)) #вывод на экран очков
            text_level = my_font.render('Level :'+str(level), False, (0, 255, 0))
            SCREEN.blit(text_level, (WIDTH - 300,20))# вывод на экран уровня     
        elif over == 1:
            text_over = my_font.render('Game Over', False, (250, 0, 0))
            SCREEN.blit(text_over, (WIDTH//2 -100,HEIGHT//2 -100)) #вывод на экран очков
            text_over = my_font.render('New Game', False, (250, 250, 0))
            SCREEN.blit(text_over, (WIDTH//2 -100,HEIGHT//2)) #вывод на экран очков
        pygame.display.flip() # обновление экрана
        clock.tick(T)  # управление временем через Т


if __name__ == '__main__':
    main()
