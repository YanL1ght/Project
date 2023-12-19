import pygame as pg
from Bullet import Bullet
# import Entity


class Player:  # класс Игрока
    def __init__(self, x=500, y=500):  # инициализация класса
        self.pos_x = x
        self.pos_y = y
        self.width = 50
        self.height = 100

        self.body = None
        self.isJump = False
        self.jumpCount = 20
        self.bullets = []
        self.facing = 1
        self.speed = 1

    def render(self):  # отрисовка персонажа и пуль
        pg.draw.rect(sc, pg.Color('white'), (self.pos_x, self.pos_y, self.width, self.height))

        for bullet in self.bullets:
            if 0 < bullet.x < win_size[0]:
                bullet.x += bullet.vel
                bullet.render(sc)
            else:
                self.bullets.pop(self.bullets.index(bullet))

    def move(self, x=10):  # движение персонажа
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.pos_x -= x * self.speed
            self.facing = -1
        elif keys[pg.K_d]:
            self.pos_x += x * self.speed
            self.facing = 1

    def jump(self):  # прыжок персонажа
        if self.isJump:
            if self.jumpCount >= -20:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.pos_y -= self.jumpCount ** 2 * 0.1 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 20

    def shot(self):  # выстрел персонажа
        self.bullets.append(Bullet(self.pos_x, self.pos_y + (self.height // 2), 10, (255, 0, 0), self.facing))

    def lunge(self, x=300):  # одна из механик игры, выпад
        self.pos_x += x * self.facing


if __name__ == '__main__':  # демонстрация работы класса
    pg.init()
    win_size = (1000, 900)
    sc = pg.display.set_mode(win_size)
    run = True
    player = Player()
    clock = pg.time.Clock()
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    player.isJump = True
                elif event.key == pg.K_f:
                    player.shot()
                elif event.key == pg.K_LSHIFT:
                    player.lunge()

        sc.fill((0, 0, 0))
        player.jump()
        player.move()
        player.render()
        pg.display.flip()
        clock.tick(30)
