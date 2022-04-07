from classes.Brick import *
from helpers import *
import pygame
import time
import random
from constants import *


class Player(Brick):
    def __init__(self, brick_color, brick_width, brick_height, x_pos, y_pos):
        super().__init__(brick_color, brick_width, brick_height, x_pos, y_pos)
        self.points = 0

    def move_left(self):
        if not (self.x_pos - BRICK_MOVEMENT < 0 or self.x_pos + BRICK_WIDTH > WINDOW_WIDTH or
                self.y_pos < 0 or self.y_pos + BRICK_HEIGHT > WINDOW_HEIGHT):
            self.x_pos -= BRICK_MOVEMENT

    def move_right(self):
        if not (self.x_pos < 0 or self.x_pos + BRICK_WIDTH + BRICK_MOVEMENT > WINDOW_WIDTH or
                self.y_pos < 0 or self.y_pos + BRICK_HEIGHT > WINDOW_HEIGHT):
            self.x_pos += BRICK_MOVEMENT

    def launch(self):
        if not self.y_pos < 0:
            self.y_pos -= BRICK_MOVEMENT

    def touch_same_brick(self, brick_list):
        disappear_list = []
        for brick in brick_list:
            if self.y_pos <= brick.get_y_pos() + BRICK_HEIGHT and brick.get_x_pos() <= self.x_pos <= brick.get_x_pos() + BRICK_WIDTH:
                if self.get_brick_color() == brick.get_brick_color():
                    disappear_list.append(brick)
                    self.points += POINT
                else:
                    create_replacement(self)
                    reset_player(self)
