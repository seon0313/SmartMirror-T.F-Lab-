import pygame


class Text:
    def __init__(self,font:pygame.font.Font, text: str, color: tuple | pygame.Color,
                 antialias: bool=True, background: tuple | pygame.Color | None = None):
        self.text = text
        self.color = color
        self.antialias = antialias
        self.font = font
        self.background = background

        self.ob = None
        self.ob_rect = None

        self.old_data = ''

    def blit(self, surface: pygame.Surface, x, y, horizontal: int=0, vertical: int=0):
        if self.text != self.old_data:
            self.ob = self.font.render(self.text, self.antialias, self.color, self.background)  # object
            self.ob_rect = self.ob.get_rect()
            self.old_data = self.text

        if horizontal == 0: self.ob_rect.centerx = x
        elif horizontal == 1: self.ob_rect.x = x
        elif horizontal == 2: self.ob_rect.x = x - self.ob_rect.w

        if vertical == 0: self.ob_rect.centery = y
        elif vertical == 1: self.ob_rect.y = y
        elif vertical == 2: self.ob_rect.y = y - self.ob_rect.h

        surface.blit(self.ob, self.ob_rect)

    def getRect(self) -> pygame.Rect:
        if self.ob == None:
            self.ob = self.font.render(self.text, self.antialias, self.color, self.background)  # object
            self.ob_rect = self.ob.get_rect()
        return self.ob_rect