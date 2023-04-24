import pygame
import sys
from balloon import Balloon, generate_random_balloon
from text import draw_text
from globals import FPS, WIDTH, HEIGHT, BALLON_ASPECT_RATIO


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font32 = pygame.font.Font("freesansbold.ttf", 32)
font64 = pygame.font.Font("freesansbold.ttf", 64)
pygame.display.set_caption("Balloon Pop")


class Game:
    def __init__(self, screen, game_time, num_balloons):
        self.screen = screen
        self.game_time = game_time * 1000
        self.max_time = self.game_time
        self.time = 0
        self.score = 0
        self.balloons: list[Balloon] = []
        for i in range(num_balloons):
            self.balloons.append(generate_random_balloon())


    def handle_input(self, event: pygame.event.Event):
        if event.type == pygame.QUIT:
            sys.exit()

        # Check if player pressed keyboard
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_ESCAPE:
                    sys.exit()
                
                # Reset all game states
                case pygame.K_r:
                    self.max_time = self.time + self.game_time
                    self.score = 0
                    self.balloons = []
                    for i in range(10):
                        self.balloons.append(generate_random_balloon())
        
        # Check if player clicked on a balloon
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for i, balloon in enumerate(self.balloons):
                if balloon.is_inside(x, y):
                    self.balloons[i] = generate_random_balloon()
                    self.score += 1


    def update(self):
        # Get elapsed time
        self.time = pygame.time.get_ticks()
        dt = clock.tick(FPS)

        # Update balloons
        for i, balloon in enumerate(self.balloons):
            balloon.update(dt)
            if balloon.pos.y < - balloon.size*BALLON_ASPECT_RATIO:
                self.balloons[i] = generate_random_balloon()
    

    def draw(self):
        # Clear previous frame
        screen.fill((0, 0, 0))

        # Check if time is used up
        if self.time > self.max_time:
            draw_text(screen, "Game Over", font64, 0, 0)
            draw_text(screen, f'score: {self.score}', font32, 300, 364)
            draw_text(screen, "Press 'r' to try again", font32, 300, 396)
        
        else:
            # Draw balloons
            for b in self.balloons:
                b.draw(screen)

            # Draw time and score
            draw_text(screen, f'time left: {(self.max_time - self.time) // 1000}', font32, 16, 16)
            draw_text(screen, f'score: {self.score}', font32, 16, 48)

        pygame.display.flip()


game = Game(screen, 60, 10)

while True:
    # Read input from user
    for event in pygame.event.get():
        game.handle_input(event)
    
    game.update()
    game.draw()
