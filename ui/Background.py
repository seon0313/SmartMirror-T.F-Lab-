import time

import pygame
from particle.Dust import Dust

class Background:
    def __init__(self, surface):
        self.sc: pygame.surface=surface
        self.sf: pygame.surface = pygame.Surface(self.sc.get_size())
        self.sf = pygame.Surface(surface.get_size())
        self.particle: list = []
        self.t = time.time()

    def blit(self):
        from m.App import App
        if len(self.particle) <= 0:
            self.particle.append(Dust(self.sf))
        if len(self.particle)<4 and time.time()-self.t >= 3:
            self.particle.append(Dust(self.sf))
            self.t = time.time()
        for i in self.particle:
            i.blit(App.dt,self.sf)

        self.sf = pygame.transform.box_blur(self.sf, 100)
        self.sc.blit(self.sf,(0,0))