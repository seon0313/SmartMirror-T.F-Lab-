import time

import pygame


class Dust:
    def __init__(self,surface:pygame.Surface):
        self.surface:pygame.Surface = surface
        self.size = self.surface.get_size()
        import random
        self.max = random.randint(60,int(self.size[1]/2))
        self.min = random.randint(60, self.max)
        self.s = random.randint(self.min, self.max)
        self.pos = [random.randint(1,self.size[0]),random.randint(1,self.size[1])]
        self.x = random.randint(10,25)
        self.y = random.randint(10,25)
        self.color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
        self.t = time.time()
        self.xa = random.randint(-1,1)
        self.ya = random.randint(-1,1)

    def blit(self, dt:float, surface=pygame.Surface):

        self.pos[0] += dt*(self.xa*self.x)
        self.pos[1] += dt*(self.ya*self.y)

        if (self.pos[0] < 0 or self.pos[0] > self.size[0]) or (self.pos[1] < 0 or self.pos[1] > self.size[1]):
            import random
            self.pos = [random.randint(1,self.size[0]),random.randint(1,self.size[1])]
            self.xa = random.randint(-1, 1)
            self.ya = random.randint(-1, 1)

        pygame.draw.circle(surface, self.color, self.pos, self.s)