# T.F Lab 정기/단체 프로젝트 Smart Mirror 소프트웨어

개발 - 추윤선

***

 ## 사용한 라이브러리 / 자산

 * 경기천년체
 * Pygame -> Pygame-CE (pygame - Comunity Edition) # Blur 기능을 위하여 변경
 * Json
 * Time
 * Threading
 * BeautifulSoup
 * urllib3
 * html5lib

 * 뉴스소스: 연합뉴스
 * 기상소스: 기상청 API

***

## 기능
* 시계 - 12 / 24 설정 가능 (setting.json)
* 백그라운드 동적 애니메이션 - 스마트미러를 구동할때 마다 색상, 애니메이션, 패턴이 랜덤으로 생성 됨
  
  ㄴ (애플뮤직/유튜브 플레이시 배경화면이 앨범/영상의 주요 색상에 따라 바뀌는 애니메이션과 같음)

* 날씨 - 기상청 API 활용. 추후 IOT 기능을 추가하여 바깥 날씨 뿐만 아닌 실내의 상황까지 띄워줄 예정
* 뉴스 - 연합뉴스 핫뉴스 데이터 크롤링. 추후 과학,IT등 기술적인 뉴스로 전환 예정

***

## 초기설정
1. 날씨 위젯을 사용하기 위해서는 setting.json에서 api > weather의 값을 기상청 초단기예보 api key로 설정

***

README.md의 내용들은 추후 알아보기 쉽도록 단어 및 문장을 수정할 예정입니다.

T.F Lab - 추윤선
