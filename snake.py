import pygame


class Snake:
    body = []
    cell_size = 0
    look = None
    board_size = 0
    color = (255, 255, 255)
    direction = 1

    def __init__(self, board_size, cell_size):
        self.cell_size = cell_size
        self.board_size = board_size
        initial_pos = self.board_size // 3
        self.body = [(initial_pos, initial_pos),
                     (initial_pos + self.cell_size, initial_pos),
                     (initial_pos + self.cell_size * 2, initial_pos)]
        self.look = pygame.Surface((self.cell_size, self.cell_size))
        self.look.fill(self.color)

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

        if self.direction == 0:
            self.body[0] = (self.body[0][0], self.body[0][1] - self.cell_size)
        if self.direction == 1:
            self.body[0] = (self.body[0][0] + self.cell_size, self.body[0][1])
        if self.direction == 2:
            self.body[0] = (self.body[0][0], self.body[0][1] + self.cell_size)
        if self.direction == 3:
            self.body[0] = (self.body[0][0] - self.cell_size, self.body[0][1])

    def move_up(self):
        self.direction = 0

    def move_right(self):
        self.direction = 1

    def move_down(self):
        self.direction = 2

    def move_left(self):
        self.direction = 3

    def draw(self, surface):
        for part in self.body:
            surface.blit(self.look, part)
