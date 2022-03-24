import pygame

from constants import *
from helpers import screen


class Brick:
    def __init__(self, brick_color, brick_width, brick_height, x_pos, y_pos):
        self.brick_color = brick_color
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.x_pos = x_pos
        self.y_pos = y_pos


    def create_brick(self):
        if(self.brick_color=="yellow"):
            img = pygame.image.load(Images/yellow_brick.jpg)
            self.image = pygame.transform.scale(img, (self.brick_width, self.brick_height))



