import pygame

from ui.Widget import Widget
from m.Weather import getWeather
from ui.Text import Text
import time
import threading


class WeatherWidget(Widget):
    def __init__(self, font: pygame.font.Font, small_font: pygame.font.Font):
        super().__init__(font, small_font)

        self.weather: dict = None
        self.load = False
        self.a = Text(self.font, "Loading", (255, 255, 255))

    def loadWeather(self, date, time_):
        try:
            self.weather = getWeather(date, time_)
        except Exception as e:
            print('WeatherWidget Error  - ;;')
        self.load = False
        print('Getting')

    def run(self, rect) -> pygame.Surface:
        sf = pygame.Surface(rect)

        size = sf.get_size()

        date = time.strftime('%Y%m%d', time.localtime(time.time()))
        time_ = time.strftime('%H%M', time.localtime(time.time()))
        t = int(time_[2:])
        if t < 30:
            t = '00'
        else:
            t = '30'
        time_ = time_[:2] + t

        if (self.weather is None or time_ != self.weather['time']) and not self.load:
            print('Get!!')
            self.load = True
            threading.Thread(target=self.loadWeather, args=(date, time_), daemon=True).start()

        # TMN: 일 최저기온℃, TMX: 일 최고기온℃, SKY: 하늘 상태, REH: 습도%, PTY: 강수 형태, POP: 강수 확률%, WSD: 풍속m/s, TMP: 현재 기온℃

        # SKY: 맑음(1), 구름많음(3), 흐림(4)
        # PTY: 없음(0), 비(1), 비/눈(2), 눈(3), 빗방울(5), 빗방울눈날림(6), 눈날림(7)
        sky = {'1': '맑음', '3': '구름 많음', '4': '흐림'}
        pty = {'0': None, '1': '비', '2': '눈비', '3': '눈', '5': '빗방울', '6': '빗방울과 눈날림', '7': '눈날림'}
        if self.weather != None:
            self.a.text = f'{self.weather["T1H"]}℃|습도: {self.weather["REH"]}%|{pty[self.weather["PTY"]]}|풍속: {self.weather["WSD"]}m/s'

        self.a.blit(sf, size[0] / 2, size[1] / 2)

        return sf
