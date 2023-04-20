import pygame


def draw_text(screen: pygame.Surface, text: str, font: pygame.font.Font, x: int, y: int):
    rendered_text = font.render(text, True, (255, 255, 255))
    text_rect = rendered_text.get_rect()
    text_rect.x = x
    text_rect.y = y
    screen.blit(rendered_text, text_rect)
