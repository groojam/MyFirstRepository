# 집 환기 시스템
* 집에 들어가기 전에 미세먼지나 온도, 습도 값이 얼만지 보고 창문, 공기청정기, 제습기를 텔레그램으로 제어할 수 있는 시스템입니다.
* 미세먼지 데이터는 인천 미추홀구 관측소에서 측정한 미세먼지 데이터와 집 안에 있는 센서로 측정한 미세먼지 데이터 두가지로 제공됩니다.
* 현재 시스템에서는 실제로 창문을 여닫지는 않지만 모터의 각도를 조절해서 일정각도로 움직였을 시에 문이 여닫히는 것으로 표현됩니다.

## 필요한 부품
1. 스텝모터

    창문을 열고 닫을 때 사용합니다.
2. 미세먼지 센서, 온습도 센서
    
    집안의 미세먼지 농도와 온습도를 측정하기위해 사용합니다.
3. 릴레이
    
    공기청정기와 제습기를 작동시킬 때 사용합니다.
    
## 전체적인 구조
<img src="https://user-images.githubusercontent.com/38938145/102112905-bb58f180-3e7b-11eb-8dce-abee8ba9e0a7.png"/>

## 텔레그램 결과 화면
<img src="https://user-images.githubusercontent.com/38938145/102322057-d2096080-3fc1-11eb-8d33-adc99b9648ca.jpeg"/>

<img src="https://user-images.githubusercontent.com/38938145/102322167-fbc28780-3fc1-11eb-9d3c-07754db7ece6.jpeg"/>

***
# PMS7003 프로토콜 예제 코드

**라즈베리파이**에서 사용되는 **PMS7003/PMS7003M**의 **Python**예제 코드입니다.  

## PMS7003.py

예제 코드 파일입니다.
직접 실행하는 경우 Serial설정을 환경에 맞게 수정해 주어야 합니다.

```
# USE PORT  
SERIAL_PORT = UART  
```
!!!위 UART 부분을 USB0으로 수정

``sudo python3 PMS7003.py``  
위 명령어로 실행해 주시면 Terminal창에서 데이터를 받아볼 수 있습니다.  
기본값 : UART = '/dev/ttyAMA0'  



## dust_chk.py

위 PMS7003.py 파일을 import 하여 실행하는 예제입니다.  

실행 전 코드의 **시리얼 설정(#USE PORT)** 부분(하단 코드 참고)을 연결 방식에 맞춰 수정해준 뒤   
```
# UART / USB Serial
USB0 =  '/dev/ttyUSB0' #USB 사용시 / USB0이 아닌경우 수정필요 
UART =  '/dev/ttyAMA0' # UART 사용시  
  
# USE PORT  
SERIAL_PORT = UART  #연결방식에 맞춰 변경

#serial setting  
ser = serial.Serial(SERIAL_PORT, Speed, timeout = 1)  
```
``sudo python3 dust_chk.py``   
위 명령어로 실행해 주시면 됩니다.


## data sheet 
PMS7003및 PMS7003M의 데이터시트(영문)이 저장되어 있습니다.


