import pygame

from constants import *
from helpers import screen, mouse_in_button


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Brick Breaker')

    clock = pygame.time.Clock()

    # Set up background image
    img = pygame.image.load("images/main_background.png")
    img = pygame.transform.scale(img, (WINDOW_WIDTH, WINDOW_HEIGHT))

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Display the background
        screen.blit(img, (0, 0))

        # Update the screen
        pygame.display.flip()
        # Update display - without input update everything

        pygame.display.update()
        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        clock.tick(60)
    pygame.quit()
    quit()
main()

