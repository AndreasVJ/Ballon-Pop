import pygame
import numpy as np
import random
from vec2d import Vec2d
from globals import WIDTH, HEIGHT, BALLOON_RESOLUTION, BALLON_ASPECT_RATIO


def circle_arc(x, r):
    return np.sqrt(r**2 - x**2)


class Balloon:
    def __init__(self, pos: tuple[float, float], vel: tuple[float, float], size: float, color: tuple[int, int, int]):
        self.pos = Vec2d(pos[0], pos[1])
        self.vel = Vec2d(vel[0], vel[1])
        self.size = size
        self.color = color
        a = []
        for x in np.linspace(size, -size, BALLOON_RESOLUTION):
            a.append([x, -circle_arc(x, size)])
        for x in np.linspace(-size, size, BALLOON_RESOLUTION):
            a.append([x, BALLON_ASPECT_RATIO*circle_arc(x, size)])
        self.vertices = np.array(a)

    
    def update(self, dt):
         self.pos += self.vel * dt / 1000
    

    def draw(self, screen: pygame.Surface):
        pygame.draw.polygon(screen, self.color, self.vertices + [self.pos.x, self.pos.y])

        y = self.pos.y + BALLON_ASPECT_RATIO*circle_arc(0, self.size)

        pygame.draw.polygon(screen, self.color, np.array([[0, -self.size*0.2], [self.size*0.3, self.size*0.3], [-self.size*0.3, self.size*0.3]]) + [self.pos.x, self.pos.y + BALLON_ASPECT_RATIO*circle_arc(0, self.size)])

        # pygame.draw.line(screen, (255, 255, 255), (self.pos.x, self.pos.y + BALLON_ASPECT_RATIO*circle_arc(0, self.size)), (self.pos.x, self.pos.y + BALLON_ASPECT_RATIO*circle_arc(0, self.size) + 30), 3)
    

    def is_inside(self, x, y) -> bool:
        x_d = x - self.pos.x
        y_d = y - self.pos.y
        if -self.size <= x_d and x_d <= self.size:
            return (-circle_arc(x_d, self.size) <= y_d and y_d <= BALLON_ASPECT_RATIO*circle_arc(x_d, self.size,))
        return False
    

def generate_random_balloon() -> Balloon:
     return Balloon((random.randint(WIDTH*0.1, WIDTH*0.9), random.randint(HEIGHT, HEIGHT*1.2)),
                    (random.randint(-20, 20), random.randint(-160, -80)), 
                     random.randint(20, 50), 
                    (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))