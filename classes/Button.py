import pygame.examples.glcube
from helpers import screen


class Button:
    def __init__(self, x_pos, y_pos, width, height):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height

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

    def on_click(self, mouse_pos):
        if self.x_pos + self.width > mouse_pos[0] > self.x_pos and \
                self.y_pos < mouse_pos[1] < self.y_pos + self.height:
            return True

    def create_button(self):
        pygame.draw.rect(screen, pygame.Rect(self.x_pos, self.y_pos, self.width, self.height))
