import random
import pygame
from enumerations import Color


class Apple:
    x = 0
    y = 0
    size = 0
    look = None
    board_size = 0
    color = ()

    def __init__(self, board_size, cell_size):
        self.size = cell_size
        self.board_size = board_size
        self.color = Color.RED.value
        self.look = pygame.Surface((self.size, self.size))
        self.look.fill(self.color)

    def random_position(self):
        self.x = random.randint(0, self.board_size - self.size)
        self.x -= self.x % self.size
        self.y = random.randint(0, self.board_size - self.size)
        self.y -= self.y % self.size

    def draw(self, surface):
        surface.blit(self.look, (self.x, self.y))

    def position(self):
        return self.x, self.y
