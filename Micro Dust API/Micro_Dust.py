#_*_coding:utf-8 _*_
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
from xml.etree.ElementTree import *
import datetime

API_KEY = unquote('hicQFwbbBJ5hqge6SCFIpv4ApaxpECQE8nacmxzocU3llRIEuDnlDuV5Aq5I%2FYb7wM3YowlheTtrcmet9SaQhg%3D%3D')
try:    
    url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'
    queryParams = '?' + urlencode({ quote_plus('ServiceKey') : API_KEY, quote_plus('numOfRows') : '1', quote_plus('pageNo') : '1', quote_plus('stationName') : '숭의', quote_plus('dataTerm') : 'DAILY', quote_plus('ver') : '1.2' })
    # 인천 미추홀구에 있는 관측소에서 관측한 정보를 가져온다.
    
    request = Request(url + queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()
    response_body = response_body.decode('utf-8')
    xmlData =fromstring(response_body)

    airlist=list()
    for parent in xmlData.iter("item"):
        air = list()
        for item in parent:
            air.append(item.text)
        airlist.append(air)
    for i in range(len(airlist)):
        print("시간 : ",airlist[i][0])
        print("미세먼지(PM10)농도 : ",airlist[i][6])
        print("미세먼지(PM10) 24시간 예측이동농도 : ",airlist[i][7])
        print("초미세먼지(PM2.5)농도 : ",airlist[i][8])
        print("초미세먼지(PM2.5) 24시간 예측이동농도 : ",airlist[i][9])
        print()
except Exception as er:
    print(er)
