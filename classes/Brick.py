import pygame
from helpers import*
from constants import *

# Creates all the relevant fields regarding class "Brick".
class Brick:
    def __init__(self, brick_color, brick_width, brick_height, x_pos, y_pos):
        self.brick_color = brick_color
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = self.create_brick()

# Organizes the brick pictures (can be found in Images)
    # in order for the bricks to fit the screen in the correct order.

    def create_brick(self):
        if self.brick_color == "yellow":
            img = pygame.image.load("Images/yellow_brick.png")
        if self.brick_color == "red":
            img = pygame.image.load("Images/red_brick.png")
        if self.brick_color == "blue":
            img = pygame.image.load("Images/blue_brick.png")
        if self.brick_color == "green":
            img = pygame.image.load("Images/green_brick.png")
        if self.brick_color == "purple":
            img = pygame.image.load("Images/purple_brick.png")
        return pygame.transform.scale(img, (self.brick_width, self.brick_height))

# Gets the x position of the brick.
    def get_x_pos(self):
        return self.x_pos

# Gets the y position of the brick.
    def get_y_pos(self):
        return self.y_pos

# Sets the x position of the brick.
    def set_x_pos(self, x):
        self.x_pos = x

# Sets the y position of the brick.
    def set_y_pos(self, y):
        self.y_pos = y

# Gets the brick's color.
    def get_brick_color(self):
        return self.brick_color

# Sets the brick color.
    def set_brick_color(self, new_color):
        self.brick_color = new_color

# Displays the brick on the screen.
    def display_brick(self):
        SCREEN.blit(self.image, (self.x_pos, self.y_pos))

# Goes over a matrix list, finds the required brick then removes said brick from the screen.
    def remove_brick(self, matrix_bricks, brick):
        for b in matrix_bricks:
            for f in brick:
                if brick == f:
                    matrix_bricks.remove(brick)
