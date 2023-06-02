import pygame
import numpy as np
import random
from math import cos, pi
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
        for x in np.linspace(0, pi, BALLOON_RESOLUTION):
            a.append([cos(x)*size, -circle_arc(cos(x)*size, size)])
        for x in np.linspace(pi, 0, BALLOON_RESOLUTION):
            a.append([cos(x)*size, BALLON_ASPECT_RATIO*circle_arc(cos(x)*size, size)])
        self.vertices = np.array(a)

    
    def update(self, dt):
         self.pos += self.vel * dt / 1000
    

    def draw(self, screen: pygame.Surface):
        pygame.draw.polygon(screen, self.color, self.vertices + [self.pos.x, self.pos.y])

        knot_y = BALLON_ASPECT_RATIO*circle_arc(0, self.size)
        knot_size = self.size*0.3
        pygame.draw.polygon(screen, self.color, np.array([[0, -knot_size], [knot_size, knot_size], [-knot_size, knot_size]]) + [self.pos.x, self.pos.y + knot_y])
    

    def is_inside(self, x, y) -> bool:
        x_d = x - self.pos.x
        y_d = y - self.pos.y
        if -self.size <= x_d and x_d <= self.size:
            return (-circle_arc(x_d, self.size) <= y_d and y_d <= BALLON_ASPECT_RATIO*circle_arc(x_d, self.size,))
        return False
    

def generate_random_balloon() -> Balloon:
     return Balloon((random.randint(int(WIDTH*0.1), int(WIDTH*0.9)), random.randint(HEIGHT, int(HEIGHT*1.2))),
                    (random.randint(-20, 20), random.randint(-160, -80)), 
                     random.randint(20, 50), 
                    (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))