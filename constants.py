import pygame

# Width and Height of the project window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

LAUNCH_X_POS = 300
LAUNCH_Y_POS = 540

BRICK_WIDTH = 60
BRICK_HEIGHT = 60

BRICK_UP_MOVEMENT = 5
BRICK_MOVEMENT = 60
BRICK_DISTANCE = 60

POINT = 1
# Color Shortcuts

YELLOW = "yellow"
RED = "red"
BLUE = "blue"
GREEN = "green"
PURPLE = "purple"
TRANSPARENT = (0, 0, 0, 0)

COLORS_LIST = [RED, YELLOW, GREEN, PURPLE, BLUE]
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
