import pygame

from constants import*
from classes.Brick import*

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))



def mouse_in_button(button, mouse_pos):
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
    if button.x_pos + button.width > mouse_pos[0] > button.x_pos and \
            button.y_pos < mouse_pos[1] < button.y_pos + button.height:
        return True

def colored_bricks(y_pos):
    if y_pos < 0 or y_pos > WINDOW_HEIGHT:
        return False
    colored_bricks_list = [RED, YELLOW, GREEN, PURPLE, BLUE]
    list_brick = []
    x_pos = 0
    for i in range (10):
        color = random.choice(colored_bricks_list)
        random_brick = Brick(color, BRICK_WIDTH, BRICK_HEIGHT, x_pos, y_pos)
        list_brick.append(random_brick)
        x_pos += BRICK_DISTANCE
    return list_brick
def row_displayer(list_of_bricks):
    for i in list_of_bricks:
        i.display_brick()