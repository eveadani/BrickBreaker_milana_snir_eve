import pygame
import random

from constants import *
from classes.Brick import *
from classes.Player import *

"""
    The function get button and mouse press position on screen and return True
    if mouse click on button
    :param button: Button object
        button on screen
    :param mouse_pos: tuple
        the x and y position of the mouse cursor
    :return: boolean
        True if mouse click on button, else False
    """


def mouse_in_button(button, mouse_pos):
    if button.x_pos + button.width > mouse_pos[0] > button.x_pos and \
            button.y_pos < mouse_pos[1] < button.y_pos + button.height:
        return True

# Displays the bricks on the screen, repeats the action.
def colored_bricks(y_pos):
    if y_pos < 0 or y_pos > WINDOW_HEIGHT:
        return False
    list_brick = []
    x_pos = 0
    for i in range(10):
        color = random.choice(COLORS_LIST)
        random_brick = Brick(color, BRICK_WIDTH, BRICK_HEIGHT, x_pos, y_pos)
        list_brick.append(random_brick)
        x_pos += BRICK_DISTANCE
    return list_brick

# Organizes the bricks in their respective rows each.
def row_displayer(list_of_bricks):
    for i in list_of_bricks:
        i.display_brick()

# Sets the background
def set_background():
    img = pygame.image.load("images/main_background.png")
    img = pygame.transform.scale(img, (WINDOW_WIDTH, WINDOW_HEIGHT))
    # Display the background
    SCREEN.blit(img, (0, 0))

# Sets starting screen
def set_starting_screen():
    img = pygame.image.load("images/start_screen.png")
    img = pygame.transform.scale(img, (WINDOW_WIDTH, WINDOW_HEIGHT))
    # Display the background
    SCREEN.blit(img, (0, 0))


# Updates the screen
def update_screen(object_list):
    set_background()
    for i in object_list:
        if type(i) is list:
            for j in i:
                j.display_brick()
        elif type(i) is Player:
            i.display_brick()
        # else:
        #     return False


# Replace bricks which I want to delete with in and do pass if so, update_screen do matrix_bricks
def reset_player(player):
    color = random.choice(COLORS_LIST)
    player.set_brick_color(color)
    player.set_x_pos = LAUNCH_X_POS
    player.set_y_pos = LAUNCH_Y_POS


# Creates a replacement for the brick for the removed bricks
def create_replacement(color, x, y):
    brick_replacement = Brick(color, BRICK_WIDTH, BRICK_HEIGHT, x, y)
    brick_replacement.display_brick()
