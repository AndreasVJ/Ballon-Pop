import pygame


def draw_text(screen: pygame.Surface, text: str, font: pygame.font.Font, x: int, y: int, centered = False):
    rendered_text = font.render(text, True, (255, 255, 255))
    text_rect = rendered_text.get_rect()
    text_rect.x = x
    text_rect.y = y
    if centered:
        text_rect.x -= text_rect.width/2
        text_rect.y -= text_rect.height/2

    screen.blit(rendered_text, text_rect)
