import pygame
import random
from vec2d import Vec2d
from globals import WIDTH, HEIGHT


class Balloon:
    def __init__(self, pos: tuple[float, float], vel: tuple[float, float], size: float, color: tuple[int, int, int]):
        self.pos = Vec2d(pos[0], pos[1])
        self.vel = Vec2d(vel[0], vel[1])
        self.size = size
        self.color = color

    
    def update(self, dt):
         self.pos += self.vel * dt / 1000
    

    def draw(self, screen: pygame.Surface):
            pygame.draw.rect(screen, self.color, (self.pos.x, self.pos.y, self.size, self.size))
    

    def is_inside(self, x, y) -> bool:
        return (self.pos.x <= x and x <= self.pos.x + self.size and self.pos.y <= y and y <= self.pos.y + self.size)
    

def generateRandomBalloon() -> Balloon:
     return Balloon((random.randint(0, WIDTH), random.randint(0, HEIGHT)),
                    (random.randint(-20, 20), random.randint(-160, -80)), 
                     random.randint(10, 50), 
                    (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))