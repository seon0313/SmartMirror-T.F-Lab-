import sys

import pygame, time, json, threading
from ui.Text import Text
from ui.Clock import Clock
from ui.Widget import WidgetUI, WidgetType
from ui.Weather_Widget import WeatherWidget
from ui.News_Widget import NewsWidget

class App:
    def __init__(self):
        pygame.init()
        self.load()
    def load(self):
        self.sc: pygame.Surface = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)
        with open('./theme/default.json', 'rb') as file:
            self.theme: dict = json.load(file)
            file.close()
        self.logo: pygame.Surface = pygame.image.load('./i/tf_dot_text_logo.svg')
        self.sc.fill(self.theme['background-color'])
        size = self.sc.get_size()
        size_logo = self.logo.get_size()
        self.sc.blit(self.logo, ((size[0]/2)-(size_logo[0]/2),(size[1]/2)-(size_logo[1]/2)))
        pygame.display.flip()

        with open('./setting.json', 'rb') as file:
            self.setting: dict = json.load(file)
            file.close()

        self.clock: pygame.time.Clock = pygame.time.Clock()

        font_sizes = []
        self.fonts: dict[pygame.font.Font] = {}

        for i in self.theme.keys():
            if 'font' in i and not (self.theme[i] in font_sizes): font_sizes.append(self.theme[i])

        for i in font_sizes:
            self.fonts[i] = pygame.font.Font('./f/경기천년제목_Medium.ttf',i)

        self.run()

    def getFont(self, theme: str) -> pygame.font.Font:
        return self.fonts[self.theme[theme]]

    def run(self):
        dt = 1/self.setting['fps']
        size = self.sc.get_size()

        clock = Clock(self.getFont('clock-font-size'),(255,255,255))

        weather_widget = WeatherWidget(self.fonts[self.theme['big-font-size']], self.fonts[self.theme['small-font-size']])
        news_widget = NewsWidget(self.fonts[self.theme['big-font-size']],self.fonts[self.theme['small-font-size']])

        bottom_widget = WidgetUI(size[0], self.theme['big-font-size']+self.theme['small-font-size']+5, WidgetType.Static, [news_widget])
        center_small_widget = WidgetUI(size[0]/2, self.theme['big-font-size'], WidgetType.Static, [weather_widget])

        while True:
            t = time.time()
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.sc.fill(self.theme['background-color'])

            size = self.sc.get_size()
            clock.blit(self.sc,size[0]/2,size[1]/2)

            center_small_widget.blit(self.sc,size[0]/2,size[1]/2+self.theme['clock-font-size']/2)
            w = bottom_widget.w
            bottom_widget.blit(self.sc, size[0]/2, size[0]-bottom_widget.h)

            if self.setting['dev']:
                text = Text(self.getFont('dev-font-size'), f'fps: {self.clock.get_fps()}', (255,255,255))
                text.blit(self.sc,10,10,1,1)

            pygame.display.flip()
            self.clock.tick(self.setting['fps'])
            dt = time.time()-t


if __name__ == '__main__':
    app = App()