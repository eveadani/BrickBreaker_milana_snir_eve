import pygame
from pygame import K_DOWN, KEYDOWN

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

    # Sets up the background image and displays the following bricks on the screen in organized rows.
    set_background()
    brick1 = Player("green", BRICK_WIDTH, BRICK_HEIGHT, LAUNCH_X_POS, LAUNCH_Y_POS)
    row1 = colored_bricks(0)
    row2 = colored_bricks(BRICK_HEIGHT)
    row3 = colored_bricks(BRICK_HEIGHT * 2)
    row4 = colored_bricks(BRICK_HEIGHT * 3)
    matrix_bricks = [row1, row2, row3, row4]
    for row in matrix_bricks:
        row_displayer(row)

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
                    for i in range(brick1.loop_times(brick1.get_x_pos(),brick1.get_y_pos(),matrix_bricks)):
                        brick1.set_y_pos(brick1.get_y_pos()-BRICK_MOVEMENT)
                        update_screen([brick1, row1, row2, row3, row4])
                        pygame.time.wait(700)
                    # brick1.launch(matrix_bricks)

        # Update the screen
        update_screen([brick1, row1, row2, row3, row4])

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
