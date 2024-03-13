import sys

import pygame, time, json
from ui.Text import Text
from ui.Clock import Clock
from ui.Widget import WidgetUI, WidgetType
from ui.Weather_Widget import WeatherWidget
from ui.News_Widget import NewsWidget
from ui.Background import Background

class App:
    theme: dict
    fonts: dict
    setting: dict
    dt: int
    def __init__(self):
        pygame.init()

    def load(self):
        self.sc: pygame.Surface = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)
        with open('./theme/default.json', 'rb') as file:
            App.theme: dict = json.load(file)
            file.close()
        self.logo: pygame.Surface = pygame.image.load('./i/tf_dot_text_logo.svg')
        self.sc.fill(App.theme['background-color'])
        size = self.sc.get_size()
        size_logo = self.logo.get_size()
        self.sc.blit(self.logo, ((size[0]/2)-(size_logo[0]/2),(size[1]/2)-(size_logo[1]/2)))
        pygame.display.flip()

        with open('./setting.json', 'rb') as file:
            App.setting: dict = json.load(file)
            file.close()

        self.clock: pygame.time.Clock = pygame.time.Clock()

        font_sizes = []
        App.fonts: dict[pygame.font.Font] = {}

        for i in App.theme.keys():
            if 'font' in i and not (App.theme[i] in font_sizes): font_sizes.append(App.theme[i])

        for i in font_sizes:
            App.fonts[i] = pygame.font.Font('./f/경기천년제목_Medium.ttf',i)
        print('load end')
        self.run()

    def getFont(theme: str) -> pygame.font.Font:
        return App.fonts[App.theme[theme]]

    def run(self):
        App.dt = 1/App.setting['fps']
        size = self.sc.get_size()

        clock = Clock()

        weather_widget = WeatherWidget()
        news_widget = NewsWidget()

        bottom_widget = WidgetUI(size[0], App.theme['big-font-size']+App.theme['small-font-size'], WidgetType.Static, [news_widget])
        center_small_widget = WidgetUI(size[0]/2, App.theme['big-font-size'], WidgetType.Static, [weather_widget])

        background = Background(self.sc)

        while True:
            t = time.time()
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.sc.fill(App.theme['background-color'])

            background.blit()

            size = self.sc.get_size()
            clock.blit(self.sc,size[0]/2,size[1]/2)

            center_small_widget.blit(self.sc,size[0]/2,size[1]/2+App.theme['clock-font-size']/2)
            bottom_widget.blit(self.sc, size[0]/2, size[1]-bottom_widget.h)

            if App.setting['dev']:
                text = Text(App.getFont('dev-font-size'), f'fps: {self.clock.get_fps()}', (255,255,255))
                text.blit(self.sc,10,10,1,1)

            pygame.display.flip()
            self.clock.tick(App.setting['fps'])
            App.dt = time.time()-t