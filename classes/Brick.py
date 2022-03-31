import pygame

from constants import *
from helpers import screen
import random

class Brick:
    def __init__(self, brick_color, brick_width, brick_height, x_pos, y_pos):
        self.brick_color = brick_color
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = self.create_brick()

    def create_brick(self):
        if self.brick_color == "yellow":
            img = pygame.image.load("Images/yellow_brick.jpg")
        if self.brick_color == "red":
            img = pygame.image.load("Images/red_brick.jpg")
        if self.brick_color == "blue":
            img = pygame.image.load("Images/blue_brick.jpg")
        if self.brick_color == "green":
            img = pygame.image.load("Images/green_brick.jpg")
        if self.brick_color == "purple":
            img = pygame.image.load("Images/purple_brick.jpg")
        return pygame.transform.scale(img, (self.brick_width, self.brick_height))

    def display_brick(self):
        screen.blit(self.image, (self.x_pos, self.y_pos))




