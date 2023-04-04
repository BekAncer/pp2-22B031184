import pygame
import random

pygame.init()
Bg = pygame.image.load("Bg.png")
Br = Bg.get_rect()
Bw, Bh = Br[2], Br[3]
W = Bw
H = Bh
fps = 30
WHITE = ((255, 255, 255))
RED = ((255, 0, 0))
GREEN = ((0, 255, 0))
BLACK = ((0, 0, 0))
scr = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
my_font = pygame.font.SysFont('Verdana', 20)
game_over = my_font.render("Game Over", True, RED)
NeW = my_font.render("New Game", True, GREEN)
score = 0
coins = 0
over = 0


class Coin():
    def __init__(self, x):
        self.y = 0
        self.x = x
        self.im = pygame.image.load("Coin.png")
        self.rect = self.im.get_rect()
        self.w, self.h = self.rect[2], self.rect[3]
        self.dy = 10

    def reset(self):
        self.y = -self.h
        self.x = random.randint(0, W - self.w)

    def move(self):
        self.y += self.dy
        if self.y > H:
            self.y = -self.h
            self.x = random.randint(0, W - self.w)

    def chcoll(self, enemy):
        if enemy.x - self.w <= self.x <= enemy.x + enemy.w and enemy.y - self.h <= self.y <= enemy.y + enemy.h:
            self.y = -self.h
            self.x = random.randint(0, W - self.w)
            return True

        return False

    def draw(self, scr):
        self.im.set_colorkey((255, 255, 255))
        scr.blit(self.im, (self.x, self.y))


class Enemy():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.im = pygame.image.load("Enemy.png")
        self.rect = self.im.get_rect()
        self.w, self.h = self.rect[2], self.rect[3]
        self.dy = 10

    def move(self):
        self.y += self.dy
        global score
        if self.y > H:
            score += 1
            self.y = -self.h
            self.x = random.randint(0, W - self.w)
            self.dy += 1

    def draw(self, scr):
        self.im.set_colorkey((0, 0, 0))
        scr.blit(self.im, (self.x, self.y))


class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.im = pygame.image.load("Player.png")
        self.rect = self.im.get_rect()
        self.w, self.h = self.rect[2], self.rect[3]

    def move(self, dx):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.x > 0:
            self.x -= dx
        if key[pygame.K_RIGHT] and self.x < W - self.w - 10:
            self.x += dx

    def chcoll(self, enemy):
        if enemy.x - self.w <= self.x <= enemy.x + enemy.w and enemy.y - self.h <= self.y <= enemy.y + enemy.h:
            return True
        return False

    def draw(self, scr):
        self.im.set_colorkey((0, 0, 0))
        scr.blit(self.im, (self.x, self.y))


def main():
    cl = 0
    global score
    global coins
    run = True
    coin = Coin(W // 2)
    enemy = Enemy(W // 2, 0)
    player = Player(W // 2, H - 120)
    dx = 15
    global over
    while run:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and over == 1:
                if (W // 2 <= mouse[0] <= W // 2 + 200) and (H // 2 - 30 <= mouse[1] <= H // 2 + 70):
                    cl = 1
        if cl == 1:
            score = 0
            coins = 0
            enemy.dy = 10
            enemy.y = -enemy.h
            player.x = W // 2
            over = 0
        if over == 0:
            cl = 0
            tscore = my_font.render("Score: " + str(score), True, GREEN)
            tcoins = my_font.render("Coins: " + str(coins), True, GREEN)
            if player.chcoll(enemy):
                over = 1
            if coin.chcoll(player):
                coins += 1
            if coin.chcoll(enemy):
                coin.reset()
            scr.blit(Bg, (0, 0))
            player.move(dx)
            player.draw(scr)
            enemy.move()
            coin.move()
            enemy.draw(scr)
            coin.draw(scr)
            scr.blit(tscore, (W - 130, 10))
            scr.blit(tcoins, (10, 10))
        elif over == 1:
            scr.fill(BLACK)
            scr.blit(game_over, (W // 2 - 40, H // 2 - 30))
            scr.blit(NeW, (W // 2 - 40, H // 2 + 20))

        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    main()
