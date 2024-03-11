import time

import pygame

from ui.Widget import Widget
from m.News import getHotNews
from ui.Text import Text
import threading


class NewsWidget(Widget):
    def __init__(self):
        super().__init__()
        self.data: list[dict] = None
        self.load = False
        self.sf: pygame.Surface = None
        self.index = 0
        self.time = 0
        self.news_title = Text(self.font,'_',(255,255,255))
        self.source_by = Text(self.small_font,'source by 연합뉴스', (100,100,100))
        self.text = ''

    def getNews(self):
        try: self.data = getHotNews()
        except Exception as e: print('NewsWidget Error - ',e)
        self.load = False

    def run(self, rect) -> pygame.Surface:
        self.sf = pygame.Surface(rect, pygame.SRCALPHA)
        size = self.sf.get_size()

        if self.data == None and not self.load:
            self.load = True
            threading.Thread(target=self.getNews).start()

        if self.data != None:
            if self.time == 0: self.time = time.time()

            if time.time()-self.time >= 5:
                self.index+=1
                self.time = time.time()
            if self.index > len(self.data): self.index = 0

            text = f'TOP {self.index+1} | '+self.data[self.index]['title']
            if self.text != text: self.news_title.text, self.text = (text,text)
            self.news_title.blit(self.sf,size[0]/2,0,vertical=1)

            height = self.news_title.getRect().h
            self.source_by.blit(self.sf,size[0]/2,height,vertical=1)

        return self.sf