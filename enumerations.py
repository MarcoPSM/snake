from enum import Enum


class Color(Enum):
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GRAY = (40, 40, 40)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
