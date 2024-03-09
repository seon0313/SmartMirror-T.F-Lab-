# We use data from Yonhap News.
# 연합뉴스의 데이터를 사용합니다.


def getHotNews() -> list:
    from bs4 import BeautifulSoup
    import requests

    import urllib3
    from urllib3.util.ssl_ import create_urllib3_context

    ctx = create_urllib3_context()
    ctx.load_default_certs()
    ctx.options |= 0x4  # ssl.OP_LEGACY_SERVER_CONNECT

    with urllib3.PoolManager(ssl_context=ctx) as http:
        r = http.request("GET", "https://www.yna.co.kr/theme/mostviewed/index")

    data = r.data.decode('utf8')#equests.get('https://www.yna.co.kr/theme/mostviewed/index', verify=False).text

    soup = BeautifulSoup(data, 'html5lib')
    a = soup.find('section',attrs={'class': 'box-mostviewed-list01'})
    b = a.find('div', attrs={'class':'list-type104'})
    c = b.find('ul', attrs={'class':'list'})
    d = c.find_all('a', attrs={'class':'tit-wrap'})
    items = []

    for i in d:
        items.append({'title': i.find_next('strong').text, 'href': i.attrs['href']})

    return items


if __name__ == '__main__':
    print(getHotNews())