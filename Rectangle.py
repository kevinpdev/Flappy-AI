# This file contains the Rectangle and Obstacle class.
# The Rectangle class is used in the Obstacle class which are
# the moving obstacles the Birds have to dodge.
import Constants
import random


class Rectangle:
    def __init__(self, height, top):
        self.width = Constants.RECTANGLE_WIDTH
        self.height = height

        if top:
            self.x = Constants.SCREEN_WIDTH
            self.y = 0
        else:
            self.x = Constants.SCREEN_WIDTH
            self.y = Constants.SCREEN_HEIGHT - self.height

        self.pos = (self.x, self.y, self.width, self.height)


class Obstacle:
    def __init__(self):
        # the rectangle height is anywhere from 1/3 to 2/3 of the screen height
        self.top_rect = Rectangle(random.randint(Constants.SCREEN_HEIGHT // 3 * 1, Constants.SCREEN_HEIGHT // 3 * 2), True)
        # leave 150 space for bird
        self.bottom_rect = Rectangle(Constants.SCREEN_HEIGHT - 150 - self.top_rect.height, False)
        # edge variables for readability
        self.left_edge = self.top_rect.x
        self.right_edge = self.top_rect.x + self.top_rect.width

    def update_position(self, game):
        # update top rect
        self.top_rect.x -= Constants.RECTANGLE_SPEED
        self.top_rect.pos = (self.top_rect.x, self.top_rect.y, self.top_rect.width, self.top_rect.height)
        # update bottom rect
        self.bottom_rect.x -= Constants.RECTANGLE_SPEED
        self.bottom_rect.pos = (self.bottom_rect.x, self.bottom_rect.y, self.bottom_rect.width, self.bottom_rect.height)
        # update left edge variable
        self.left_edge = self.top_rect.x
        self.right_edge = self.top_rect.x + self.top_rect.width

