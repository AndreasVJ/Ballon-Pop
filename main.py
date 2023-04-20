import pygame
import sys
from balloon import Balloon, generateRandomBalloon
from text import draw_text
from globals import FPS, WIDTH, HEIGHT


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font32 = pygame.font.Font('freesansbold.ttf', 32)
font64 = pygame.font.Font('freesansbold.ttf', 64)
pygame.display.set_caption('Balloon pop')


game_time = 12 * 1000
max_time = game_time
score = 0
balloons: list[Balloon] = []
for i in range(10):
    balloons.append(generateRandomBalloon())


while True:
    # Get elapsed time
    time = pygame.time.get_ticks()
    dt = clock.tick(FPS)

    # Clear previous frame
    screen.fill((0, 0, 0))

    # Read input from user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_ESCAPE:
                    sys.exit()
                
                case pygame.K_r:
                    score = 0
                    max_time = time + game_time
                    balloons = []
                    for i in range(10):
                        balloons.append(generateRandomBalloon())
        
        # Check if player clicked on a balloon
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for i, b in enumerate(balloons):
                if b.is_inside(x, y):
                    balloons[i] = generateRandomBalloon()
                    score += 1
                    
    
    # Check if time is used up
    if time > max_time:
        draw_text(screen, "Game Over", font64, 300, 300)
        draw_text(screen, f'score: {score}', font32, 300, 364)
        draw_text(screen, "Press 'r' to try again", font32, 300, 396)

    else:
        # Update balloons
        for i, b in enumerate(balloons):
            b.update(dt)
            if b.pos.y < - b.size:
                balloons[i] = generateRandomBalloon()
            b.draw(screen)

        
        # Draw time and score
        draw_text(screen, f'time left: {(max_time - time) // 1000}', font32, 16, 16)
        draw_text(screen, f'score: {score}', font32, 16, 48)

    pygame.display.flip()