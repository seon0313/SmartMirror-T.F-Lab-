import pygame


class Alert:
    def __init__(self, surface: pygame.Surface,color:tuple|pygame.Color,background_color:tuple|pygame.Color,
                 font:pygame.font.Font, small_font:pygame.font.Font):
        self.sf:pygame.Surface = surface
        self.color:tuple|pygame.Color = color
        self.bg:tuple|pygame.Color = background_color
        self.font: pygame.font.Font = font
        self.small_font: pygame.font.Font = small_font
