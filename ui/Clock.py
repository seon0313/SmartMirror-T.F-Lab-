import time, pygame
from ui.Text import Text
import threading

class Clock:
    def __init__(self,font: pygame.font.Font, color: tuple | pygame.Color, time_format=12):
        self.font = font
        self.color = color
        self.time = time.time()
        self.format = time_format

        #self.thread_ = threading.Thread(target=self.time_thread,daemon=True)
        #self.thread_.start()
        self.hour:Text = None
        self.l:Text = None
        self.minute:Text = None
        self.sec = Text(self.font, ':', self.color)
        self.sec_r = self.sec.getRect()
    def blit(self,surface: pygame.Surface, x:int, y:int):
        hour_ = time.strftime('%H' if self.format == 24 else '%I', time.localtime(time.time()))
        if self.hour == None or self.hour.text != hour_:
            self.hour = Text(self.font, hour_, self.color)
            self.hour_r = self.hour.getRect()

        minute_ = time.strftime('%M', time.localtime(time.time()))
        if self.minute == None or self.minute.text != minute_:
            self.minute = Text(self.font, minute_, self.color)
            self.minute_r = self.minute.getRect()




        sf = pygame.Surface((self.hour_r.w+self.minute_r.w+self.sec_r.w, self.hour_r.h))
        sf_r = sf.get_rect()
        sf_r.center = (x,y)

        self.hour.blit(sf,0,0,1,1)
        self.minute.blit(sf,self.hour_r.w+self.sec_r.w,0,1,1)

        data = time.time() - self.time
        if 0 <= data <= 1:
            self.sec.blit(sf, self.hour_r.w, 0, 1, 1)
        if data >= 2:
            self.time = time.time()

        surface.blit(sf, sf_r)