import pygame
from enumerations import Color, Direction


class Snake:
    body = []
    cell_size = 0
    look = None
    board_size = 0
    color = ()
    direction = None

    def __init__(self, board_size, cell_size):
        self.cell_size = cell_size
        self.board_size = board_size
        initial_pos = self.initial_position()
        self.direction = Direction.RIGHT
        self.color = Color.WHITE.value

        self.body = [(initial_pos[0], initial_pos[1]),
                     (initial_pos[0] + self.cell_size, initial_pos[1]),
                     (initial_pos[0] + self.cell_size * 2, initial_pos[1])]
        self.look = pygame.Surface((self.cell_size, self.cell_size))
        self.look.fill(self.color)

    def initial_position(self):
        pos = self.board_size // 3
        x = pos - pos % self.cell_size
        y = pos - pos % self.cell_size
        return x, y

    def head(self):
        return self.body[0]

    def grow(self):
        self.body.append((0, 0))

    def size(self):
        return len(self.body)

    def self_collision(self):
        for part in self.body[1:-1]:
            if self.head()[0] == part[0] and self.head()[1] == part[1]:
                return True
        return False

    def crawl(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i] = (self.body[i - 1][0], self.body[i - 1][1])

        if self.direction == Direction.UP:
            self.body[0] = (self.body[0][0], self.body[0][1] - self.cell_size)
        if self.direction == Direction.RIGHT:
            self.body[0] = (self.body[0][0] + self.cell_size, self.body[0][1])
        if self.direction == Direction.DOWN:
            self.body[0] = (self.body[0][0], self.body[0][1] + self.cell_size)
        if self.direction == Direction.LEFT:
            self.body[0] = (self.body[0][0] - self.cell_size, self.body[0][1])

    def move_up(self):
        self.direction = Direction.UP

    def move_right(self):
        self.direction = Direction.RIGHT

    def move_down(self):
        self.direction = Direction.DOWN

    def move_left(self):
        self.direction = Direction.LEFT

    def draw(self, surface):
        for part in self.body:
            surface.blit(self.look, part)
