from enum import Enum, unique
from math import sqrt
from random import randint

import pygame


@unique
class Color(Enum):
    """color"""

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        """random color"""
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)


class Ball(object):
    """ball"""

    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        """initt"""
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        """move"""
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        """eat that ball"""
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:
                other.alive = False
               	self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        """draw balls"""
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)


def main():
    # balls container
    balls = []
    # init pygame module
    pygame.init()
    # init windows sizes
    screen = pygame.display.set_mode((800, 600))
    print(screen.get_width())
    print(screen.get_height())
    # set windows caption
    pygame.display.set_caption('Big balls eat small balls')
    # define small ball position of Windows
    x, y = 50, 50
    running = True
    # Start a loop event to deal
    while running:
        # get event to deal
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                ball = Ball(x, y, radius, sx, sy, color)
                balls.append(ball)
        screen.fill((255, 255, 255))
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()
        # init windows 50 mrico seconds refresh ball position
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            for other in balls:
                ball.eat(other)


if __name__ == '__main__':
    main()
