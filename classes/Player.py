import helpers
from classes.Brick import *
import pygame
import time
import random
from constants import *


# Creates all the relevant fields and methods for the class "Player".
class Player(Brick):
    def __init__(self, brick_color, brick_width, brick_height, x_pos, y_pos):
        super().__init__(brick_color, brick_width, brick_height, x_pos, y_pos)
        self.points = 0

    # Creates an event key for the left button when the button is pressed.
    def move_left(self):
        if not (self.x_pos - BRICK_MOVEMENT < 0 or self.x_pos + BRICK_WIDTH > WINDOW_WIDTH or
                self.y_pos < 0 or self.y_pos + BRICK_HEIGHT > WINDOW_HEIGHT):
            self.x_pos -= BRICK_MOVEMENT

    # Creates an event key for the right button when the button is pressed.
    def move_right(self):
        if not (self.x_pos < 0 or self.x_pos + BRICK_WIDTH + BRICK_MOVEMENT > WINDOW_WIDTH or
                self.y_pos < 0 or self.y_pos + BRICK_HEIGHT > WINDOW_HEIGHT):
            self.x_pos += BRICK_MOVEMENT

    def loop_times(self, matrix_bricks):
        loops = 1
        rows = 0
        cols = 0
        for rows in range(len(matrix_bricks)):
            for cols in range(len(matrix_bricks[rows])):
                if matrix_bricks[rows][cols].get_x_pos() == self.x_pos:
                    loops = loops + 1
                    spec_row_brick = rows
                    spec_col_brick = cols
            cols += 1
        rows += 1

        loops = 10 - loops
        return loops, spec_row_brick, spec_col_brick

    # Checks if bricks of the same color come in contact with each other,
    # if so, said bricks will disappear from the screen.
    def touch_same_brick(self, matrix_bricks, spec_brick_row, spec_brick_col):
        disappear_list = []
        flag = True
        while flag:
            left = self.check_left(matrix_bricks, spec_brick_row, spec_brick_col)
            right = self.check_right(matrix_bricks, spec_brick_row, spec_brick_col)
            up = self.check_up(matrix_bricks, spec_brick_row, spec_brick_col)
            if left is None and right is None and up is None:
                flag = False
            if left is not None:
                disappear_list.append(left)
                self.touch_same_brick(matrix_bricks, spec_brick_row, spec_brick_col - 1)
            if right is not None:
                disappear_list.append(right)
                self.touch_same_brick(matrix_bricks, spec_brick_row, spec_brick_col + 1)
            if up is not None:
                disappear_list.append(up)
                self.touch_same_brick(matrix_bricks, spec_brick_row - 1, spec_brick_col)

        # for row in len(matrix_bricks):
        #     for col in len(row):
        #         if self.get_brick_color() == matrix_bricks[row][col].get_brick_color():
        #             disappear_list.append(matrix_bricks[row][col])
        #             self.points += POINT
        if len(disappear_list) == 0:
            helpers.create_replacement(self.brick_color, self.x_pos, self.y_pos)
        self.reset_player()
        return disappear_list

    def reset_player(self):
        color = random.choice(COLORS_LIST)
        self.brick_color = color
        self.x_pos = LAUNCH_X_POS
        self.y_pos = LAUNCH_Y_POS

    def check_left(self, matrix_bricks, row, col):
        if (col - 1) < 0 or (col - 1) > 10:
            return None
        if matrix_bricks[row][col - 1].get_brick_color() == self.brick_color:
            return matrix_bricks[row][col - 1]

    def check_right(self, matrix_bricks, row, col):
        if (col + 1) < 0 or (col + 1) > 10:
            return None
        if matrix_bricks[row][col + 1].get_brick_color() == self.brick_color:
            return matrix_bricks[row][col + 1]

    def check_up(self, matrix_bricks, row, col):
        if (row - 1) < 0 or (row - 1) > 4:
            return None
        if matrix_bricks[row - 1][col].get_brick_color() == self.brick_color:
            return matrix_bricks[row - 1][col]
