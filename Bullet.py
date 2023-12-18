import pygame as pg


class Bullet:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 50 * facing

    def render(self, sc):
        pg.draw.circle(sc, self.color, (self.x, self.y), self.radius)
