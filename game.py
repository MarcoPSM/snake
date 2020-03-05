import pygame
from pygame.locals import *
import time
from enumerations import Color, Direction
from apple import Apple
from snake import Snake


class Game:
    screen = None
    clock = None

    def __init__(self):
        self.title = "Snake"
        self.board_size = 600  # its always a square
        self.cell_size = 40
        self.board_color = Color.BLACK.value
        self.has_grid = True
        self.grid_color = Color.GRAY.value
        self.speed = 10
        self.pause = 2
        self.running = True
        # Score
        self.score = 0
        self.score_font = "bahnschrift"
        self.score_size = 30
        self.score_color = Color.GREEN.value
        self.score_position = (self.board_size - 4 * self.cell_size, self.cell_size)
        self.score_text = 'Score: '
        # Game over
        self.game_over_font = "bahnschrift"
        self.game_over_size = 120
        self.game_over_color = Color.GREEN.value
        self.game_over_position = (self.board_size // 6, self.board_size // 4)
        self.game_over_text = 'Game Over'

        self.snake = Snake(self.board_size, self.cell_size)
        self.apple = Apple(self.board_size, self.cell_size)
        self.apple.random_position()

    def boundaries_collision(self):
        snake_head = self.snake.head()
        return snake_head[0] == self.board_size or snake_head[1] == self.board_size or \
               snake_head[0] < 0 or snake_head[1] < 0

    def eat(self):
        return self.snake.head()[0] == self.apple.position()[0] and \
               self.snake.head()[1] == self.apple.position()[1]

    def draw_grid(self):
        for i in range(0, self.board_size, self.cell_size):  # Draw vertical lines
            pygame.draw.line(self.screen, self.grid_color, (i, 0), (i, self.board_size))
        for i in range(0, self.board_size, self.cell_size):  # Draw horizontal lines
            pygame.draw.line(self.screen, self.grid_color, (0, i), (self.board_size, i))

    def draw_score(self):
        score_font = pygame.font.SysFont(self.score_font, self.score_size)
        text = score_font.render(self.score_text + str(self.score), True, self.score_color)
        self.screen.blit(text, self.score_position)

    def game_over(self):
        print("GO")
        font = pygame.font.SysFont(self.game_over_font, self.game_over_size)
        text = font.render(self.game_over_text, True, self.game_over_color)
        self.screen.blit(text, self.game_over_position)
        pygame.display.update()
        time.sleep(self.pause)
        exit()

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.board_size, self.board_size))
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()

        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                if event.type == KEYDOWN:
                    if event.key == K_UP and self.snake.direction != Direction.DOWN:
                        self.snake.move_up()
                    if event.key == K_RIGHT and self.snake.direction != Direction.LEFT:
                        self.snake.move_right()
                    if event.key == K_DOWN and self.snake.direction != Direction.UP:
                        self.snake.move_down()
                    if event.key == K_LEFT and self.snake.direction != Direction.RIGHT:
                        self.snake.move_left()

            if self.eat():
                self.apple.random_position()
                self.snake.grow()
                self.score += 1

            if self.boundaries_collision():
                self.game_over()

            if self.snake.self_collision():
                self.game_over()

            self.snake.crawl()

            self.screen.fill(self.board_color)
            if self.has_grid:
                self.draw_grid()
            self.apple.draw(self.screen)
            self.snake.draw(self.screen)
            self.draw_score()
            pygame.display.update()

            self.clock.tick(self.speed)


if __name__ == '__main__':
    game = Game()
    game.run()
