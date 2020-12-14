transmission_SensorValue.py
======================
* 텔레그램으로 미세먼지, 온습도의 데이터를 받고 창문, 공기청정기, 제습기를 텔레그램으로 제어할 수 있도록 만든 코드입니다.

### 설치한 것
* pip3 install python-telegram-bot --upgrade

***
### 소스코드
* git clone https://github.com/python-telegram-bot/python-telegram-bot --recursive
1. git clone으로 저장소를 다운로드를 합니다.
2. 다운로드한 저장소의 python-telegram-bot/examples 디렉토리 안의 echobot.py를 수정해 사용합니다.

***
### 실행 방법
* python3 transmission_SensorValue.py 로 실행한다.
* 토큰을 넣었던 텔레그램 봇으로 메시지가 전송된다.
* 사용자가 텔레그램에서 /now 입력 시 센서에서 측정한 미세먼지 및 온습도 값이 전송되도록 한다.
* 사용자가 텔레그램에서 /MicroDust 입력 시 인천 미추홀구에 있는 관측소에서 측정한 미세먼지 데이터를 전송한다.
* 사용자가 텔레그램에서 /winopen 및 /winclose 입력 시 모터를 움직여 창문을 열고 닫는다.
* 사용자가 텔레그램에서 /airon 및 /airoff 입력 시 릴레이를 사용해 공기청정기를 작동시키거나 멈춘다.
* 사용자가 텔레그램에서 /dehumidon 및 /dehumidoff 입력 시 릴레이를 사용해 제습기를 작동시키거나 멈춘다.
* 사용자가 텔레그램에서 /help를 입력하면 앞서 설명한 명령어들에 대한 설명을 하는 문구를 전송한다.
