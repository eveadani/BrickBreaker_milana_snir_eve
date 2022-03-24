from classes import Brick
import pygame

from constants import *
from helpers import screen


class Player(Brick):
    def __init__(self, brick_color, brick_width, brick_height, x_pos, y_pos):
        Brick.__init__(self, brick_color, brick_width, brick_height, x_pos, y_pos)
        self.points = 0

