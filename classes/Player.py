from classes import Brick
import pygame

from constants import *


class Player(Brick):
    def __init__(self, brick_color, brick_width, brick_height, x_pos, y_pos):
        super().__init__(self, brick_color, brick_width, brick_height, x_pos, y_pos)
        self.x_pos = LAUNCH_X_POS
        self.y_pos = LAUNCH_Y_POS
        self.points = 0

    def move_left(self):
        if (self.x_pos - BRICK_MOVEMENT < 0 or self.x_pos + BRICK_WIDTH > WINDOW_WIDTH or
                self.y_pos < 0 or self.y_pos + BRICK_WIDTH > WINDOW_WIDTH):
            return False
        self.x_pos = self.x_pos - BRICK_MOVEMENT

    def move_right(self):
        if (self.x_pos < 0 or self.x_pos + BRICK_WIDTH + BRICK_MOVEMENT > WINDOW_WIDTH or
                self.y_pos < 0 or self.y_pos + BRICK_WIDTH > WINDOW_WIDTH):
            return False
        self.y_pos = self.y_pos + BRICK_MOVEMENT
