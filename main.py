import pygame

from constants import *
from helpers import *
from classes.Brick import *
from classes.Player import *


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Brick Breaker')

    clock = pygame.time.Clock()

    # Set up background image
    set_background()
    brick1 = Player("green", BRICK_WIDTH, BRICK_HEIGHT, LAUNCH_X_POS, LAUNCH_Y_POS)
    new_row = colored_bricks(0)
    row_displayer(new_row)
    brick1.display_brick()
    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    brick1.move_left()
                if event.key == pygame.K_RIGHT:
                    brick1.move_right()
                if event.key == pygame.K_UP:
                    brick1.launch()
                    # brick1.touch_same_brick(new_row)

        # Update the screen
        update_screen([brick1, new_row])

        pygame.display.flip()
        # Update display - without input update everything

        pygame.display.update()

        # brick1.display_brick()
        # brick1.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        clock.tick(120)
    pygame.quit()
    quit()


main()
