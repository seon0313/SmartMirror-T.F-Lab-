import pygame


class Widget:
    def __init__(self):
        from uuid import uuid4
        from m.App import App
        self.id = uuid4()
        self.font = App.getFont('big-font-size')
        self.small_font = App.getFont('small-font-size')

    def run(self, rect) -> pygame.Surface:
        sf = pygame.Surface(rect)
        return sf

    def getFun(self): return self.function

class WidgetUI:
    def __init__(self, width: float, height: float, WidgetType: int, Items: list[Widget] = []):
        self.w: float = width
        self.h: float = height
        self.type: int = WidgetType
        self.items: list = Items
        self.focus: int = 0
        self.time = 0
    def blit(self, surface: pygame.Surface, x: float, y: float, background: pygame.Surface | None = None):
        sf = pygame.Surface((self.w,self.h))
        if background != None:
            sf.blit(background, (0,0))
        try:
            if self.type == WidgetType.Static:
                i_sf:pygame.Surface = self.items[self.focus].run(sf.get_size())
                sf.blit(i_sf, (0,0))
            if self.type == WidgetType.Stack:
                pass
            if self.type == WidgetType.Slide:
                pass
        except Exception as e: print(e)

        sf_R = sf.get_rect()
        sf_R.center = (x,y)

        surface.blit(sf,sf_R)

    def itemAppend(self, item: Widget):
        self.items.append(item)

class WidgetType:
    Static: int = 0
    Stack: int = 1
    Slide: int = 2

