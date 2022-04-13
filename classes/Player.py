from classes.Brick import *
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

    # ````   dont need launch
    def launch(self, matrix_bricks):
        if not self.y_pos < 0:

            clock = pygame.time.Clock()
            # loop_times = 0
            # x_pos_change = X_POS_CHANGE_LEFT
            # if self.get_x_pos() == X_POS_LEFTEST:
            #     loop_times = CANT_MOVE_LOOP_TIMES
            # elif self.get_x_pos() == X_POS_START:
            #     loop_times = START_MOVE_LEFT_LOOP_TIMES
            # else:
            #     loop_times = MOVE_LOOP_TIMES
            for i in range(self.loop_times(self.x_pos, self.y_pos, matrix_bricks)):
                cover_img = pygame.image.load('Images/main_background.png')
                SCREEN.blit(cover_img, (self.x_pos, self.y_pos))
                # pygame.draw.rect(SCREEN, YELLOW, (self.x_pos, self.y_pos), )
                self.set_y_pos(self.y_pos - BRICK_MOVEMENT)
                self.display_brick()
                print("displayed")
                # pygame.display.flip()
                clock.tick(120)

    # problem in function
    def loop_times(self, current_x_pos, current_y_pos, matrix_bricks):
        max_y_pos = 0
        for list_brick in matrix_bricks:
            for brick in list_brick:
                if (brick.get_y_pos() + BRICK_HEIGHT) > max_y_pos and current_y_pos <= (brick.get_y_pos() + BRICK_HEIGHT) and brick.get_x_pos() <= current_x_pos <= (
                        brick.get_x_pos() + BRICK_WIDTH):
                    max_y_pos = brick.get_y_pos() - BRICK_HEIGHT
        loops = (WINDOW_HEIGHT - max_y_pos) // 10
        print(loops)
        return loops

    # delete-brick in brick

    def touch_same_brick(self, brick_list):
        disappear_list = []
        for brick in brick_list:
            if self.y_pos <= brick.get_y_pos() + BRICK_HEIGHT and brick.get_x_pos() <= self.x_pos <= brick.get_x_pos() + BRICK_WIDTH:
                print(2)
                if self.get_brick_color() == brick.get_brick_color():
                    disappear_list.append(brick)
                    self.points += POINT
        if len(disappear_list) == 0:
            helpers.create_replacement(self.brick_color, self.x_pos, self.y_pos)
        else:
            for brick_disappear in disappear_list:
                cover_img = pygame.image.load('Images/main_background.png')
                SCREEN.blit(cover_img, (brick_disappear.get_x_pos(), brick_disappear.get_y_pos()))
