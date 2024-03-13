# T.F Lab 정기/단체 프로젝트 Smart Mirror 소프트웨어

![T.F Lab](/i/tf_dot_text_logo.svg)

개발 - 추윤선

***

## 목차

* [개요](#개요)
* [사용한 라이브러리 / 자산](#사용한-라이브러리-/-자산)
* [기능](#기능)
* [설치](#설치)
* [초기설정](#초기설정)
* [라이센스](#LICENSE)

***

## 개요

T.F Lab의 스마트미러 하드웨어에 탑재될 소프트웨어.

개발환경: Windows 11

실행환경: Ubuntu 23.10

***

 ## 사용한 라이브러리 / 자산

 * Python 3.12
 * 경기천년체
 * Pygame -> Pygame-CE (pygame - Comunity Edition) # Blur 기능을 위하여 변경
 * Json
 * Time
 * Threading
 * BeautifulSoup 4
 * urllib3
 * html5lib

 * 뉴스소스: 연합뉴스
 * 기상소스: 기상청 API

### SmartMirror - T.F Lab은 자체 제작 라이브러리로 UI를 구연합니다.
 | 파일 | 설명 |
 | --- | --- |
 | m.App.py | 프로그램 메인 클래스 |
 | m.News.py | 뉴스(연합뉴스) 크롤링 모듈 |
 | m.NowPlaying.py | 현재 재생중인 미디어(영상, 음악)의 정보를 받아오는 모듈 |
 | m.Weather.py | 기상청 API 모듈 |
 | particle.Dust.py | 배경화면의 색상 오브젝트 |
 | particle.Particle.py | 다양한 Particle 오브젝트의 기반이 되는 모듈 |
 | ui.Alert.py | 알람 시스템의 UI |
 | ui.Background.py | 백그라운드 시스템의 UI |
 | ui.Clock.py | 시계 |
 | ui.News_Widget.py | 뉴스 위젯 |
 | ui.Text.py | 텍스트 UI |
 | ui.Weather_Widget.py | 날씨 위젯 |
 | ui.Widget.py | 위젯 UI |

***

## 기능
* 시계 - 12 / 24 설정 가능 (setting.json)
* 백그라운드 동적 애니메이션 - 스마트미러를 구동할때 마다 색상, 애니메이션, 패턴이 랜덤으로 생성 됨
  
  ㄴ (애플뮤직/유튜브 플레이시 배경화면이 앨범/영상의 주요 색상에 따라 바뀌는 애니메이션과 같음)

* 날씨 - 기상청 API 활용. 추후 IOT 기능을 추가하여 바깥 날씨 뿐만 아닌 실내의 상황까지 띄워줄 예정
* 뉴스 - 연합뉴스 핫뉴스 데이터 크롤링. 추후 과학,IT등 기술적인 뉴스로 전환 예정

***

## 설치
Python 3를 다운로드 합니다.

권장: Python 3.6 >=

테스트 됨: Python 3.12, Python 3.12.2

설치가 필요한 라이브러리는 다음과 같습니다.

python-ce, beautifulsoup4, html5lib, urllib3

다음 명령어로 라이브러리를 설치할수있습니다.

```
pip install <라이브러리 명>
pip3 install <라이브러리 명>
python -m pip install <라이브러리 명>
python3 -m pip isntall <라이브러리 명>

#예)
pip install pygame-ce
```

깃허브에서 모든 소스를 다운로드 합니다.

소스를 압축해제 후 해제된 폴더에서 main.py를 실행합니다.

main.py를 더블클릭하여 실행하거나 CMD 또는 터미널에서 다음과 같은 명령어로 실행합니다.
```
python main.py
```
명령어로 실행시 CD 명령어를 이용해 압축해제한 폴더로 이동후 위 명령어를 실행해 주세요.

## 초기설정
1. 날씨 위젯을 사용하기 위해서는 setting.json에서 api > weather의 값을 기상청 초단기예보 api key로 설정

***

README.md의 내용들은 추후 알아보기 쉽도록 단어 및 문장을 수정할 예정입니다.

***

## LICENSE

Apache-2.0 license

사용시 저작권 고지 필수

T.F Lab의 로고는 모두 T.F Lab 동아리에 있습니다.

Apache-2.0 license가 적용되는 것은 소스코드에 한정됩니다.

개발: T.F Lab - 추윤선
