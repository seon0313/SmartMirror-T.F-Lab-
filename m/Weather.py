def getWeather(date:str, time:str, autoBack=True) -> dict:
    from requests import get
    from json import loads
    from m.App import App
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
    params = {'serviceKey': App.setting['api']['weather'], 'dataType': 'JSON', 'base_date': date,
              'base_time': time, 'nx': '55', 'ny': '127'}
    response = get(url, params=params,timeout=2)
    print(response.content.decode('utf8'))
    data = loads(response.content.decode('utf8'))['response']
    if data['header']['resultMsg'] == 'NO_DATA':
        return getWeather(date, str(int(time)-30))
    else: data = data['body']['items']['item']

    result = {'date':date,'time': time}
    for i in data:
        result[i['category']] = i['obsrValue']
    return result

# {'PTY': '0', 'REH': '79', 'RN1': '0', 'T1H': '1.8', 'UUU': '-0.2', 'VEC': '33', 'VVV': '-0.3', 'WSD': '0.5'}

if __name__ == '__main__':
    import time
    date = time.strftime("%Y%m%d", time.localtime(time.time()))
    print(getWeather('20240310', '0000'))#date, '0600'))