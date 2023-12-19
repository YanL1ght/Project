import pygame as pg


class Bullet:  # класс пули
    def __init__(self, x, y, radius, color, facing):  # создание пули по введённым параметрам
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 50 * facing

    def render(self, sc):  # отрисовка пули
        pg.draw.circle(sc, self.color, (self.x, self.y), self.radius)
        
